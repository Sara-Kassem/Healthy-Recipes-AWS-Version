from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Course, Recipe, Ingredients, Directions, Base

engine = create_engine('sqlite:////var/www/healthyRecipes/healthyRecipes/healthyRecipes.db?check_same_thread=False')

DBSession = sessionmaker(bind=engine)
session = DBSession()

# -------------------------------- #
#         Add all Courses          #
# -------------------------------- #

# Add Soup to courses
soup = Course(
    id='1',
    name='Soup'
    )

session.add(soup)
session.commit()

# Add Side Dish to courses
side_dish = Course(
    id="2",
    name="Side Dish"
    )
session.add(side_dish)
session.commit()

# Add Appetizer to courses
appetizer = Course(
    id="3",
    name="Appetizer"
    )
session.add(appetizer)
session.commit()

# Add Dessert to courses
dessert = Course(
    id="4",
    name="Dessert"
    )
session.add(dessert)
session.commit()

# Add Breakfast to courses
breakfast = Course(
    id="5",
    name="Breakfast"
    )
session.add(breakfast)
session.commit()

# Add Main Dish to courses
main_dish = Course(
    id="6",
    name="Main Dish"
    )
session.add(main_dish)
session.commit()

# Add Brunch to courses
brunch = Course(
    id="7",
    name="Brunch"
    )
session.add(brunch)
session.commit()

# Add Smoothie to courses
smoothie = Course(
    id="8",
    name="Smoothie"
    )
session.add(smoothie)
session.commit()

# Add Salad to courses
salad = Course(
    id="9",
    name="Salad"
    )
session.add(salad)
session.commit()

print ("All Courses were added successfully!")

# ----------------------------------------------------------------------------#
#                              Add Soup Recipes                               #
# ----------------------------------------------------------------------------#

# ------------------------------------------------------- #
#         Crushed Lentil Soup with Lamb Meatballs         #
# ------------------------------------------------------- #

lentil_soup = Recipe(
    id='1',
    name='Crushed Lentil Soup with Lamb Meatballs',
    image="crushed-lentil-soup-with-lamb-meatballs.jpg",
    course_id=soup.id,
    )

session.add(lentil_soup)
session.commit()

# ------------------------------------------------------- #
#   Crushed Lentil Soup with Lamb Meatballs Ingredients   #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='1',
    ingredient='crushed Lentil Soup'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='2',
    ingredient='2T. extra virgin Olive oil'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='3',
    ingredient='1 lg. yellow onion, diced (about 2 cups)'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='4',
    ingredient='1 lg. carrot, diced (about 1/2 cup)'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='5',
    ingredient='1 celery stalk, diced (about 1/2 cup)'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='6',
    ingredient='5 garlic cloves, minced'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='7',
    ingredient='3 fresh bay leaves'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='8',
    ingredient='1/2 c. red split lentils'
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='9',
    ingredient='1/2 c. brown rice'
    )

session.add(ingredient009)
session.commit()

ingredient010 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='10',
    ingredient='2 1/2 tsp. curry powder'
    )

session.add(ingredient010)
session.commit()

ingredient011 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='11',
    ingredient='1 1/2 tsp. sea salt'
    )

session.add(ingredient011)
session.commit()

ingredient012 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='12',
    ingredient='1/4 tsp. crushed red pepper'
    )

session.add(ingredient012)
session.commit()

ingredient013 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='13',
    ingredient='1/2 tsp. black pepper'
    )

session.add(ingredient013)
session.commit()

ingredient014 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='14',
    ingredient='7 c. vegetable broth, divided'
    )

session.add(ingredient014)
session.commit()

ingredient015 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='15',
    ingredient='Lamb Meatballs'
    )

session.add(ingredient015)
session.commit()

ingredient016 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='16',
    ingredient='3 T. olive oil'
    )

session.add(ingredient016)
session.commit()

ingredient017 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='17',
    ingredient='2 slices Udis Whole Grain Gluten Free Bread, crumbled'
    )

