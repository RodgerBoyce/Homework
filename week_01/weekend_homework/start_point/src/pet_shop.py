# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name["name"]


def get_total_cash(total):
    return total["admin"]["total_cash"]


def add_or_remove_cash(total_cash, cash):
    total_cash["admin"]["total_cash"] += cash


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, pet_increase):
    shop["admin"]["pets_sold"] += pet_increase
    

def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    pets = []

    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets


def find_pet_by_name(shop, name):

    for pet_name in shop["pets"]:
        if pet_name["name"] == name:
            return pet_name

def remove_pet_by_name(shop, name):

    for pet in shop["pets"]:
      if pet["name"] == name:
        shop["pets"].remove(pet)
        
def add_pet_to_stock(shop, name):

    for pet in shop["pets"]:
        if pet["name"] != name:
            shop["pets"].append(pet)


