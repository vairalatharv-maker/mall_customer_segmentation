# Mall Customer Segmentation using K-Means Clustering

## Project Overview

This project performs customer segmentation using the K-Means Clustering algorithm. The goal is to group customers based on their Annual Income and Spending Score, helping businesses understand customer behavior and create targeted marketing strategies.

---

## Objectives

- Analyze customer data
- Perform Exploratory Data Analysis (EDA)
- Apply Feature Scaling
- Find the optimal number of clusters using the Elbow Method
- Segment customers using K-Means Clustering
- Visualize customer groups
- Generate business insights

---

## Dataset

The dataset contains the following features:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Machine Learning Algorithm

- K-Means Clustering

---

## Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Understanding
4. Data Cleaning
5. Exploratory Data Analysis (EDA)
6. Feature Selection
7. Feature Scaling
8. Elbow Method
9. Train K-Means Model
10. Customer Segmentation
11. Cluster Visualization
12. Model Evaluation using Silhouette Score
13. Business Insights
14. Save Clustered Dataset

---

## Results

- Successfully segmented customers into 5 clusters.
- Used Elbow Method to determine the optimal number of clusters.
- Evaluated clustering quality using the Silhouette Score.
- Visualized customer segments using scatter plots.

---

## Business Insights

- Premium Customers (High Income, High Spending)
- Budget Customers (Low Income, Low Spending)
- Average Customers
- High Income but Low Spending Customers (Marketing Opportunity)
- Regular Customers

---

## Project Structure

```
Mall-Customer-Segmentation/
│
├── data/
├── notebook/
├── outputs/
├── images/
├── README.md
├── requirements.txt
└── app.py
```

---

## How to Run

1. Clone the repository

```bash
git clone <repository_link>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook

```bash
jupyter notebook
```

---

## Future Improvements

- Interactive Streamlit Web Application
- Deploy on Streamlit Community Cloud
- Add interactive charts using Plotly
- Predict cluster for new customers

---

## Author

**Atharv Vairal**

BE Information Technology

Aspiring Data Scientist
