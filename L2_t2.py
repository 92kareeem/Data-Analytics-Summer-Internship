import pandas as pd

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Identify the most common combinations of cuisines in the dataset
cuisine_combinations = data['Cuisines'].value_counts().head(10)

# Determine if certain cuisine combinations tend to have higher ratings
cuisine_ratings = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
top_cuisine_ratings = cuisine_ratings.loc[cuisine_combinations.index]

# Prepare the results
cuisine_combination_results = {
    "Most common combinations": cuisine_combinations,
    "Average ratings of top combinations": top_cuisine_ratings
}

# Print the results
print("Most Common Combinations of Cuisines:")
print(cuisine_combinations)
print("\nAverage Ratings of Top Cuisine Combinations:")
print(top_cuisine_ratings)
