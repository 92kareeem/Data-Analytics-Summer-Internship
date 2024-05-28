import pandas as pd
import matplotlib.pyplot as plt

# load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Plotting the distribution of price ranges
plt.figure(figsize=(10, 6))
data['Price range'].value_counts().plot(kind='bar')
plt.title('Distribution of Price Ranges among Restaurants')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.show()

# Calculating the percentage of restaurants in each price range category
price_range_percent = data['Price range'].value_counts(normalize=True) * 100
print(price_range_percent)
