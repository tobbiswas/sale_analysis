import pandas as pd
#Load the dataset into a Pandas DataFrame.
data = {
    "Order id": [1001, 1002, 1003, 1004, 1005, 1006],
    "Date" : pd.to_datetime(["2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07", "2024-01-10", "2024-01-12"]),
    "Product": ["T-shirt", "Jeans", "Laptop", "Phone", "Jacket", "Headphones"],
    "Category": ["Clothing", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics"],
    "Quantity": [2, 1, 1, 1, 1, 2],
    "Price": [10, 30, 500, 300, 50, 40],
    "Total Sales": [20, 30, 500, 300, 50, 80]
}
#Show basic information and statistics about the dataset.
df = pd.DataFrame(data)

print(df)
print()
print("Basic information: ")
print(df.info())
print()
#Find the total sales for each category.
Category_sale = df.groupby("Category")["Total Sales"].sum()
print("Total Sale by Category: ")
print(Category_sale)

#Identify the most sold product by quantity.
Most_sold_Product = df.loc[df["Quantity"].idxmax(), "Product"]
print()
print("Most Sold product by Quantity: ", Most_sold_Product)

#Find the total revenue generated.
print()
Total_Revenue = df["Total Sales"].sum()
print("Total Revenue: ", Total_Revenue)
print()

#Filter and display sales for the "Electronics" category.
Electronics_Sales = df[df["Category"]=="Electronics"]
print(Electronics_Sales)
print()
#Find the average price of products sold.
Average_price = df["Price"].mean()
print("Average price of product Sold: ",Average_price)


# Sort dataset by total sales in descending order
Sort_Df = df.sort_values(by= "Total Sales", ascending = True)
print(Sort_Df)