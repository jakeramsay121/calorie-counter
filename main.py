import calorie_counter

def main():
    food_dict = {}
    print("Welcome to the Calorie Counter")

    while True:
        food_item = input("Enter a food item (or type 'done' to finish): ")
        if food_item.lower() == 'done':
            break

        try:
            calories = int(input(f"Enter calories for {food_item}: "))
            calorie_counter.add_food(food_dict, food_item, calories)
        except ValueError:
            print("Invalid input. Please enter an integer for calories.")
            continue

total_calories, average_calories, highest_calories, lowest_calorie, num_items = calorie_counter.calculate_statistics(food_dict)
max_foods, min_foods = calorie_counter.get_max_min_foods(food_dict)



