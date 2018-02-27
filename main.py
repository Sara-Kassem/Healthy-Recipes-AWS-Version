from flask import Flask, render_template, url_for, request, redirect
from flask import jsonify, flash

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course, Recipe, Ingredients, Directions

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('/var/www/healthyRecipes/healthyRecipes/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Healthy Recipes"

# ----------------------- #
#        SQLAlchemy       #
# ----------------------- #

engine = create_engine('sqlite:////var/www/healthyRecipes/healthyRecipes/healthyRecipes.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# --------------------------------------------------------------------------- #
#      Set the number of recipes to be shown in the latest recipes secion     #
# --------------------------------------------------------------------------- #

latestRecipesLimit = 9


# --------------------------------------------------------------------------- #
#                                 Login Page                                  #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# --------------------------------------------------------------------------- #
#                              Connect to Google                              #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('/var/www/healthyRecipes/healthyRecipes/client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    print ("done!")
    return "True"


# --------------------------------------------------------------------------- #
#                            Disconnect from Google                           #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print ('Access Token is None')
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        print (response)
        flash("Current user not connected.")
        return redirect(url_for('homePage'))
    print ('In gdisconnect access token is %s', access_token)
    print ('User name is: ')
    print (login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print ('result is ')
    print (result)
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        print (response)
        return redirect(url_for(request.args.get('next'),
                                course_id=request.args.get('course_id'),
                                recipe_id=request.args.get('recipe_id')))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# --------------------------------------------------------------------------- #
#                              All courses JSON                               #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/courses/JSON')
def coursesJSON():

    # Get the course with id from the database
    courses = session.query(Course).all()

    return jsonify(courses=[i.serialize for i in courses])


# --------------------------------------------------------------------------- #
#                                 Recipe JSON                                 #
# --------------------------------------------------------------------------- #
@app.route(
    '/healthy-recipes/course/<int:course_id>/recipes/<int:recipe_id>/JSON')
def recipeJSON(course_id, recipe_id):

    viewRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    return jsonify(Recipe=viewRecipe.serialize,
                   ingredients=[i.serialize for i in ingredients],
                   directions=[i.serialize for i in directions])


# --------------------------------------------------------------------------- #
#                                 Home Page                                   #
# --------------------------------------------------------------------------- #
@app.route('/')
@app.route('/healthy-recipes')
def homePage():

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the latest added recipes
    latestRecipes = session.query(Recipe).order_by(
        Recipe.id.desc()).limit(latestRecipesLimit)

    # Load index.html
    return render_template('index.html',
                           all_courses=all_courses,
                           latestRecipes=latestRecipes,
                           login_session=login_session
                           )


# --------------------------------------------------------------------------- #
#                         All Recipes in a course                             #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/course/<int:course_id>/')
@app.route('/healthy-recipes/course/<int:course_id>/recipes')
def courseRecipes(course_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with id from the database
    course = session.query(Course).filter_by(id=course_id).one()

    # Get all recipes in the selected courses
    courseRecipes = session.query(Recipe).order_by(Recipe.name).filter_by(
        course_id=course_id).all()

    # Load a page with all recipes in the course
    return render_template('courseRecipes.html',
                           all_courses=all_courses,
                           courseRecipes=courseRecipes,
                           course=course,
                           login_session=login_session
                           )


# --------------------------------------------------------------------------- #
#                           View a recipe details                             #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/course/<int:course_id>/recipes/<int:recipe_id>')
def viewRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    viewRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    # Load a page with the recipe details
    return render_template('viewRecipe.html',
                           all_courses=all_courses,
                           viewRecipe=viewRecipe,
                           recipeCourse=recipeCourse,
                           ingredients=ingredients,
                           directions=directions,
                           login_session=login_session
                           )


# --------------------------------------------------------------------------- #
#                             Delete a Recipe                                 #
# --------------------------------------------------------------------------- #
@app.route(
    '/healthy-recipes/course/<int:course_id>/recipes/<int:recipe_id>/delete',
    methods=['GET', 'POST'])
def deleteRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    deleteRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    # Check if the user is logged in, if not then redirect to the login page
    if 'username' not in login_session:
        return redirect(url_for('showLogin',
                                next=request.endpoint,
                                course_id=course_id,
                                recipe_id=recipe_id))

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # delete the ingredients of the selected recipe
        for i in ingredients:
            session.delete(i)
            session.commit()

        # delete the steps of the selected recipe
        for i in directions:
            session.delete(i)
            session.commit()

        # delete the selected recipe from database
        session.delete(deleteRecipe)
        session.commit()

        flash("Recipe was deleted successfully!")

        # redirect to all recipes in the course after deleting
        return redirect(url_for('courseRecipes',
                                course_id=recipeCourse.id))

    # else, load deleteRecipe.html
    else:
        return render_template('deleteRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               deleteRecipe=deleteRecipe,
                               login_session=login_session
                               )


# --------------------------------------------------------------------------- #
#                               Edit a Recipe                                 #
# --------------------------------------------------------------------------- #
@app.route(
    '/healthy-recipes/course/<int:course_id>/recipes/<int:recipe_id>/edit',
    methods=['GET', 'POST'])
def editRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    editRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(
        recipe_id=recipe_id).all()

    # Check if the user is logged in, if not then redirect to the login page
    if 'username' not in login_session:
        return redirect(url_for('showLogin',
                                next=request.endpoint,
                                course_id=course_id,
                                recipe_id=recipe_id))

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # update recipe name with the new one given in the form if provided
        if request.form['updateName']:
            editRecipe.name = request.form['updateName']

        # update recipe course with the new one given in the form if provided
        if request.form['updateCourse']:
            updateCourse = session.query(Course).filter_by(
                name=request.form['updateCourse']).one()
            editRecipe.course_id = updateCourse.id

        # update the database with the changes
        session.add(editRecipe)
        session.commit()

        # delete all current ingredients
        for i in ingredients:
            session.delete(i)
            session.commit()

        # store each line in ingredients input as an element of a list
        ingredients_line = request.form['updateIngredients'].splitlines()

        # iterate through new ingredients (the list) one by one
        for i in range(len(ingredients_line)):

            # if the current line isn't blank, process the code inside
            if ingredients_line[i]:

                # create a new instance of Ingredients with the input data
                newIngredient = Ingredients(
                    recipe_id=recipe_id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                # add the new ingredient to the database
                session.add(newIngredient)
                session.commit()

        # delete all current directions
        for i in directions:
            session.delete(i)
            session.commit()

        # store each line in directions input as an element of a list
        directions_line = request.form['updateDirections'].splitlines()

        # iterate through new directions (the list) one by one
        for i in range(len(directions_line)):

            # if the current line isn't blank, process the code inside
            if directions_line[i]:

                # create a new instance of Directions with the input data
                newDirection = Directions(
                    recipe_id=recipe_id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                # add the new step to the database
                session.add(newDirection)
                session.commit()

        flash("Recipe was edited successfully!")

        # after updating all the changes, redirect to the selected recipe page
        return redirect(url_for('viewRecipe',
                                course_id=recipeCourse.id,
                                recipe_id=editRecipe.id))

    # else, load editRecipe.html
    else:
        return render_template('editRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               editRecipe=editRecipe,
                               ingredients=ingredients,
                               directions=directions,
                               login_session=login_session
                               )


# --------------------------------------------------------------------------- #
#                             Add a New Recipe                                #
# --------------------------------------------------------------------------- #
@app.route('/healthy-recipes/course/<int:course_id>/recipes/new',
           methods=['GET', 'POST'])
def newRecipe(course_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Check if the user is logged in, if not then redirect to the login page
    if 'username' not in login_session:

        return redirect(url_for('showLogin',
                                next=request.endpoint,
                                course_id=course_id))

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # create a new instance of Recipe with the input data
        newRecipe = Recipe(
            name=request.form['newRecipeName'],
            course_id=course_id
        )

        # add the new recipe to the database
        session.add(newRecipe)
        session.commit()

        # get the added recipe from the database
        addedRecipe = session.query(Recipe).filter_by(
            name=request.form['newRecipeName']).one()

        # store each line in ingredients input as an element of a list
        ingredients_line = request.form['newIngredients'].splitlines()

        # iterate through new ingredients (the list) one by one
        for i in range(len(ingredients_line)):

            # if the current line isn't blank, process the code inside
            if ingredients_line[i]:

                # create a new instance of ingredients with the input data
                newIngredient = Ingredients(
                    recipe_id=addedRecipe.id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                # add the new ingredient to the database
                session.add(newIngredient)
                session.commit()

        # store each line in directions input as an element of a list
        directions_line = request.form['newDirections'].splitlines()

        # iterate through new directions (the list) one by one
        for i in range(len(directions_line)):

            # if the current line isn't blank, process the code inside
            if directions_line[i]:

                # create a new instance of Directions with the input data
                newDirection = Directions(
                    recipe_id=addedRecipe.id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                # add the new step to the database
                session.add(newDirection)
                session.commit()

        flash("Recipe was added successfully!")

        # after adding the new recipe, redirect to its page
        return redirect(url_for('viewRecipe',
                                course_id=course_id,
                                recipe_id=addedRecipe.id))

    # else, load newRecipe.html
    else:
        return render_template('newRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               login_session=login_session
                               )

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = False
    app.run(host='0.0.0.0', port=8080)