session.add(ingredient017)
session.commit()

ingredient018 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='18',
    ingredient='1/4 c. organic whole milk'
    )

session.add(ingredient018)
session.commit()

ingredient019 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='19',
    ingredient='1 lb. grassfed ground lamb'
    )

session.add(ingredient019)
session.commit()

ingredient020 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='20',
    ingredient='1 c. slivered and toasted almonds, chopped'
    )

session.add(ingredient020)
session.commit()

ingredient021 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='21',
    ingredient='1 smallish yellow onion (about &frac13; cup)'
    )

session.add(ingredient021)
session.commit()

ingredient022 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='22',
    ingredient='1/3 c. golden raisins, chopped'
    )

session.add(ingredient022)
session.commit()

ingredient023 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='23',
    ingredient='1 beaten egg'
    )

session.add(ingredient023)
session.commit()

ingredient024 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='24',
    ingredient='3 garlic cloves, minced'
    )

session.add(ingredient024)
session.commit()

ingredient025 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='25',
    ingredient='2 T. fresh chopped parsley'
    )

session.add(ingredient025)
session.commit()

ingredient026 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='26',
    ingredient='1 T. fresh chopped cilantro'
    )

session.add(ingredient026)
session.commit()

ingredient027 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='27',
    ingredient='1 tsp. kosher salt'
    )

session.add(ingredient027)
session.commit()

ingredient028 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='28',
    ingredient='Yogurt Sauce'
    )

session.add(ingredient028)
session.commit()

ingredient029 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='29',
    ingredient='1 c. organic plain yogurt'
    )

session.add(ingredient029)
session.commit()

ingredient030 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='30',
    ingredient='1 T. chopped mint'
    )

session.add(ingredient030)
session.commit()

ingredient031 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='31',
    ingredient='1/2 tsp. lemon zest'
    )

session.add(ingredient031)
session.commit()

ingredient032 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='32',
    ingredient='1/2 tsp. lemon juice'
    )

session.add(ingredient032)
session.commit()

ingredient033 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='33',
    ingredient='1 tsp. honey (optional since I gave up sugar)'
    )

session.add(ingredient033)
session.commit()

ingredient034 = Ingredients(
    recipe_id=lentil_soup.id,
    ingr_number='34',
    ingredient='Pinch of salt'
    )

session.add(ingredient034)
session.commit()

