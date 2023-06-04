import mysql.connector

# Initialise connector object
conn = mysql.connector.connect(
  host ='localhost',
  user = 'cf-python',
  passwd = 'password')

#Initialise cursor object from conn
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)
)''')
print("\nWelcome to my Recipes database.")

# Main code
def main_menu(conn, cursor):
  choice = ""
  while(choice != 'quit'):
    print("\nMain Menu")
    print("\n=============================================")
    print("\nPlease choose one of the following options: ")
    print("1. Create a new recipe")
    print("2. Search for a recipe by ingredient")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("5. Show all recipes")
    print("\nType 'quit' to exit the program")
    print("\n")
    choice =input("Your choice: ")

    if choice == '1':
      create_recipe(conn, cursor)
    
    elif choice == '2':
      search_recipe(conn, cursor)

    elif choice == '3':
      update_recipe(conn, cursor)

    elif choice == '4':
      delete_recipe(conn, cursor)
    
    elif choice == '5':
      view_all_recipes(conn, cursor)
    
  conn.close()

def create_recipe(conn, cursor):
  
  name = str(input("Enter name of the recipe: "))
  cooking_time = int(input("Enter cooking time in minutes: "))
  ingredients = str(input("Enter ingredient of the recipe, separate by using a comma: "))
  ingredients_list = ingredients.split(", ")
  difficulty = calculate_difficulty(cooking_time, ingredients_list)

  sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES( %s, %s, %s, %s)'
  val = (name, ingredients, cooking_time, difficulty)
  cursor.execute(sql, val)
  conn. commit()
  print("Recipe" + name + "added to the database.")

def calculate_difficulty(cooking_time, ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    difficulty = "Easy"
  elif cooking_time < 10 and len(ingredients) >= 4:
    difficulty = "Medium"
  elif cooking_time >= 10 and len(ingredients) < 4:
    difficulty = "Intermediate"
  elif cooking_time >= 10 and len(ingredients) >= 4:
    difficulty = "Hard"
  return difficulty

def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    for ingredients in results:
        for ingredients_tup in ingredients:
          ingredients_list = ingredients_tup.split(", ")
          all_ingredients.extend(ingredients_list)

      # Removes duplicate ingredients  
    all_ingredients = list(dict.fromkeys(all_ingredients))

    # All ingredients enumerated
    all_ingredients_list = list(enumerate(all_ingredients))

    print("List of Ingredients: ", )
    print("===========================")
    for ingredients_tup in all_ingredients_list:
      print(str(ingredients_tup[0] + 1) + ". " + ingredients_tup[1])

    try:
      search_number = int(input("Enter the ingredient number: "))
      search_ingredient = all_ingredients_list[search_number - 1][1]

    except:
      print("Unexpected error occured. Please enter a number from this list.")

    else:
      cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s",("%" + search_ingredient +"%",))
      recipes_results = cursor.fetchall()
      print("Recipe found with" + search_ingredient + ": ")
      print("===========================================")
      for row in recipes_results:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty: ", row[4])
        print()

def update_recipe(conn, cursor):
  # Display all recipes
  view_all_recipes(conn, cursor)

  # User asked to select the recipe ID to be updated
  update_id = int(input("Choose the recipe ID number to be updated: "))

  # User asked to select which field is to be updated
  print("Enter the field ID to be updated, (e.g 1,2 or 3): ")
  print(" 1. Name")
  print(" 2. Cooking Time")
  print(" 3. Ingredients")
  selected_field = input("Your choice: ")

  if selected_field == "1": # Update recipe name
    name = str(input("Enter updated name: "))
    cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s",(name, update_id))
    print("Recipe " + name + " updated")
    
  elif selected_field == "2": # Update cooking time
    cooking_time = int(input("Enter updated cooking time in minutes: "))
    cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s",(cooking_time, update_id))
    
    # Recalculate Recipe's difficult when cooking time updated
    cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s",(update_id,))
    ingredients = cursor.fetchall()
    ingredients_list = ingredients[0][0].split(", ")
    difficulty = calculate_difficulty(cooking_time, ingredients_list)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id= %s",(difficulty, update_id))
    
    print("Cooking time for recipe " + str(update_id) + " updated")

  elif selected_field == "3": # Update ingredients
    ingredients = str(input("Enter the ingredients, separate each with a comma: "))
    cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s",(ingredients, update_id))
    
    # Recalculate Recipe's difficulty when ingredients updated
    ingredients_list = ingredients.split(', ')
    cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (update_id,))
    cooking_time = cursor.fetchall()
    difficulty = calculate_difficulty(int(cooking_time[0][0]), ingredients_list)
    cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, update_id))

    print("Ingredients for recipe" + str(update_id) + " updated")

  conn.commit()

def delete_recipe(conn, cursor):
  view_all_recipes(conn, cursor)

  delete_id = int(input("Choose the recipe to be deleted from database: "))
  cursor.execute("DELETE FROM Recipes WHERE id = %s", (delete_id,))
  conn.commit()
  print("Recipe " + str(delete_id) + " has been deleted from database")

def view_all_recipes(conn, cursor):
  cursor.execute("SELECT * FROM Recipes")
  results = cursor.fetchall()
  print("The updated recipe list")
  for row in results:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Ingredients: ", row[2])
    print("Cooking Time: ", row[3])
    print("Difficulty: ", row[4])
    print()

main_menu(conn, cursor)
print("Good-Bye, thank you for using my program.")