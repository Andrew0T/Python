import pickle

def display_recipe(recipe):
  print("-----------------------------------------")
  print("Name: ", recipe["name"])
  print("Cooking time (min): ", str(recipe["cooking_time"]))
  print("Ingredients: ", ", " .join(recipe["ingredients"]))
  print("Difficulty: ", recipe["difficulty"])
  print("-------------------------------------------")
        

def search_ingredient(data):
  print("Ingredients available")
  for position, value in enumerate(data["all_ingredients"], 1):
    print("ingredient " + str(position) + ": " + value)
  print("-------------------------------------------")

  try:
    index = int(input("Please enter the ingredient number: "))
    ingredient_searched = data["all_ingredients"][index -1]
  except IndexError:
        print("Number entered is invalid!")
  except:
    print("Sorry something was not correct")
  else:
    for recipe in data["recipes_list"]:
      for ingredient in recipe["ingredients"]:
        if ingredient == ingredient_searched:
          print("This recipe contains to searched ingredient:")
          print("-------------------------------------------")
          display_recipe(recipe)


filename = input("Enter the filename where you've stored your recipes, (include .bin ): ")
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist. Please try again.")

except:
    print("An unexpected error occurred. Please try again")

else:
    search_ingredient(data)
