# amazon_data_analysis
This project focuses on analyzing and visualizing Amazon sales data using Python. The dataset includes product information, ratings, prices, and reviews, enabling an in-depth analysis of trends and correlations.

# Features
Data preprocessing and cleaning of sales data.
Conversion of price columns into numerical formats for analysis.
Calculation and normalization of discount percentages.
Encoding of categorical variables for advanced analysis.
Creation of various plots, including scatter plots, histograms, and heatmaps.
Exploration of correlations between product attributes.
Generation of pivot tables for aggregated insights.
Technologies Used
Python: Programming language.
Pandas: For data manipulation and analysis.
Seaborn: For advanced data visualization.
Matplotlib: For plotting graphs.
Scikit-learn: For label encoding of categorical variables.


# Project Workflow
## 1. Data Cleaning
Removed currency symbols and commas from price columns (actual_price, discounted_price) and converted them to float.
Normalized discount_percentage by converting percentages to decimal values.
Converted the rating column to numerical format, replacing invalid values.
## 2. Data Visualization
Scatter Plot: Relationship between actual price and ratings.
Histogram: Distribution of product prices.
Heatmap: Correlation between various numerical attributes.
## 3. Encoding Categorical Variables
Used Label Encoding to transform non-numerical columns (e.g., category, product_id) into numerical format for further analysis.
## 4. Pivot Table
Created a pivot table to examine average ratings by category and product.

# Generated Visualizations
### Scatter Plot:
Relationship between actual_price and rating.


### Histogram:
Distribution of actual_price.


### Correlation Heatmap:
Correlation matrix showing relationships between numerical attributes.


# Usage Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/ocwerfrancis/amazon_data_analysis.git
cd amazon_data_analysis
2. Set Up the Environment
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
3. Run the Analysis
Execute the main script to generate visualizations:

bash
Copy code
python scripts/exploratory_analysis.py
Dataset
The dataset used in this project is located at: /data/amazon.csv

Columns in the dataset include:

discounted_price: Discounted price of the product.
actual_price: Original price of the product.
discount_percentage: Percentage discount offered.
rating: Customer rating of the product.
category, product_id, user_name, etc.
Future Enhancements
Implement advanced machine learning models to predict customer ratings.
Add sentiment analysis of product reviews.
Integrate interactive visualizations using Plotly or Dash.
License
This project is licensed under the MIT License. See the LICENSE file for details.
