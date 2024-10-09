#!/usr/bin/env python
# coding: utf-8

# In[107]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[108]:


df = pd.read_csv('cleaned.csv')


# In[109]:


df


# In[110]:


df.describe()


# In[111]:


df.dtypes


# In[112]:


#df['timestamp'] = pd.to_datetime(df['timestamp'])


# In[113]:


df


# In[114]:


df


# In[97]:


df.isnull().sum()


# In[66]:


df['amount'].describe()


# In[67]:


df['gender'].value_counts()


# In[68]:


df['category'].value_counts()


# In[69]:


df['brand'].value_counts()


# # Average rating by category

# In[70]:


avg_rating_category = df.groupby('category')['rating'].mean()
print(avg_rating_category)


# In[71]:


plt.figure(figsize=(10, 6))
avg_rating_category.plot(kind='bar')
plt.title('Average Rating per Category')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()


# # Counts of Rating Distribution

# In[72]:


sns.histplot(df['rating'])
plt.title('Rating Distribution')
plt.show()


# # Top brands by sales
# 

# In[73]:


top_brands = df.groupby('brand')['amount'].sum().sort_values(ascending=False).head(10)
print(top_brands)


# In[74]:


plt.figure(figsize=(10, 6))
top_brands.plot(kind='bar', color='skyblue')

plt.title('Top 10 Brands by Sales', fontsize=20)
plt.xlabel('Brand', fontsize=20)
plt.ylabel('Total Sales (Amount)', fontsize=20)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[131]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by category and calculate total sales (amount)
category_sales = df.groupby('category')['amount'].sum().sort_values(ascending=False)

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='Set2')

# Add titles and labels
plt.title('Total Sales Amount by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)

# Format the y-axis to show large numbers with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()


# In[132]:


print("Original DataFrame Year Values:")
print(df['year'].value_counts())

# Filter the data for the years 2015 to 2018
data_filtered = df[(df['year'] >= 2015) & (df['year'] <= 2018)]

# Check the filtered DataFrame
print("\nFiltered DataFrame (2015-2018):")
print(data_filtered)

# Check if data_filtered is empty
if data_filtered.empty:
    print("No data available for the years 2015 to 2018.")
else:
    # Group by year and calculate total sales (amount) for each year
    sales_yearly = data_filtered.groupby('year')['amount'].sum().reset_index()

    # Visualization: Bar plot of sales by year
    plt.figure(figsize=(10, 6))
    sns.barplot(x='year', y='amount', data=sales_yearly, palette='Blues_d')

    # Add titles and labels
    plt.title('Total Sales by Year (2015 - 2018)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Sales (Amount)', fontsize=12)

    # Display the plot
    plt.tight_layout()
    plt.show()


# # Category percentage sales
# 

# In[78]:


df.groupby('category')['amount'].sum().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 category salespercentage')


# # Brand wise sales percentage
# 

# In[79]:


# Group sales by brand and calculate percentage of total sales for each brand
brand_sales = df.groupby('brand')['amount'].sum()

# Calculate the percentage of total sales for each brand
brand_percentage = brand_sales / brand_sales.sum() * 100

# Convert the Series to a DataFrame for better visualization
brand_percentage_df = brand_percentage.reset_index()
brand_percentage_df.columns = ['Brand', 'Percentage']

# Visualize using a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Percentage', y='Brand', data=brand_percentage_df, palette='coolwarm')

# Add titles and labels
plt.title('Brand Wise Sales Percentage', fontsize=30)
plt.xlabel('Percentage of Total Sales (%)', fontsize=19)
plt.ylabel('Brand', fontsize=20)

# Rotate the brand names
plt.yticks(rotation=15)

# Display the plot
plt.tight_layout()
plt.show()


# # Visualize Category Percentage Sales

# In[80]:


category_sales = df.groupby('category')['amount'].sum()

# Calculate the percentage of total sales for each category
category_percentage = category_sales / category_sales.sum() * 100

# Convert the Series to a DataFrame for better visualization
category_percentage_df = category_percentage.reset_index()
category_percentage_df.columns = ['Category', 'Percentage']

# Visualize using a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Percentage', y='Category', data=category_percentage_df, palette='viridis')

# Add titles and labels
plt.title('Category Percentage Sales', fontsize=16)
plt.xlabel('Percentage of Total Sales (%)', fontsize=12)
plt.ylabel('Category', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()


# In[87]:


df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce')  # Convert the timestamp to datetime
df['year'] = df['timestamp'].dt.year  # Extract the year again


# In[122]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


# Group by year and calculate total sales
year_sales = df_filtered.groupby('year')['amount'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='year', y='amount', data=year_sales, palette='Blues_d')

 
plt.title('Sales by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales (Amount)', fontsize=12)

ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()


# In[123]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by gender and calculate total sales (amount)
gender_sales = df.groupby('gender')['amount'].sum().reset_index()

# Create a bar plot for sales by gender
plt.figure(figsize=(8, 6))
sns.barplot(x='gender', y='amount', data=gender_sales, palette='Set2')

# Add titles and labels
plt.title('Sales by Gender', fontsize=16)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Total Sales (Amount)', fontsize=12)

# Format the y-axis to show large numbers with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Display the plot
plt.tight_layout()
plt.show()


# In[125]:


# Group by gender and calculate total sales (amount)
gender_sales = df.groupby('gender')['amount'].sum().reset_index()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(gender_sales['amount'], labels=gender_sales['gender'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))

plt.title('Sales Distribution by Gender', fontsize=16)

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.show()


# In[126]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by category and gender, calculating total sales (amount)
category_gender_sales = df.groupby(['category', 'gender'])['amount'].sum().unstack().reset_index()

# Create a bar plot
plt.figure(figsize=(12, 6))
category_gender_sales.plot(kind='bar', x='category', stacked=False, color=sns.color_palette('Set2'))

# Add titles and labels
plt.title('Sales by Category and Gender', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales (Amount)', fontsize=12)

# Format the y-axis to show large numbers with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()


# In[127]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by brand and year, calculating total sales (amount)
brand_year_sales = df.groupby(['brand', 'year'])['amount'].sum().unstack().fillna(0)

# Create a bar plot
plt.figure(figsize=(14, 8))
brand_year_sales.plot(kind='bar', stacked=False, color=sns.color_palette('Set2'))

# Add titles and labels
plt.title('Sales by Brand and Year', fontsize=16)
plt.xlabel('Brand', fontsize=12)
plt.ylabel('Total Sales (Amount)', fontsize=12)

# Format the y-axis to show large numbers with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()


# In[130]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group by category and calculate total sales (amount)
category_sales = df.groupby('category')['amount'].sum().sort_values(ascending=False)

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='Set2')

# Add titles and labels
plt.title('Total Sales Amount by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)

# Format the y-axis to show large numbers with commas
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




