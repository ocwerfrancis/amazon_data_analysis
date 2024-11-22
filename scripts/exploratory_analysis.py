import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import LabelEncoder

# dont show warnings
warnings.filterwarnings('ignore')

# Load data
df_sales = pd.read_csv('/home/francis/Projects/amazon_data_analysis/data/amazon.csv')


# Changing the data type of discounted price and actual price

df_sales['discounted_price'] = df_sales['discounted_price'].str.replace("₹",'')
df_sales['discounted_price'] = df_sales['discounted_price'].str.replace(",",'')
df_sales['discounted_price'] = df_sales['discounted_price'].astype('float64')

df_sales['actual_price'] = df_sales['actual_price'].str.replace("₹",'')
df_sales['actual_price'] = df_sales['actual_price'].str.replace(",",'')
df_sales['actual_price'] = df_sales['actual_price'].astype('float64')

# Changing Datatype and values in Discount Percentage
df_sales['discount_percentage'] = df_sales['discount_percentage'].str.replace('%','').astype('float64')

df_sales['discount_percentage'] = df_sales['discount_percentage'] / 100

# Changing Rating Columns Data Type

df_sales['rating'] = df_sales['rating'].str.replace('|', '3.9').astype('float64')


# Changing 'rating_count' Column Data Type

df_sales['rating_count'] = df_sales['rating_count'].str.replace(',', '').astype('float64')


# df_sales.plot(kind='bar', title="Actual price against rating", color="black", figsize=(8,4))
# plt.xlabel('actual_price')
# plt.ylabel('rating')
# plt.grid(False)
# plt.savefig('bar_plot.png')

# Set the theme for the plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_sales, x='actual_price', y='rating',color = 'blue')
plt.title("Actual price against rating")
plt.xlabel("actual_price")
plt.ylabel("rating")
plt.tight_layout()
plt.savefig('Actual_price_rating.png',dpi=300)


# Plot of distribution of actual Price
plt.figure(figsize=(10, 5))
sns.histplot(data=df_sales, x='actual_price', color='blue', bins=50)
plt.title("Distribution of actual price")
plt.xlabel("Actual_price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig('actual_price_distribution.png',dpi=300)


# HEAT MAP
# label encode categorical variables

le_product_id = LabelEncoder()
le_category = LabelEncoder()
le_review_id = LabelEncoder()
le_review_content = LabelEncoder()
le_product_name = LabelEncoder()
le_user_name = LabelEncoder()
le_about_product = LabelEncoder()
le_user_id = LabelEncoder()
le_review_title = LabelEncoder()
le_img_link = LabelEncoder()
le_product_link = LabelEncoder()


df_sales['product_id'] = le_product_id.fit_transform(df_sales['product_id'])
df_sales['category'] = le_category.fit_transform(df_sales['category'])
df_sales['review_id'] = le_review_id.fit_transform(df_sales['review_id'])
df_sales['review_content'] = le_review_content.fit_transform(df_sales['review_content'])
df_sales['product_name'] = le_product_name.fit_transform(df_sales['product_name'])
df_sales['user_name'] = le_user_name.fit_transform(df_sales['user_name'])
df_sales['about_product'] = le_about_product.fit_transform(df_sales['about_product'])
df_sales['user_id'] = le_user_id.fit_transform(df_sales['user_id'])
df_sales['review_title'] = le_review_title.fit_transform(df_sales['review_title'])
df_sales['img_link'] = le_img_link.fit_transform(df_sales['img_link'])
df_sales['product_link'] = le_product_link.fit_transform(df_sales['product_link'])

# Compute the correlation matrix
correlation_matrix = df_sales.corr()

# Plot the heatmap
plt.figure(figsize=(14, 14))  # Optional: Adjust the size of the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title("Correlation Heatmap")
plt.savefig('correlation_heatmap.png',dpi=600)


# PIVOT TABELS

# Pivot table of rating by category and customer location
pivot_table = df_sales.pivot_table(values='rating', index='category', columns='product_link', aggfunc='mean')
print(pivot_table)