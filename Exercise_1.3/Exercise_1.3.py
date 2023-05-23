
recipes_list =[]

ingredients_list = []

#Defining new function that allows users to input a recipe to a dictionary
def take_recipe ():
  name = str(input("Enter name of the Recipe: "))
  cooking_time = int(input("Enter cooking time in minutes: "))
  ingredients = input("Enter ingredients, use a comma to separate: ")
  recipe = dict({"name": name, "cooking_time": cooking_time, "ingredients": ingredients.split(", " )})
  return recipe

n = int(input("How many recipes they would like to enter?: "))

# Add each ingredient to the ingredients list
for i in range(n):
  recipe = take_recipe()
  print(recipe)

# Checks ingredient list and if new ingredient is found adds it to list
  for ingredient in recipe["ingredients"]:
    if ingredient not in ingredients_list:
        ingredients_list.append(ingredient)

  recipes_list.append(recipe)

# Assesses the difficulty of the recipe to the given criteria and assigns a rating
for recipe in recipes_list:
  if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
    recipe["difficulty"] = "Easy"
  elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
    recipe["difficulty"] = "Medium"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
    recipe["difficulty"] = "Intermediate"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
    recipe["difficulty"] = "Hard"

# Prints a list recipe details
  print("-----------------------------------------")
  print("Recipe: ", recipe["name"])
  print("Cooking time (min): ", str(recipe["cooking_time"]))
  print("Ingredients: ")
  for ingredient in recipe["ingredients"]:
     print(ingredient)
  print("Difficulty: ", recipe["difficulty"])

# Prints a list of all ingredients from all recipes
print("Ingredients available across all recipes")
print("-------------------------------------------")
for ingredient in ingredients_list:
    print(ingredient)
