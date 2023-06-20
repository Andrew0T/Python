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
        recipe (dictionary): Stores the name, cooking_time, and ingredients variables 
        recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}.
    
    Define recipes and ingredients lists
    User can enter recipes which are then added to the Recipes List
    with the recipe's name, cooking time and ingredients
    A "for" loop sort the ingredients individually then 
    adds each to the Ingredients List
    Another "for" loop determines difficulty of each recipe using certain criteria,
    then prints the value of each recipe within the Recipe List plus Difficulty
    Prints all ingredients from Ingredients List


Exercise 1.4: File Handling in Python
    Learning Goals

    Use files to store and retrieve data in Python
    
    Create a recipe_input.py to store recipe data to a .bin binary file
    Create a binary file should one no exist
    Create a recipe_search.py to retrieve the recipe data from this binary file
    

Exercise 1.5: Object-Oriented Programming in Python

    Learning Goals
    
    Apply object-oriented programming concepts to a Recipe app
    
    Create recipe_oop.py in which:

        Build a Recipe class with relevant data and procedural attributes (data attributes and methods)
        Create and store recipes using class methods
        Use these class methods to search for recipes according to specific ingredients.

    Folders / Files

        Code Practice folder that contains the screenshots and file for the optional task
        Screenshots of the task (recipe_list.png, recipe_search.png)
        recipe_oop.py
        learning journal 1.5

Exercise 1.6: Connecting to Databases in Python

Learning Goals

Create a MySQL database for the Recipe app


Exercise 1.7: Finalizing the Python Program
Learning Goals

Interact with a database using an object-relational mapper
Build your final command-line Recipe application



Exercise 2.1: Getting Started with Django

Learning Goals

Explain MVT architecture and compare it with MVC
Summarise Django’s benefits and drawbacks 
Install and get started with Django


Exercise 2.2: Django Project Set Up

Learning Goals

Describe the basic structure of a Django project 
Summarise the difference between projects and apps
Create a Django project and run it locally
Create a superuser for a Django web application

Exercise 2.3: Django Models

Learning Goals

Discuss Django models, the “M” part of Django’s MVT architecture
Create apps and models representing different parts of your web application 
Write and run automated tests


  Task 2.4
Task Goals

    Define the view (recipe_home in recipes/views.py)
    Create the template for the defined view (recipe_home.html)
    Map URL to the vie

    w in recipes/urls.py
    Register the view and URL in the main urls.py

