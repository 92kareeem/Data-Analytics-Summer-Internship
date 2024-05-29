import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Plot the locations of restaurants on a map
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=data, hue='City', palette='viridis', legend=None)
plt.title('Geographic Distribution of Restaurants')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Identify any patterns or clusters of restaurants in specific areas
# Using seaborn's kdeplot to show density
plt.figure(figsize=(12, 8))
sns.kdeplot(x=data['Longitude'], y=data['Latitude'], shade=True, cmap='viridis', bw_adjust=0.5)
plt.title('Density Plot of Restaurant Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
