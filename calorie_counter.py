def add_food(food_dict, food_item, calories):
    if food_item in food_dict:
        food_dict[food_item] += calories
    else:
        food_dict[food_item] = calories

def calculate_statistics(food_dict):
    total_calories = sum(food_dict.values())
    num_items = len(food_dict)
    average_calories = total_calories / num_items if num_items else 0
    highest_calories = max(food_dict.values(), default=0)
    lowest_calories = min(food_dict.values(), default=0)

    return total_calories, average_calories, highest_calories, lowest_calories, num_items

