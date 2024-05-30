import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Dataset .csv'
data = pd.read_csv(file_path)

# Assuming the dataset has a 'Reviews' column for the text reviews
# For demonstration, I'll create a dummy 'Reviews' column with random text
# Remove this part if your dataset already includes reviews
import random
random.seed(42)
dummy_reviews = [
    "Great food and excellent service", 
    "Terrible experience, the food was bad",
    "Had a wonderful time, loved the ambiance",
    "Food was okay but the service was slow",
    "Absolutely loved the desserts, will visit again",
    "Would not recommend, very disappointing",
]
data['Reviews'] = [random.choice(dummy_reviews) for _ in range(len(data))]

# Analyze the text reviews to identify the most common positive and negative keywords
positive_keywords = ["great", "excellent", "wonderful", "loved", "amazing", "best"]
negative_keywords = ["terrible", "bad", "slow", "disappointing", "would not recommend"]

positive_counts = Counter()
negative_counts = Counter()

for review in data['Reviews']:
    words = review.lower().split()
    for word in words:
        if word in positive_keywords:
            positive_counts[word] += 1
        if word in negative_keywords:
            negative_counts[word] += 1

# Calculate the average length of reviews
data['Review Length'] = data['Reviews'].apply(len)
average_review_length = data['Review Length'].mean()

# Explore if there is a relationship between review length and rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Review Length', y='Aggregate rating', data=data, alpha=0.5)
plt.title('Relationship between Review Length and Rating')
plt.xlabel('Review Length')
plt.ylabel('Aggregate Rating')
plt.show()

# Prepare the results
review_analysis_results = {
    "Most common positive keywords": positive_counts,
    "Most common negative keywords": negative_counts,
    "Average review length": average_review_length
}

print("Most Common Positive Keywords:", positive_counts)
print("Most Common Negative Keywords:", negative_counts)
print("Average Review Length:", average_review_length)
