# IMPORT LIBRARIES

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# LOAD & CLEAN DATA

df = pd.read_csv("global_ecom.csv")
df.drop(["Customer_ID","Unused_Internal_Code"], axis=1, inplace=True)
df.drop_duplicates(inplace=True)


# MISSING VALUE HANDLE

df["Country"] = df["Country"].fillna("Unknown")
df["Product_Category"] = df["Product_Category"].fillna("Others")
df["Order_Status"] = df["Order_Status"].fillna("Not Available")

df["Sales_Amount"] = df["Sales_Amount"].fillna(df["Sales_Amount"].mean())


# DATE FORMATING

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.sort_values(by='Order_Date')
df = df.reset_index(drop=True)


# SALES DISTRIBUTION

# plt.figure(figsize=(10,8))
# sns.countplot(data=df, x="Country", palette="bright6")
# plt.title("Distribution of Sales by Countries")
# plt.xlabel("")
# plt.ylabel("Number of Sales")
# plt.tight_layout()
# plt.show()


# MOST SELLING PRODUCT CATEGORY

# products_data = df["Product_Category"].value_counts()
# print(products_data)
# plt.pie(products_data, labels= products_data.index, autopct="%1.1f%%", colors=sns.color_palette("dark6"))
# plt.title("Sales Percentage by Product Category")
# plt.tight_layout()
# plt.show()


# MOST SELLING PRODUCT BY COUNTRIES

# fig, axes = plt.subplots(2,3, figsize= (10,8))
# fig.suptitle("Most Selling Product Category by Each Country", fontsize=18)

# sns.countplot(data=df[df["Country"]=="USA"], x="Product_Category", ax= axes[0,0], palette="bright")
# axes[0,0].set_title("Sales in USA")
# axes[0,0].set_xlabel("")
# axes[0,0].set_ylabel("")
# axes[0,0].tick_params(axis="x", rotation=30)

# sns.countplot(data=df[df["Country"]== "UK"], x="Product_Category", ax= axes[0,1], palette="bright")
# axes[0,1].set_title("Sales in UK")
# axes[0,1].set_xlabel("")
# axes[0,1].set_ylabel("")
# axes[0,1].tick_params(axis="x", rotation=30)

# sns.countplot(data=df[df["Country"]=="Canada"], x="Product_Category", ax= axes[0,2], palette="bright")
# axes[0,2].set_title("Sales in Canada")
# axes[0,2].set_xlabel("")
# axes[0,2].set_ylabel("")
# axes[0,2].tick_params(axis="x", rotation=30)

# sns.countplot(data=df[df["Country"]=="Germany"], x="Product_Category", ax= axes[1,0], palette="bright")
# axes[1,0].set_title("Sales in Germany")
# axes[1,0].set_xlabel("")
# axes[1,0].set_ylabel("")
# axes[1,0].tick_params(axis="x", rotation=30)

# sns.countplot(data=df[df["Country"]=="France"], x="Product_Category", ax= axes[1,1], palette="bright")
# axes[1,1].set_title("Sales in France")
# axes[1,1].set_xlabel("")
# axes[1,1].set_ylabel("")
# axes[1,1].tick_params(axis="x", rotation=30)

# sns.countplot(data=df[df["Country"]=="Unknown"], x="Product_Category", ax= axes[1,2], palette="bright")
# axes[1,2].set_title("Sales in Unknown Country")
# axes[1,2].set_xlabel("")
# axes[1,2].set_ylabel("")
# axes[1,2].tick_params(axis="x", rotation=30)

# plt.tight_layout()
# plt.show()


# PERCENTAGE OF ACTUAL PROFIT CONTRIBUTION BY CATEGORY

df["Profit_Amount"] = df["Sales_Amount"] * df["Profit_Margin"]

total_profit_by_cat = df.groupby("Product_Category")["Profit_Amount"].sum()

# plt.figure(figsize=(10,8))
# plt.pie(total_profit_by_cat, labels=total_profit_by_cat.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("bright"), explode=[0.05]*len(total_profit_by_cat))
# plt.title("Percentage of Actual Profit Contribution by Category")
# plt.show()


# Order Status

# plt.figure(figsize=(10,8))
# sns.countplot(data=df, x="Product_Category", hue="Order_Status", palette="dark")
# plt.title("Order Status Distribution by Product Category")
# plt.xlabel("")
# plt.ylabel("Number of Orders")
# plt.tight_layout()
# plt.show()


# AVERAGE SHIPPING COST BY COUNTRIES

country_shipping = df.groupby("Country")["Shipping_Cost"].mean().sort_values(ascending=False)

# plt.figure(figsize=(10,8))
# sns.barplot(x=country_shipping.index, y=country_shipping.values, palette="Reds_r")
# plt.title("Average Shipping Cost by Countries")
# plt.xlabel("")
# plt.ylabel("Average Cost")
# plt.tight_layout()
# plt.show()


# IMPACT OF SHIPPING COST ON PROFIT

df["Gross_Profit"] = df["Sales_Amount"] * df["Profit_Margin"]
df["Net_Profit"] = df["Gross_Profit"] - df["Shipping_Cost"]

country_impact = df.groupby("Country")[["Gross_Profit","Net_Profit"]].sum().reset_index()

# plt.figure(figsize=(10,8))
# sns.barplot(data=country_impact, x="Country", y="Net_Profit", palette="plasma")
# plt.title("Impact of Shipping Cost on Profit")
# plt.xlabel("")
# plt.ylabel("Net Profit")
# plt.tight_layout()
# plt.show()