# ------------------------------------------------------- #
#    Crushed Lentil Soup with Lamb Meatballs Directions   #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=lentil_soup.id,
    step_number='1',
    step=(
        "In a large stock pot on medium-high heat, saute onion and garlic "
        "for a few minutes or until onion is tender and translucent."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=lentil_soup.id,
    step_number='2',
    step=(
        "Add 5 c. vegetable broth, lentils, brown rice, curry powder, sea "
        "salt, crushed red pepper."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=lentil_soup.id,
    step_number='3',
    step=(
        "Bring to a boil and then reduce to a simmer. Cover and cook for "
        "about 20 minutes or until tender."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=lentil_soup.id,
    step_number='4',
    step=(
        "While the soup is cooking, prepare the meatballs. Preheat the oven "
        "to 350 degrees."
        )
    )

session.add(direction004)
session.commit()

direction005 = Directions(
    recipe_id=lentil_soup.id,
    step_number='5',
    step='Soak breadcrumbs with milk in a small bowl.'
    )

session.add(direction005)
session.commit()

direction006 = Directions(
    recipe_id=lentil_soup.id,
    step_number='6',
    step=(
        "In a large bowl, using two forks, combine lamb, almonds, onion, "
        "raisins, egg, soaked breadcrumbs, garlic, parsley, cilantro, crushed red "
        "pepper salt and pepper."
        )
    )

session.add(direction006)
session.commit()

direction007 = Directions(
    recipe_id=lentil_soup.id,
    step_number='7',
    step='Form the mixture into 16 nicely sized meatballs.'
    )

session.add(direction007)
session.commit()

direction008 = Directions(
    recipe_id=lentil_soup.id,
    step_number='8',
    step=(
        "Heat large oven proof skillet with olive oil. Sear the meatballs on "
        "all sides over high heat."
        )
    )

session.add(direction008)
session.commit()

direction009 = Directions(
    recipe_id=lentil_soup.id,
    step_number='9',
    step=(
        "Transfer the skillet to the oven and cook for about 15 minutes or "
        "until done through."
        )
    )

session.add(direction009)
session.commit()

direction010 = Directions(
    recipe_id=lentil_soup.id,
    step_number='10',
    step=(
        "While the meatballs are cooking, remove about 1 c. of the lentils & "
        "rice mixture and the bay leaves. Set lentils and rice mixture aside. "
        "Discard the bay leaves."
        )
    )

session.add(direction010)
session.commit()

direction011 = Directions(
    recipe_id=lentil_soup.id,
    step_number='11',
    step=(
        "Using a immersion blender, blend the soup until smooth. You can "
        "also use a food processor or a regular blender. If using a blender, allow "
        "the soup to cool for about 5-10 minutes and then blend carefully. No "
        "explosions please!! That\'s why I love my immersion blender."
        )
    )

session.add(direction011)
session.commit()

direction012 = Directions(
    recipe_id=lentil_soup.id,
    step_number='12',
    step=(
        "Once blended and back in the same pot, add the reserved lentils and "
        "rice back in for some texture."
        )
    )

session.add(direction012)
session.commit()

direction013 = Directions(
    recipe_id=lentil_soup.id,
    step_number='13',
    step=(
        "Add 2 more cups of vegetable broth, stir and cook for a few minutes "
        "more. Keep warm."
        )
    )

session.add(direction013)
session.commit()

direction014 = Directions(
    recipe_id=lentil_soup.id,
    step_number='14',
    step=(
        "Make the yogurt sauce by combining the yogurt, mint, lemon zest, "
        "juice, honey, if using and salt."
        )
    )

session.add(direction014)
session.commit()

direction015 = Directions(
    recipe_id=lentil_soup.id,
    step_number='15',
    step=(
        "Serve the soup up with the meatballs and drizzle with the yogurt "
        "sauce. Say Grace and enjoy!!"
        )
    )

session.add(direction015)
session.commit()

print ("Added Crushed Lentil Soup with Lamb Meatballs!")

# ------------------------------------------------------- #
#                Roasted Cherry Tomato Soup               #
# ------------------------------------------------------- #

roasted_tomato = Recipe(
    id='2',
    name='Roasted Cherry Tomato Soup',
    image="roasted-cherry-tomato-soup.jpg",
    course_id=soup.id,
    )

session.add(roasted_tomato)
session.commit()

# ------------------------------------------------------- #
#          Roasted Cherry Tomato Soup Ingredients         #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='1',
    ingredient='1 medium onion, sliced'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='2',
    ingredient='2 pints cherry tomatoes'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='3',
    ingredient='2 cloves garlic'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='4',
    ingredient='2 tablespoons olive oil'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='5',
    ingredient='1/4 teaspoon fine sea salt'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='6',
    ingredient='1/4 teaspoon pepper'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='7',
    ingredient='1 cup low sodium vegetable broth'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='8',
    ingredient='1 tablespoon tomato paste'
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='9',
    ingredient='1/2 teaspoon dried oregano'
    )

session.add(ingredient009)
session.commit()

ingredient010 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='10',
    ingredient='1/2 cup canned full-fat coconut milk'
    )

session.add(ingredient010)
session.commit()

ingredient011 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='11',
    ingredient='1/4 teaspoon fine sea salt'
    )

session.add(ingredient011)
session.commit()

ingredient012 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='12',
    ingredient='plenty of chopped fresh basil, for serving'
    )

session.add(ingredient012)
session.commit()

ingredient013 = Ingredients(
    recipe_id=roasted_tomato.id,
    ingr_number='13',
    ingredient='your favorite bread (or croutons!), for serving'
    )

session.add(ingredient013)
session.commit()

