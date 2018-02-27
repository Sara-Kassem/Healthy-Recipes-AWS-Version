import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# create a table for courses
class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


# create a table for recipes
class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'image': self.image
        }


# create a table for ingredients
class Ingredients(Base):
    __tablename__ = 'ingredients'

    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    ingr_number = Column(Integer)
    ingr_index = Column(Integer, primary_key=True)
    ingredient = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'ingr_number': self.ingr_number,
            'ingredient': self.ingredient
        }


# create a table for directions
class Directions(Base):
    __tablename__ = 'directions'

    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    step_number = Column(Integer)
    step_index = Column(Integer, primary_key=True)
    step = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'step_number': self.step_number,
            'step': self.step,
        }


engine = create_engine('sqlite:////var/www/healthyRecipes/healthyRecipes/healthyRecipes.db?check_same_thread=False')

Base.metadata.create_all(engine)

print ("Database Created!!")
