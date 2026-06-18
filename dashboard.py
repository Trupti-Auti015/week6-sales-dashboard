import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv(r"C:\Terraform\TRUPTI\The  developer arena\week6-sales-dashboard\sales_data.csv")

total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sale:", highest_sale)



# Load Data
df = pd.read_csv(
    r"C:\Terraform\TRUPTI\The  developer arena\week6-sales-dashboard\sales_data.csv"
)

# Product Sales
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

# Correlation
corr = df[["Quantity", "Price", "Total_Sales"]].corr()


# Box Plot

sns.barplot(data=product_sales,
            x="Product",
            y="Total_Sales")

plt.title("Box plot")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("visualizations/bar_chart.png")
plt.show()

# Violin Plot

sns.violinplot(y=df["Total_Sales"])
plt.title("Violin Plot of Total Sales")
plt.ylabel("Total Sales")
plt.savefig("visualizations/violin_plot.png")
plt.show()

# Heatmap
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/heatmap.png")
plt.show()

# Interactive Plotly Chart

product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()
 
fig = px.bar(
    product_sales,
    x="Product",
    y="Total_Sales",
    color="Product",
    title="Interactive Sales Dashboard"
)

fig.show()


