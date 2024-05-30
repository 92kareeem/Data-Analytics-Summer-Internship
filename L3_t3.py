import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Convert 'Has Table booking' and 'Has Online delivery' to binary values
data['Has Table booking'] = data['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Has Online delivery'] = data['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Analyze the relationship between price range and the availability of online delivery and table booking
price_range_table_booking = data.groupby('Price range')['Has Table booking'].mean()
price_range_online_delivery = data.groupby('Price range')['Has Online delivery'].mean()

# Prepare the results
price_range_analysis_results = {
    "Table Booking Availability by Price Range": price_range_table_booking,
    "Online Delivery Availability by Price Range": price_range_online_delivery
}

# Print the results
print("Table Booking Availability by Price Range:")
print(price_range_table_booking)

print("\nOnline Delivery Availability by Price Range:")
print(price_range_online_delivery)

# Visualization
plt.figure(figsize=(14, 7))

# Table Booking Availability by Price Range
plt.subplot(1, 2, 1)
price_range_table_booking.plot(kind='bar', color='skyblue')
plt.title('Table Booking Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion of Restaurants with Table Booking')
plt.xticks(rotation=0)

# Online Delivery Availability by Price Range
plt.subplot(1, 2, 2)
price_range_online_delivery.plot(kind='bar', color='lightgreen')
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion of Restaurants with Online Delivery')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
