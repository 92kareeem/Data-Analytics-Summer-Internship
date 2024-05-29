import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Analyze the distribution of aggregate ratings
rating_distribution = data['Aggregate rating'].value_counts().sort_index()

# Determine the most common rating range
most_common_rating = rating_distribution.idxmax()
most_common_rating_count = rating_distribution.max()

# Calculate the average number of votes received by restaurants
average_votes = data['Votes'].mean()

# Prepare the results
rating_analysis_results = {
    "Most common rating": most_common_rating,
    "Count of most common rating": most_common_rating_count,
    "Average number of votes": average_votes
}

# Plot the distribution of aggregate ratings
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_distribution.index, y=rating_distribution.values, palette="viridis")
plt.xlabel('Aggregate Rating')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Aggregate Ratings')
plt.show()

# Print the results
print("Most common rating:", most_common_rating)
print("Count of most common rating:", most_common_rating_count)
print("Average number of votes:", average_votes)
