import pandas as pd
import matplotlib.pyplot as plt
#load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Determine the percentage of restaurants that offer online delivery
online_delivery_count = data['Has Online delivery'].value_counts()
online_delivery_percentage = (online_delivery_count / data.shape[0]) * 100

# Compare the average ratings of restaurants with and without online delivery
average_rating_with_delivery = data[data['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_delivery = data[data['Has Online delivery'] == 'No']['Aggregate rating'].mean()

print(f"Percentage of restaurants offering online delivery: {online_delivery_percentage}")
print(f"Average rating of restaurants with online delivery: {average_rating_with_delivery:.2f}")
print(f"Average rating of restaurants without online delivery: {average_rating_without_delivery:.2f}")

# Visualization code
labels = ['With Online Delivery', 'Without Online Delivery']
ratings = [average_rating_with_delivery, average_rating_without_delivery]

plt.figure(figsize=(10, 6))
plt.bar(labels, ratings, color=['blue', 'orange'])
plt.xlabel('Online Delivery Option')
plt.ylabel('Average Rating')
plt.title('Average Ratings With vs Without Online Delivery')
plt.ylim(0, 5)  # Adjust the limit according to your rating scale
plt.show()