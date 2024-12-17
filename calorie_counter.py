def add_food(food_dict, food_item, calories):
    if food_item in food_dict:
        food_dict[food_item] += calories
    else:
        food_dict[food_item] = calories