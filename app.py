import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Mall Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Mall Customer Segmentation")
st.write("Customer Segmentation using K-Means Clustering")

st.markdown("---")

# -----------------------------
# Load Dataset
# -----------------------------
try:
    df = pd.read_csv("customerdataset2.csv")
except:
    st.error("Dataset not found! Please keep customerdataset2.csv in the project folder.")
    st.stop()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.write("Shape :", df.shape)

# -----------------------------
# Feature Selection
# -----------------------------
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# -----------------------------
# Scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Settings")

k = st.sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,
    value=5
)

# -----------------------------
# Train Model
# -----------------------------
kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

# -----------------------------
# Cluster Plot
# -----------------------------
st.subheader("Customer Segmentation")

fig, ax = plt.subplots(figsize=(8,6))

scatter = ax.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    c=df["Cluster"],
    cmap="viridis",
    s=70
)

centers = scaler.inverse_transform(kmeans.cluster_centers_)

ax.scatter(
    centers[:,0],
    centers[:,1],
    c="red",
    s=300,
    marker="X",
    label="Centroids"
)

ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Mall Customer Segmentation")
ax.legend()

st.pyplot(fig)

# -----------------------------
# Cluster Summary
# -----------------------------
st.subheader("Cluster Summary")

summary = df.groupby("Cluster")[
    ["Annual Income (k$)",
     "Spending Score (1-100)",
     "Age"]
].mean()

st.dataframe(summary)

# -----------------------------
# Download CSV
# -----------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Clustered Dataset",
    csv,
    "clustered_customers.csv",
    "text/csv"
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.success("Project Developed by Atharv Vairal ❤️")
