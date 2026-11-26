import pandas as pd
import numpy as np

raz = pd.read_csv("raz.csv") #products
dva = pd.read_csv("dva.csv") #orders
tri = pd.read_csv("tri.csv") #users

result = pd.merge(dva, raz, on='product_id', how="left")
result["product_name"] = result["product_name"].fillna("Unknown Product")
result["price"] = result["price"].fillna(0)
result['total_price'] = result['quantity'] * result['price']
user_stats = result.groupby("user_id").agg({
    "total_price"  : "sum",
    "quantity" : "sum",
    "order_id" : "count"
}).reset_index()
user_stats = user_stats.rename(columns={
    "total_price": "total_spent",
     "quantity": "total_items",
      "order_id": "order_count"
    })
merged = pd.merge(tri, user_stats, how="left")
merged[["total_spent", "total_items", "order_count"]] = merged[["total_spent", "total_items", "order_count"]].fillna(0)
print(result)
category = result.groupby("category")["total_price"].sum().sort_values(ascending=False)
convert = result[["total_price", "quantity", "price"]]
x = convert.to_numpy()
print(x.shape)

