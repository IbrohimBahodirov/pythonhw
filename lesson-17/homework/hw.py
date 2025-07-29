import pandas as pd
import numpy as np

# ========== HOMEWORK 1 ==========

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1.
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2.
print("=== First 3 Rows ===")
print(df.head(3))

# 3
mean_age = df['age'].mean()
print("\n=== Mean Age ===")
print(mean_age)

# 4.
print("\n=== Name and City ===")
print(df[['first_name', 'City']])

# 5.
np.random.seed(0) 
df['Salary'] = np.random.randint(3000, 8000, size=len(df))

# 6
print("\n=== Summary Statistics ===")
print(df.describe(include='all'))


# ========== HOMEWORK 2 ==========
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(sales_data)

print("\n=== Max Sales and Expenses ===")
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

print("\n=== Min Sales and Expenses ===")
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

print("\n=== Average Sales and Expenses ===")
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


# ========== HOMEWORK 3 ==========
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(expenses_data)

expenses = expenses.set_index('Category')

print("\n=== Max Expense per Category ===")
print(expenses.max(axis=1))

print("\n=== Min Expense per Category ===")
print(expenses.min(axis=1))

print("\n=== Average Expense per Category ===")
print(expenses.mean(axis=1))