# ------------------------------------------------------- #
#           Roasted Cherry Tomato Soup Directions         #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=roasted_tomato.id,
    step_number='1',
    step='Preheat the oven to 400F.'
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=roasted_tomato.id,
    step_number='2',
    step=(
        "Add the onion, tomatoes and garlic (leave the cloves whole!) to "
        "a large rimmed baking sheet. Drizzle with the olive oil, then sprinkle "
        "with the salt and pepper. Toss to coat and spread in an even layer. Bake "
        "for about 30 minutes, stirring halfway through, until the tomatoes "
        "have shriveled and started to char. Remove from the oven and let cool "
        "for about 5 minutes."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=roasted_tomato.id,
    step_number='3',
    step=(
        "Add the roasted veggie mixture to a blender, along with the broth, "
        "tomato paste, oregano, coconut milk and salt. Process until smooth. "
        "Transfer the mixture to a medium saucepan."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=roasted_tomato.id,
    step_number='4',
    step=(
        "Set the pan over medium low / low heat and cook for about "
        "10 minutes, stirring occasionally, until warmed through and the flavors "
        "have had a chance to meld. Taste and season with additional salt / pepper "
        "as needed."
        )
    )

session.add(direction004)
session.commit()

direction005 = Directions(
    recipe_id=roasted_tomato.id,
    step_number='5',
    step=(
        "Serve topped with plenty of fresh basil and bread on the "
        "side for dipping!"
        )
    )

session.add(direction005)
session.commit()

print ("Added Roasted Cherry Tomato Soup!")

# ------------------------------------------------------- #
#         7 Ingredient Coconut Curry Seafood Soup         #
# ------------------------------------------------------- #

coconut_curry = Recipe(
    id='3',
    name='7 Ingredient Coconut Curry Seafood Soup',
    image="7-ingredient-coconut-curry-seafood-soup.jpg",
    course_id=soup.id
    )

session.add(coconut_curry)
session.commit()

# ------------------------------------------------------- #
#    7 Ingredient Coconut Curry Seafood Soup Ingredients  #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='1',
    ingredient='1 6oz can of clams, drained'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='2',
    ingredient='1 6oz can of salad shrimp, drained'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='3',
    ingredient='32 oz low sodium vegetable broth'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='4',
    ingredient='1 package of frozen stir-fry veggies'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='5',
    ingredient='2 tbsp coconut milk powder'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='6',
    ingredient='1 tbsp thai red curry paste'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=coconut_curry.id,
    ingr_number='7',
    ingredient='1 tsp dried ginger powder'
    )

session.add(ingredient007)
session.commit()

# ------------------------------------------------------- #
#    7 Ingredient Coconut Curry Seafood Soup Directions   #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=coconut_curry.id,
    step_number='1',
    step='Simmer all ingredients in a soup pot for 25 minutes.'
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=coconut_curry.id,
    step_number='2',
    step=(
        "Serve with minced cilantro, crushed roasted peanuts, "
        "and shredded coconut."
        )
    )

session.add(direction002)
session.commit()

print ("Added 7 Ingredient Coconut Curry Seafood Soup!")

# ----------------------------------------------------------------------------#
#                              End Soup Recipes                               #
# ----------------------------------------------------------------------------#

# ----------------------------------------------------------------------------#
#                            Add Side Dish Recipes                            #
# ----------------------------------------------------------------------------#

# ------------------------------------------------------- #
#             Thai Pomelo Crab Salad Avocados             #
# ------------------------------------------------------- #

pomelo_avocados = Recipe(
    id='4',
    name='Thai Pomelo Crab Salad Avocados',
    image="thai-pomelo-crab-salad-avocados.jpg",
    course_id=side_dish.id
    )

session.add(pomelo_avocados)
session.commit()

