import pandas as pd

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Identify restaurant chains by checking for repeated restaurant names
restaurant_chain_counts = data['Restaurant Name'].value_counts()
restaurant_chains = restaurant_chain_counts[restaurant_chain_counts > 1]

# Filter the dataset to include only restaurant chains
chain_data = data[data['Restaurant Name'].isin(restaurant_chains.index)]

# Analyze the ratings and popularity (votes) of different restaurant chains
chain_ratings = chain_data.groupby('Restaurant Name')['Aggregate rating'].mean()
chain_votes = chain_data.groupby('Restaurant Name')['Votes'].sum()

# Combine the results into a single DataFrame for easier analysis
chain_analysis = pd.DataFrame({
    'Average Rating': chain_ratings,
    'Total Votes': chain_votes
}).sort_values(by='Total Votes', ascending=False)

# Prepare the results
restaurant_chain_results = {
    "Restaurant Chains": restaurant_chains,
    "Chain Analysis": chain_analysis
}

# Print the results
print("Restaurant Chains:")
print(restaurant_chains)
print("\nChain Analysis:")
print(chain_analysis)
