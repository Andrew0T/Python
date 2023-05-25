import pickle

# Define function take_recipe
def take_recipe():
  name = input("Please enter name of the Recipe: ")
  cooking_time = int(input("Please enter the cooking time in minutes: "))
  ingredients = input("Please enter each ingredient, separate by using a comma: ")
  recipe = dict({
                "name": name,
                "cooking_time": cooking_time,
                "ingredients": ingredients.split(", " )
              })
  recipe["difficulty"] = calc_difficulty(recipe)
  return recipe


# Define function calc_difficulty
def calc_difficulty(recipe):
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
      recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
      recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
      recipe["difficulty"] = "Intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
      recipe["difficulty"] = "Hard"
    return recipe["difficulty"]

# Define the main code
recipes_list =[]
all_ingredients = []

filename = input("Please enter the filename where your recipes are stored: ")
try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Creating new file.")
    data = {
      "recipes_list": recipes_list,
      "all_ingredients": all_ingredients
    }
except:
    print("Sorry, something went wrong. Create new file")
    data = {
      "recipes_list": recipes_list,
      "all_ingredients": all_ingredients
    }
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes they would like to enter?: "))

# Add each ingredient to the ingredients list
for i in range(0, n):
  recipe = take_recipe()
# Checks ingredient list and if new ingredient is found adds it to list
  for ingredient in recipe["ingredients"]:
    if ingredient not in all_ingredients:
        all_ingredients.append(ingredient)
  recipes_list.append(recipe)
  data = {
      "recipes_list": recipes_list,
      "all_ingredients": all_ingredients
    }
  print(recipe)

# Create new file
new_file_name = input("Please enter new file name: ")
with open(new_file_name, "wb") as file:
  pickle.dump(data, file)
