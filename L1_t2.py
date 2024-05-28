import pandas as pd

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Identify the city with the highest number of restaurants
city_restaurant_counts = data['City'].value_counts()
city_with_most_restaurants = city_restaurant_counts.idxmax()
most_restaurants_count = city_restaurant_counts.max()

# Calculate the average rating for restaurants in each city
city_average_ratings = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
city_with_highest_avg_rating = city_average_ratings.idxmax()
highest_avg_rating = city_average_ratings.max()

# Prepare the results
results = {
    "City with most restaurants": city_with_most_restaurants,
    "Number of restaurants": most_restaurants_count,
    "City with highest average rating": city_with_highest_avg_rating,
    "Highest average rating": highest_avg_rating
}

print("City with the most restaurants:", city_with_most_restaurants)
print("Number of restaurants:", most_restaurants_count)
print("City with the highest average rating:", city_with_highest_avg_rating)
print("Highest average rating:", highest_avg_rating)
