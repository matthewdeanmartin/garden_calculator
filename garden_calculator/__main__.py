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
    print(url)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        food_data = response.json()

        # Get the calorie content for 100g of the food
        calories_per_100g = food_data["foodNutrients"][0]["amount"]

        return calories_per_100g
    else:
        print(f"Request failed {response.status_code}")
        print(response.text)
        # Return None if the request failed
        return None

# Function to search for the food ID of a specific food item
def search_food_id(food_name, brand_owner=None):
    # Base URL for the USDA Food Composition Databases API
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

    # API key (you'll need to obtain your own key from the USDA)
    api_key = os.environ["USDA_API_KEY"]

    # Query parameters for the API request
    params = {
        "query": food_name,
        # "dataType": [ "Foundation"] ,# "Foundation,SR Legacy",
        # "pageSize": 25,
        # "sortBy": "description",
        # "sortOrder": "asc",
        "api_key": api_key
    }
    if brand_owner:
        params["brandOwner"] = brand_owner

    # Make the API request
    response = requests.get(base_url, params=params)
    print(response.url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        food_search_results = response.json()
        print(food_search_results)
        # Get the first result
        first_result = food_search_results["foods"][0]

        # Return the food ID of the first result
        return first_result["fdcId"]
    else:
        print(f"Request failed {response.status_code}")
        print(response.text)
        # Return None if the request failed
        return None

# Example usage
food_name = "cheese"
brand_owner = None # "Kar Nut Products Company"
food_id = search_food_id(food_name, brand_owner)

print("The food ID for", food_name, "is", food_id)


# # Example usage
# potato_calories = get_calories_for_food(potato_food_id)
# tomato_calories = get_calories_for_food(tomato_food_id)
# squash_calories = get_calories_for_food(squash_food_id)

# print("Potatoes contain", potato_calories, "calories per 100g")
# print("Tomatoes contain", tomato_calories, "calories per 100g")
# print("Summer squash contain", squash_calories, "calories per 100g")
