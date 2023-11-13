spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name']for food in spicy_foods]
    return names



def get_spiciest_foods(spicy_foods):
    spicy = [food for food in spicy_foods if food.get('heat_level', 0)>5]
    return spicy
   


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cuisine = food.get('cuisine')
        heat_level = food.get('heat_level')

        output_string = f"{name} ({cuisine}) | Heat Level: {'🌶' *  heat_level}"
        print(output_string)



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
 

def print_spiciest_foods(spicy_foods):
    heat_level = get_spiciest_foods(spicy_foods)
    print_spicy_foods(heat_level)



def get_average_heat_level(spicy_foods):
    return sum(food['heat_level']for food in spicy_foods)/len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
