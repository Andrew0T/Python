class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print("Item added to list")
        else:
            print("Item already in list.")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed from list")
        else:
            print("Item not found")

    def view_list(self):
        print(self.shopping_list)

pet_store_list = ShoppingList("Pet Store Shopping List")

item = ["dog food", "frisbee", "bowl","collars", "flea collars"]
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")
pet_store_list.remove_item("flea collars")          # Remove flea collars from list
pet_store_list.add_item("frisbee")                  # Add frisbee again to list
pet_store_list.view_list()
