import pandas as pd

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Identify the restaurants with the highest and lowest number of votes
restaurant_with_highest_votes = data.loc[data['Votes'].idxmax()]
restaurant_with_lowest_votes = data.loc[data['Votes'].idxmin()]

# Analyze if there is a correlation between the number of votes and the rating of a restaurant
correlation_votes_rating = data['Votes'].corr(data['Aggregate rating'])

# Prepare the results
votes_analysis_results = {
    "Restaurant with highest votes": {
        "Restaurant Name": restaurant_with_highest_votes['Restaurant Name'],
        "Votes": restaurant_with_highest_votes['Votes'],
        "Rating": restaurant_with_highest_votes['Aggregate rating']
    },
    "Restaurant with lowest votes": {
        "Restaurant Name": restaurant_with_lowest_votes['Restaurant Name'],
        "Votes": restaurant_with_lowest_votes['Votes'],
        "Rating": restaurant_with_lowest_votes['Aggregate rating']
    },
    "Correlation between votes and rating": correlation_votes_rating
}

# Print the results
print("Restaurant with the highest votes:")
print(f"Name: {restaurant_with_highest_votes['Restaurant Name']}")
print(f"Votes: {restaurant_with_highest_votes['Votes']}")
print(f"Rating: {restaurant_with_highest_votes['Aggregate rating']}")

print("\nRestaurant with the lowest votes:")
print(f"Name: {restaurant_with_lowest_votes['Restaurant Name']}")
print(f"Votes: {restaurant_with_lowest_votes['Votes']}")
print(f"Rating: {restaurant_with_lowest_votes['Aggregate rating']}")

print("\nCorrelation between votes and rating:")
print(correlation_votes_rating)
