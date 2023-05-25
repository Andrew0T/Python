import pickle

with open('recipe_binary.bin', 'rb') as my_file:
  recipe = pickle.load(my_file)

print("Ingredient Name: " + recipe["Ingredient Name"])
print("Ingredients: " + str(recipe["Ingredients"]))
print("Cooking Time: " + str(recipe["Cooking Time"]))
print("Difficulty: " + recipe["Difficulty"])