# ------------------------------------------------------- #
#       Thai Pomelo Crab Salad Avocados Ingredients       #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='1',
    ingredient=(
        "pomelo - 1 large pomelo (1.5 cups) segmented and pulled apart "
        "to small pieces (can exchange with 1 large grapefruit and 1 medium "
        "orange)"
        )
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='2',
    ingredient='shallots - 4-5 peeled and chopped finely'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='3',
    ingredient='garlic - 2 cloves peeled and chopped finely'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='4',
    ingredient=(
        "crab meat - 450 grams (1 cup) gluten-free imitation crab or "
        "steamed fresh crab picked over for shells)"
        )
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='5',
    ingredient=(
        "coconut oil - 2 tablespoons melted or olive oil if you prefer "
        "(I love that tropical flavor with the coconut oil)"
        )
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='6',
    ingredient=(
        "lemon juice - juice of a lemon (extra lemon to prepare the "
        "avocados) You can also use limes but I only had lemons on hand"
        )
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='7',
    ingredient=(
        "chili peppers - 1 finely chopped (to taste) I used a Thai "
        "chili but you can use any kind you wish or none at all if you like it"
        "mild"
        )
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='8',
    ingredient='salt and pepper - to taste '
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=pomelo_avocados.id,
    ingr_number='9',
    ingredient='avocados - 2 - 3 whole'
    )

session.add(ingredient009)
session.commit()

# ------------------------------------------------------- #
#       Thai Pomelo Crab Salad Avocados Directions        #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='1',
    step=(
        "Segment your your pomelo (or grapefruit and oranges), pull apart "
        "gently into small pieces and set aside."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='2',
    step=(
        "In a small frying pan saute your shallots and garlic in a little "
        "bit of olive oil or coconut oil just until aromatic. Set Aside to cool."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='3',
    step=(
        "In a medium bowl, add your chopped gluten-free imitation crab-meat "
        "or fresh steamed crab meat, picked over for shells. Add the cooled shallots "
        "and garlic, pomelo, olive oil (melted coconut oil), lemon juice, chili "
        "peppers and salt and pepper to taste. Toss gently to incorporate "
        "ingredients. Set aside."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='4',
    step=(
        "Cut your avocados in half. Carefully remove the pit a small "
        "teaspoon full of the the avocado meat to give more room for the Thai Pomelo "
        "Crab Salad. That extra spoonful is a treat for the cook of course! Sprinkle "
        "the juice of the lemon inside the avocado to prevent the oxidation process "
        "from occurring. Season with salt and pepper as desired."
        )
    )

session.add(direction004)
session.commit()

direction005 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='5',
    step=(
        "Place a few mounding tablespoons of Thai Pomelo Crab Salad in the "
        "center of the avocado and mound up high. Enjoy!"
        )
    )

session.add(direction005)
session.commit()

direction006 = Directions(
    recipe_id=pomelo_avocados.id,
    step_number='6',
    step=(
        "***You can make your Thai Pomelo Crab Salad up to 24 hours in "
        "advance. Cut your avocados in half and sprinkle with lemon juice just "
        "before you are ready to serve."
        )
    )

session.add(direction006)
session.commit()

print ("Added Thai Pomelo Crab Salad Avocados!")

# ------------------------------------------------------- #
#             Cilantro-Jalapeno Grilled Shrimp            #
# ------------------------------------------------------- #

jalapeno_shrimp = Recipe(
    id='5',
    name='Cilantro-Jalapeno Grilled Shrimp',
    image="cilantro-jalapeno-grilled-shrimp.jpg",
    course_id=side_dish.id
    )

session.add(jalapeno_shrimp)
session.commit()

# ------------------------------------------------------- #
#       Cilantro-Jalapeno Grilled Shrimp Ingredients      #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='1',
    ingredient='8 oz fresh or frozen large shrimp in shells (peel & devein)'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='2',
    ingredient='1 1/2 cup fresh cilantro (washed)'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='3',
    ingredient='1/4 cup squeezed lime juice'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='4',
    ingredient='2 fresh jalapeno peppers (seeded)'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='5',
    ingredient='2 tbsp olive oil'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='6',
    ingredient='1 medium mango (peeled and cut into small strips)'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='7',
    ingredient='1 cup jicama (peeled and cut into small strips)'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='8',
    ingredient='1/4 cup red onion (chopped)'
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='9',
    ingredient='1/4 cup cucumber (sliced)'
    )

