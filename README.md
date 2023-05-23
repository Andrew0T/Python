# Python


Exercise 1.1:

    Task - Goals:

    Create python file with python program to add two numbers using basic python syntax

    add.py file that adds two numbers
    requirments.txt holds dependencies for virtual enviroment
    screenshots of creating new virtual enviroment, installing ipython to enviroment, copy dependencies to a new virtual enviroment


Exercise 1.2:
    
    Task - Goals:

    Chose the data storage type explain why you chose this type.
    Create a recipe list with 5 recipes. The list is to include:

    name (str): Contains the name of the recipe
    cooking_time (int): Contains the cooking time in minutes
    ingredients (list): Contains a number of ingredients, each of the str data type
    
    recipe_1 = {'Name': 'Tea', 'Cooking_Time': '5 Minutes', 'Ingredients':['Tea Leaves', 'Sugar', 'Water']}


    I chose dictionaries for storing the data for each recipe because it allows different data types to be stored and the flexibility that dictionaries brings
    Dictionaries can store the recipe names as strings, the ingredients as lists and for the cooking time as an integer, however I chose to store it as string to include 'minutes' with the integer.
    Dictionaries are also mutable, so each recipe can be updated or added to in future.
    
    all_recipes = []
  
    I chose to use lists for the outer structure to store the recipe dictionaries because lists are sequential, are mutable, able to store multiple recipes and can be updated or added to in future.
  
  
Exercise 1.3: Functions and Other Operations in Python

    Task - Goals

    Implement conditional statements in Python to determine program flow
    Use loops to reduce time and effort in Python programming
    Write functions to organize Python code
    
    def take_recipes () =    
        name (str): Stores the name of the recipe.
        cooking_time (int): Stores the cooking time (in minutes).
        ingredients (list): A list that stores ingredients, each of the string data type.
        recipe (dictionary): Stores the name, cooking_time, and ingredients variables (e.g., recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}).
    
    Define recipes and ingredients lists
    User can enter recipes which are then added to the Recipes List
    with the recipe's name, cooking time and ingredients
    A "for" loop sort the ingredients individually then 
    adds each to the Ingredients List
    Another "for" loop determines difficulty of each recipe using certain criteria,
    then prints the value of each recipe within the Recipe List plus Difficulty
    Prints all ingredients from Ingredients List




  