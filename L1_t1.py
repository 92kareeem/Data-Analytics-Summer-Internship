import pandas as pd

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Split the 'Cuisines' column and explode it to get individual cuisine entries
cuisine_series = data['Cuisines'].str.split(', ').explode()

# Determine the top three most common cuisines
top_cuisines = cuisine_series.value_counts().head(3)
top_cuisines_names = top_cuisines.index.tolist()

# Calculate the percentage of restaurants that serve each of the top cuisines
total_restaurants = len(data)
cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Prepare the results
top_cuisines_results = {
    "Top Cuisines": top_cuisines_names,
    "Cuisines Count": top_cuisines.tolist(),
    "Percentage of Restaurants": cuisine_percentages.tolist()
}

print("Top Three Most Common Cuisines:")
for cuisine, count, percentage in zip(top_cuisines_names, top_cuisines.tolist(), cuisine_percentages.tolist()):
    print(f"{cuisine}: {count} restaurants ({percentage:.2f}%)")