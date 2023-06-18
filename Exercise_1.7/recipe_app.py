# Creates an engine object that connects to the desired database
from sqlalchemy import create_engine
# Create Base class
from sqlalchemy.orm import declarative_base
# Import column object
from sqlalchemy import Column
# Import Integer and String types
from sqlalchemy.types import Integer, String
# Imports the sessionmaker to make changes to the database
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/task_database")
Base = declarative_base()
# Creates the session object to make changes to the database
Session = sessionmaker(bind=engine)
session = Session()


# Defines Recipe class that inherits Base class
class Recipe(Base):
  __tablename__ = "final_recipes"
  id = Column(Integer, primary_key = True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer())
  difficulty = Column(String(20))
  
  # Shows a quick representation of the recipe show ID, Name and Difficulty
  def __repr__(self):
    return "<Recipe ID: ", + str(self.id) + "Name: " + self.name + "Difficulty: " + self.difficulty + ">"

  # Shows a formatted version of the Recipe
  def __str__(self):
    print("="*60)
    return "Recipe ID: " + str(self.id) +\
        "\nName:  " + self.name +\
        "\nIngredients:\f"+ self.ingredients +\
        "\nCooking Time:  " + str(self.cooking_time) +\
        "\nDifficulty:  " + self.difficulty
    print(end="=")
    print("="*59) 

  # Calculates the difficulty level using the below criteria
  def calculate_difficulty(self):
    if int(self.cooking_time) < 10 and len(self.return_ingredients_as_list()) < 4:
      self.difficulty = "Easy"
    elif int(self.cooking_time) < 10 and len(self.return_ingredients_as_list()) >= 4:
      self.difficulty = "Medium"
    elif int(self.cooking_time) >= 10 and len(self.return_ingredients_as_list()) < 4:
      self.difficulty = "Intermediate"
    elif int(self.cooking_time) >= 10 and len(self.return_ingredients_as_list()) >= 4:
      self.difficulty = "Hard"

  def return_ingredients_as_list(self):
    ingredients_list = []
    if not self.ingredients.split:
      ingredients = self.ingredients.split(", ")  # split the strings and create a list
    return ingredients_list
  
# Create model table
Base.metadata.create_all(engine)

# Users are able to create a recipe using name, ingredients and cooking time.
def  create_recipe(): 
# Prevent user entering more than 50 or incorrect characters.
  correct_input_name = False
  while correct_input_name == False:
    name = input("\nEnter recipe name:  ")
    if len(name) > 50:
      print("\nSorry, only 50 characters can be entered.")
    else: 
      correct_input_name = True

  # User enters number of minutes, only numerical values greater than zero can be entered
  correct_cooking_time_input = False
  while correct_cooking_time_input == False:
    cooking_time = input("\nEnter recipe cooking time in minutes:  ")
    if not cooking_time.isnumeric(): 
      print("\nSorry, will only accept a number.")
    elif int(cooking_time) < 1:
      print("\nSorry, please enter a number greater than zero.")
    else:
      correct_cooking_time_input = True

  # Empty temporary ingredients list
  ingredients_list = []
  # User is asked for the number of ingredients, only numerical values greater than zero can be entered
  correct_ingredient_number = False
  while correct_ingredient_number == False:
    ingredients_number = input("\nHow many ingredients does your recipe have?  ")
    if not ingredients_number.isnumeric():
        print("\nSorry, please enter a number.")
    elif int(ingredients_number) < 1:
      print("\nSorry, please enter a number greater than zero.")
    else:
      correct_ingredient_number = True

  # Ask user for the ingredients, Prevents user from entering more than 255 or incorrect characters
  for i in range(0, int(ingredients_number)):
    correct_ingredients_input = False
    while correct_ingredients_input == False:
      ingredients_input = input("\nEnter an ingredient:  ")
      if len(ingredients_input) > 255:
        print("\nSorry, only 255 characters can be stored")
      else:
        correct_ingredients_input = True
    if ingredients_input not in ingredients_list:
      ingredients_list.append(ingredients_input)    
    
  # Convert ingredients list into a string
  ingredients_str = ", ".join(ingredients_list)

  # Create a new object from the Rceipe model
  recipe_entry = Recipe(
    name  = name,
    cooking_time = cooking_time,
    ingredients = ingredients_str,
    )

  # Generates the difficulty value for this recipe
  recipe_entry.calculate_difficulty()

  # Add this recipe to the database
  session.add(recipe_entry)
  session.commit()
  print("Recipe saved to database.")

