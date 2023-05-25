import pickle

recipe = {
  'Ingredient Name': 'Tea',
  'Ingredients': ['Tea leaves', 'Water', 'Sugar'],
  'Cooking Time': '5 minutes',
  'Difficulty': 'Easy'
}

with open('recipe_binary.bin', 'wb') as my_file:
  pickle.dump(recipe, my_file)