session.add(ingredient009)
session.commit()

ingredient010 = Ingredients(
    recipe_id=jalapeno_shrimp.id,
    ingr_number='10',
    ingredient='salt to taste'
    )

session.add(ingredient010)
session.commit()

# ------------------------------------------------------- #
#       Cilantro-Jalapeno Grilled Shrimp Directions       #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=jalapeno_shrimp.id,
    step_number='1',
    step='If using frozen shrimp, thaw shrimp by putting it in a cold water.'
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=jalapeno_shrimp.id,
    step_number='2',
    step=(
        "Now lets make our marinade: In a blender blend cilantro, lime "
        "juice, jalapeno peppers and olive oil. Reserve 2 tablespoons for mango "
        "salad."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=jalapeno_shrimp.id,
    step_number='3',
    step=(
        "To make mango salad: In a medium size mixing bowl combine mango, "
        "cucumber, jicama, red onion, 2 tablespoons of cilantro marinade and season "
        "with salt to taste. Garnish with chopped cilantro. Mix and set aside."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=jalapeno_shrimp.id,
    step_number='4',
    step=(
        "Dry shrimps with a paper towel. Place shrimp in a bowl and add "
        "cilantro marinade. Marinade for 20 minutes. Thread 3 shrimp into 10 inch "
        "skewers. Grill on a charcoal or gas grill over medium heat, for about 4 "
        "minutes on each side, or until shrimp is cooked."
        )
    )

session.add(direction004)
session.commit()

direction005 = Directions(
    recipe_id=jalapeno_shrimp.id,
    step_number='5',
    step='Serve with mango salad. Enjoy'
    )

session.add(direction005)
session.commit()

print ("Added Cilantro-Jalapeno Grilled Shrimp!")

# ------------------------------------------------------- #
#              Sesame Miso Chicken Meatballs              #
# ------------------------------------------------------- #

sesame_chicken = Recipe(
    id='6',
    name='Sesame Miso Chicken Meatballs',
    image="sesame-miso-chicken-meatballs.jpg",
    course_id=side_dish.id
    )

session.add(sesame_chicken)
session.commit()

# ------------------------------------------------------- #
#         Sesame Miso Chicken Meatballs Ingredients       #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='1',
    ingredient='Ground chicken - 1/2 pound (8 ounces)'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='2',
    ingredient='Tofu - 1/3 cup firm'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='3',
    ingredient='Green onions - 1/4 cup chopped finely '
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='4',
    ingredient='Miso paste - 1 tablespoon (gluten-free)'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='5',
    ingredient='Ginger - 1 tablespoon'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='6',
    ingredient='Tamari (soy sauce) - 1 tablespoon'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='7',
    ingredient='White pepper - 1/2 teaspoon'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='8',
    ingredient='Sesame oil - 1 teaspoon'
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='9',
    ingredient='Sesame seeds - 3 tablespoons toasted white '
    )

session.add(ingredient009)
session.commit()

ingredient010 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='10',
    ingredient='Ponzu Dipping Sauce'
    )

session.add(ingredient010)
session.commit()

ingredient011 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='11',
    ingredient='Tamari (soy sauce) - 3 tablespoons'
    )

session.add(ingredient011)
session.commit()

ingredient012 = Ingredients(
    recipe_id=sesame_chicken.id,
    ingr_number='12',
    ingredient='Lime juice - 2 tablespoons'
    )

session.add(ingredient012)
session.commit()