def view_all_recipes():
  all_recipes =  session.query(Recipe).all()
  # If no recipes found in database returns to main menu
  if not all_recipes: # session.query(Recipe).count() == 0:
    print("\nSorry, there are no recipes in the database.", end="-  ")
    print("\nPlease enter a recipe")
    return None
  else:
    print("\nAll recipes in the database.")
    print("="*60)
    for recipe in all_recipes:
      print(recipe)
      print("="*60)

def search_by_ingredient():
# If no recipes found in database returns to main menu
  if session.query(Recipe).count() == 0:
    print("\nSorry, there are no recipes in the database.", end="-  ")
    print("\nPlease enter a recipe")
    return None

  else:
    # Retrieves only the values from the ingredients column
    results = session.query(Recipe.ingredients).all()
  # Initialises an empty list called all_ingredients
  all_ingredients = []
  # Append all ingredients to all_ingredients list
  for ingredients_tup in results:
      for ingredients_str in ingredients_tup: 
        ingredients_list = ingredients_str.split(", ") # splits each ingredients from ingredients_tup
        for ingredient in ingredients_list:
          if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

  # Removes duplicate ingredients  
  # all_ingredients = list(dict.fromkeys(all_ingredients))
  # All ingredients enumerated
  # all_ingredients_list = list(enumerate(all_ingredients))

  print("\nList of Ingredients: ", )
  print("="*60)
  for index, ingredients_tup in enumerate(all_ingredients, 1):
    print("\n" + str(index) + ". " + ingredients_tup)

  try:
    # Asks user to choose the ingredient by it's corresponding number
    search_number = input("\nEnter the ingredient's number. You can enter more than one:\t")
    search_number_input = search_number.strip().split(" ")

    # Search ingredients list created to stored the selected ingredients
    search_ingredients = []
    for number in search_number_input:
      search_index = int(number) - 1
      search_ingredient = all_ingredients[search_index]
      search_ingredients.append(search_ingredient)
      print("\nYou have selected the following ingredients:\n", search_ingredients)

    condition_list =[]
    for ingredient in search_ingredients:
      like_term = "%"+ingredient+"%"
      condition = Recipe.ingredients.like(like_term)
      condition_list.append(condition)
      searched_recipes = session.query(Recipe).filter(*condition_list).all()
      # print(searched_recipes)
  except IndexError:
    print("Sorry, the option selected is incorrect")
    return None
  except Exception as error:
    print("\nSorry, something went wrong. Please enter a number from this list.")
    print(error)
    return None
  else:
    print("\nThese recipes contain the selected ingredient\s:")
    print(("="*60))
    for recipe in searched_recipes:
      print(recipe)

def edit_recipe():
  ingredients_list= []
