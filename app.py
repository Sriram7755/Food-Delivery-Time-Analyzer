import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🚚 Food Delivery Time Analyzer")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("delivery_data.csv")

df = load_data()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df.head(100))

# Box Plot
st.subheader("📦 Delivery Time by Location")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.boxplot(x='location', y='delivery_time', data=df, palette='Set2', ax=ax1)
ax1.set_title('Delivery Time by Location')
ax1.set_xlabel('Location')
ax1.set_ylabel('Delivery Time (minutes)')
st.pyplot(fig1)

# Heatmap
st.subheader("🔥 Delay Heatmap by Hour and Region")
df['order_hour'] = df['order_hour'].astype(str)
pivot_table = df.pivot_table(index='order_hour', columns='region', values='delay', aggfunc='mean')

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='YlOrRd', ax=ax2)
ax2.set_title('Average Delay by Hour and Region')
st.pyplot(fig2)

# Line Plot
st.subheader("📈 Average Delivery Duration by Hour")
avg_delivery_by_hour = df.groupby('order_hour')['delivery_time'].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=avg_delivery_by_hour, x='order_hour', y='delivery_time', marker='o', ax=ax3)
ax3.set_title('Average Delivery Duration by Hour')
ax3.set_xlabel('Hour of the Day')
ax3.set_ylabel('Avg Delivery Time (minutes)')
ax3.grid(True)
st.pyplot(fig3)