# ------------------------------------------------------- #
#         Sesame Miso Chicken Meatballs Directions        #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=sesame_chicken.id,
    step_number='1',
    step=(
        "In a bowl mix ground chicken, tofu, green onions, miso paste, "
        "ginger, tamari (soy sauce), white pepper, sesame oil and mix until well "
        "incorporated."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=sesame_chicken.id,
    step_number='2',
    step=(
        "Roll chicken mixture into 1 and 1/2 inch balls and then roll into "
        "toasted sesame seeds to cover chicken meatball completely. Set aside on a "
        "parchment paper lined baking dish or well greased pan. (They have "
        "a tendency to stick so don't skip this step)"
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=sesame_chicken.id,
    step_number='3',
    step=(
        "You can either bake uncovered for approximately 20 minutes in a 190  "
        "degree C (375 degrees F) oven until golden brown and no longer pink inside. "
        "Or you can pan fry for approximately 12 minutes on medium low heat and "
        "turning occasionally so they brown on all sides. When the chicken meatballs "
        "are done, they will be slightly firm to the touch and no longer pink "
        "inside."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=sesame_chicken.id,
    step_number='4',
    step=(
        "While your chicken meatballs are cooking, prepare the ponzu dipping "
        "sauce. In a small bowl add tamari (soy sauce), lime juice and sesame oil "
        "and mix."
        )
    )

session.add(direction004)
session.commit()

direction005 = Directions(
    recipe_id=sesame_chicken.id,
    step_number='5',
    step=(
        "Enjoy Sesame Miso Chicken Meatballs with the ponzu sesame sauce! "
        "Garnish with green onions if desired."
        )
    )

session.add(direction005)
session.commit()

print ("Added Sesame Miso Chicken Meatballs!")

# ----------------------------------------------------------------------------#
#                            End Side Dish Recipes                            #
# ----------------------------------------------------------------------------#

# ----------------------------------------------------------------------------#
#                            Add Appetizer Recipes                            #
# ----------------------------------------------------------------------------#

# ------------------------------------------------------- #
#            Garlic-Herb Parmesan Dipping Sticks          #
# ------------------------------------------------------- #

parmesan_sticks = Recipe(
    id='7',
    name='Garlic-Herb Parmesan Dipping Sticks',
    image="garlic-herb-parmesan-dipping-sticks.jpg",
    course_id=appetizer.id
    )

session.add(parmesan_sticks)
session.commit()

# ------------------------------------------------------- #
#      Garlic-Herb Parmesan Dipping Sticks Ingredients    #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='1',
    ingredient='1 package (13.8 ounces) refrigerated pizza dough'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='2',
    ingredient='3/4 cup light garlic-and-herb spreadable cheese'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='3',
    ingredient='3/4 cup shredded Italian cheese blend'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='4',
    ingredient='1/4 cup grated Parmesan cheese'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='5',
    ingredient='1/2 teaspoon dried oregano'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=parmesan_sticks.id,
    ingr_number='6',
    ingredient=(
        "Warm marinara sauce and/or reduced-fat ranch salad dressing "
        "(optional)"
        )
    )

session.add(ingredient006)
session.commit()

# ------------------------------------------------------- #
#      Garlic-Herb Parmesan Dipping Sticks Directions     #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=parmesan_sticks.id,
    step_number='1',
    step=(
        "Preheat oven to 400F. Spray baking sheet with nonstick "
        "cooking spray."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=parmesan_sticks.id,
    step_number='2',
    step=(
        "Roll out dough on lightly floured surface to 12-inch square. "
        "Place prepared baking sheet. Bake 10 minutes."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=parmesan_sticks.id,
    step_number='3',
    step=(
        "Spread garlic-and-herb spreadable cheese evenly over crust. Layer "
        "evenly with Italian cheese blend, Parmesan cheese, and oregano. Bake 15 "
        "minutes or until golden brown."
        )
    )

session.add(direction003)
session.commit()

direction004 = Directions(
    recipe_id=parmesan_sticks.id,
    step_number='4',
    step=(
        "Slice lengthwise into 8 rows; slice opposite direction into 3 rows. "
        "Serve with marinara sauce or ranch for dipping, if desired."
        )
    )

session.add(direction004)
session.commit()

print ("Added Garlic-Herb Parmesan Dipping Sticks!")

# ------------------------------------------------------- #
#                    Party Pitas Recipe                   #
# ------------------------------------------------------- #

party_pitas = Recipe(
    id='8',
    name='Party Pitas Recipe',
    image="party-pitas-recipe.jpg",
    course_id=appetizer.id
    )

session.add(party_pitas)
session.commit()

# ------------------------------------------------------- #
#               Party Pitas Recipe Ingredients            #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='1',
    ingredient='1 package (8 ounces) cream cheese, softened'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='2',
    ingredient='1/2 cup mayonnaise'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='3',
    ingredient='1/2 teaspoon dill weed'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='4',
    ingredient='1/4 teaspoon garlic salt'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='5',
    ingredient='4 whole pita breads'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='6',
    ingredient='1-1/2 cups fresh baby spinach'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='7',
    ingredient='1 pound shaved fully cooked ham'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=party_pitas.id,
    ingr_number='8',
    ingredient='1/2 pound thinly sliced Monterey Jack cheese'
    )

session.add(ingredient008)
session.commit()

# ------------------------------------------------------- #
#               Party Pitas Recipe Directions             #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=party_pitas.id,
    step_number='1',
    step=(
        "Combine the cream, mayonnaise, dill and garlic salt. Cut each pita "
        "in half horizontally; spread 2 tablespoons mixture onto each cut "
        "surface."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=party_pitas.id,
    step_number='2',
    step=(
        "On four pita halves, layer spinach, ham and cheese. Top with "
        "remaining pita halves. Cut each sandwich into four wedges; secure with "
        "toothpicks. Yield: 16 pieces."
        )
    )

session.add(direction002)
session.commit()

print ("Added Party Pitas Recipe!")

# ------------------------------------------------------- #
#                 Mediterranean Tuna Cups                 #
# ------------------------------------------------------- #

tuna_cups = Recipe(
    id='9',
    name='Mediterranean Tuna Cups',
    image="mediterranean-tuna-cups.jpg",
    course_id=appetizer.id
    )

session.add(tuna_cups)
session.commit()

# ------------------------------------------------------- #
#            Mediterranean Tuna Cups Ingredients          #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='1',
    ingredient='3 English cucumbers'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='2',
    ingredient='2/3 cup plain nonfat Greek yogurt'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='3',
    ingredient='1/3 cup coarsely chopped pitted Kalamata olives'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='4',
    ingredient='1/3 cup finely chopped red onion'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='5',
    ingredient='2 tablespoons fresh lemon juice'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='6',
    ingredient='1/4 teaspoon garlic salt'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=tuna_cups.id,
    ingr_number='7',
    ingredient=(
        "2 cans (5 ounces each) solid white albacore tuna in water, "
        "drained and flaked"
        )
    )

session.add(ingredient007)
session.commit()

# ------------------------------------------------------- #
#            Mediterranean Tuna Cups Directions           #
# ------------------------------------------------------- #

direction001 = Directions(
    recipe_id=tuna_cups.id,
    step_number='1',
    step=(
        "Cut ends off of each cucumber; cut each cucumber into 10 slices. "
        "Scoop out cucumber slices with a rounded 1/2 teaspoon, leaving thick "
        "shell."
        )
    )

session.add(direction001)
session.commit()

direction002 = Directions(
    recipe_id=tuna_cups.id,
    step_number='2',
    step=(
        "Stir yogurt, olives, onion, lemon juice, and garlic in large bowl "
        "until smooth and well blended. Stir in tuna."
        )
    )

session.add(direction002)
session.commit()

direction003 = Directions(
    recipe_id=tuna_cups.id,
    step_number='3',
    step=(
        "Spoon about 1 tablespoon tuna salad into each cucumber cup. Serve "
        "immediately."
        )
    )

session.add(direction003)
session.commit()

print ("Added Mediterranean Tuna Cups!")

# ----------------------------------------------------------------------------#
#                            End Appetizer Recipes                            #
# ----------------------------------------------------------------------------#

print ("All Recipes Were Added Successfully!")