# If no recipes found in database returns to main menu
  if session.query(Recipe).count() == 0:
    print("\nSorry, there are no recipes in the database.", end="-  ")
    print("\nPlease enter a recipe")
    return None

  # Retrieves and shows all stored recipes ID and name to the user
  else:
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("\nAll recipes in the database:\t")
    print("="*50)
    for result in results:
      print( "Recipe ID: " + str(result[0]) +\
             "\nName: " + result[1])
    
    # User to enter recipe ID to be edited
    recipe_id_to_edit = int(input("\nChoose the recipe ID to be edited: "))
    print (session.query(Recipe).with_entities(Recipe.id, Recipe.name).all())

    # Temporary list to hold selected id
    selected_id =[]
    for result in results:
      selected_id.append(selected_id)
    
    recipe_to_edit = session.get(Recipe, int(recipe_id_to_edit))
    print(" 1. Name ")
    print(" 2. Cooking Time")
    print(" 3. Ingredients")
    selected_field = input("Your choice: ")

    if selected_field == "1": # Update recipe name
      correct_input_name = False
      while correct_input_name == False:
        name = input("\nEnter updated name:  ")
        if len(name) > 50:
          print("\nSorry, a maximum of 50 characters can be entered.")
        else: 
          correct_input_name = True
      session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({Recipe.name: name})
      session.commit()
      print("\nRecipe name has been updated.")
        
    elif selected_field == "2": # Update cooking time
      correct_cooking_time_input = False
      while correct_cooking_time_input == False:
        try:
          cooking_time = input("\nEnter updated recipe cooking time in minutes:  ")
          # if not cooking_time.isnumeric():
        except ValueError:
          print("\nSorry, will only accept a number. Please try again")
          continue
        if int(cooking_time) < 1:
          print("\nSorry, please enter a number greater than zero.")
        else:
          correct_cooking_time_input = True
      
      recipe_to_edit.cooking_time = cooking_time
      recipe_to_edit.calculate_difficulty()
      session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({
          Recipe.cooking_time: cooking_time,
          Recipe.difficulty: recipe_to_edit.difficulty
        })
      session.commit()
      print("\nRecipe cooking time has been updated")

    elif selected_field == "3": # Update ingredients
      correct_ingredient_number = False
      while correct_ingredient_number == False:
        ingredients_number = input("\nHow many ingredients does your recipe have?:  ")
        if not ingredients_number.isnumeric():
          print("\nSorry, will only accept a number.")
        elif int(ingredients_number) < 1:
          print("\nSorry, please enter a number greater than zero.")
        else:
          correct_ingredient_number = True
          
      for i in range(int(ingredients_number)):
        correct_ingredients = False
        while correct_ingredients == False:
          ingredients = input("\nEnter an ingredient:  ")
          if len(ingredients) > 255:
            print("\nSorry, only 255 characters can be stored")
          else:
            correct_ingredients = True
        if ingredients not in ingredients_list:
          ingredients_list.append(ingredients)

        recipe_to_edit.ingredients = ingredients
        recipe_to_edit.calculate_difficulty()
        ingredients = ", ".join(ingredients_list)
        session.query(Recipe).filter(Recipe.id == recipe_id_to_edit).update({
          Recipe.ingredients: ingredients,
          Recipe.difficulty: recipe_to_edit.difficulty
        })
        session.commit()
        print("\nIngredients have been updated")
    
    else:
      print("Sorry something went wrong.")
    
    session.commit()

def delete_recipe():
# If no recipes found in database returns to main menu
  if session.query(Recipe).count() == 0:
    print("\nSorry, there are no recipes in the database.", end="-  ")
    return None

# Retrieves and shows all stored recipes ID and name to the user
  else:
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print("\nRecipes in database:  ")
    print("="*50)
    for result in results:
      print( "Recipe ID: " + str(result[0]) +\
             "\nName: " + result[1] )

# User to enter recipe ID to be deleted
  delete_recipe_id = input("\nChoose the recipe ID to be deleted from database:  ")

  choosen_id = []
  for result in results:
    choosen_id.append(result[0])

  if not delete_recipe_id.isnumeric():
    print("\nEnter ID as a number", end=" - ")
    print("please try again")
    
  elif not int(delete_recipe_id) in choosen_id:
    print("\nThe recipe ID choosen does not exist", end=" - ")
    print("please try again")
    
  else:
    recipe_to_be_deleted = session.query(Recipe).filter(Recipe.id == delete_recipe_id).one()
    print("\n!! Danger !! You will delete this recipe!")
    print(recipe_to_be_deleted)
    
    # Ask user to confirm that recipe is to be deleted
    confirm_deletion = input("You sure you want to delete this recipe ID? You must type yes or no):  ")
    if confirm_deletion == "yes":
      session.delete(recipe_to_be_deleted)
      session.commit()
      print("The recipe" + recipe_to_be_deleted.name + " has been deleted from the datbase.")

    elif confirm_deletion == "no":
      return None

# Main code
def main_menu():
  choice = ""
  while(choice != 'quit'):
    print("\nMain Menu\n")
    print("=============================================\n")
    print("Please choose one of the following options:\n")
    print("1. Create a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. Edit a recipe")
    print("4. Delete a recipe")
    print("5. View all recipes")
    print("\nType 'quit' to exit the program")
    choice =input("\nYour choice: ")

    if choice == '1':
      create_recipe()    
    elif choice == '2':
      search_by_ingredient()
    elif choice == '3':
      edit_recipe()
    elif choice == '4':
      delete_recipe()    
    elif choice == '5':
      view_all_recipes()    
    else:
      if choice == "quit":
        print("\nGood-bye\n")
      else:
        print("\nPlease choose a number ", end="-")
        print(" or type quit")
    
session.close()

main_menu()