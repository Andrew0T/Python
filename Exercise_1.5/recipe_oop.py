class Recipe(object):

    all_ingredients = []

    def __init__(self, name ):
      self.name = name
      self.ingredients = []
      self.cooking_time = int(0)
      self.difficulty = " "

  # Getter Method for Name
    def get_name(self):
      return self.name

  # Setter Method for Name
    def set_name(self):
        self.name = input("Enter recipe name: ")

  # Getter Method for Cooking Time
    def get_cooking_time(self):
        return self.cooking_time

  # Setter Method for Cooking Time
    def set_cooking_time(self):
        self.cooking_time = int(input("Enter cooking time in minutes: "))

    def add_ingredients(self, *ingredients):
        self.ingredients = list(ingredients)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

# Getter Method for difficulty
    def get_difficulty(self):
        if self.difficulty == " ":
          self.calculate_difficulty()
        return self.difficulty
    
# A method to calculate difficulty using cooking time and number of ingredients values
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
          self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
          self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
          self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
          self.difficulty = "Hard"
        return self.difficulty

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not (ingredient in Recipe.all_ingredients):
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        output = "\nRecipe Name: " + self.get_name() + \
           "\nCooking Time: " + str(self.get_cooking_time()) + \
           "\nDifficulty: " + self.get_difficulty() + \
           "\nIngredients: \n"
        for ingredient in self.ingredients:
            output += ingredient + '\n'
        return output

    def search_ingredient(self, ingredient, ingredients):
        if (ingredient in ingredients):
            return True
        else:
            return False

    def recipe_search(self, recipes_list, ingredient):
      data = recipes_list
      search_term = ingredient
      for recipe in data:
        if self.search_ingredient(search_term, recipe.ingredients):
          print(recipe)

tea = Recipe("Tea")
tea.set_name()
tea.add_ingredients("Tea Leaves", "Water", "Milk")
tea.set_cooking_time()
tea.get_difficulty()
print(tea)

coffee = Recipe("Coffee")
coffee.set_name()
coffee.add_ingredients("Coffee powder", "Water", "Milk")
coffee.set_cooking_time()
coffee.get_difficulty()
print(coffee)

cake = Recipe("Cake")
cake.set_name()
cake.add_ingredients("Flour", "Sugar", "Eggs", "Milk", "Butter", "Vanilla Essence")
cake.set_cooking_time()
cake.get_difficulty()
print(cake)

banana_smoothie = Recipe("Banana smoothie")
banana_smoothie.set_name()
banana_smoothie.add_ingredients("Banana", "Milk", "Sugar", "Ice")
banana_smoothie.set_cooking_time()
banana_smoothie.get_difficulty()
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

print("Recipes List")
for recipe in recipes_list:
    print(recipe)

print("Results for recipe_search with Water: ")
tea.recipe_search(recipes_list, "Water")

print("Results for recipe_search with Sugar: ")
tea.recipe_search(recipes_list, "Sugar")

print("Results for recipe_search with Banana: ")
tea.recipe_search(recipes_list, "Banana")