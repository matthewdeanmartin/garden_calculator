import os

import requests

# Constants for the food IDs of the crops
potato_food_id = 11507
tomato_food_id = 9072
squash_food_id = 11955

# Function to get the calorie content for a food
def get_calories_for_food(food_id):
    # Base URL for the USDA Food Composition Databases API
    base_url = "https://api.nal.usda.gov/fdc/v1/food/"

    # API key (you'll need to obtain your own key from the USDA)
    api_key = os.environ["USDA_API_KEY"]

    # URL for the API request
    url = f"{base_url}{food_id}?api_key={api_key}"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        food_data = response.json()

        # Get the calorie content for 100g of the food
        calories_per_100g = food_data["foodNutrients"][0]["amount"]

        return calories_per_100g
    else:
        # Return None if the request failed
        return None

# Example usage
potato_calories = get_calories_for_food(potato_food_id)
tomato_calories = get_calories_for_food(tomato_food_id)
squash_calories = get_calories_for_food(squash_food_id)

print("Potatoes contain", potato_calories, "calories per 100g")
print("Tomatoes contain", tomato_calories, "calories per 100g")
print("Summer squash contain", squash_calories, "calories per 100g")
