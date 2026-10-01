import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load the trained model and scaler
model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title of the app
st.title("Customer Segmentation Using K-Means Clustering")

st.write("""
This application segments mall customers based on:
- Age
- Annual Income (k$)
- Spending Score (1–100)

The goal is to help businesses understand different customer groups
and create targeted marketing strategies.

Upload a CSV file to predict customer segments and receive marketing recommendations.
""")

st.sidebar.header("Manual Customer Prediction")

age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25)

income = st.sidebar.number_input(
    "Annual Income (k$)",
    min_value=0,
    max_value=200,
    value=50
)

spending = st.sidebar.number_input(
    "Spending Score (1-100)",
    min_value=1,
    max_value=100,
    value=50
)

if st.sidebar.button("Predict Cluster"):

    customer = [[age, income, spending]]

    customer_scaled = scaler.transform(customer)

    cluster = model.predict(customer_scaled)[0]

    recommendation = {
        0: "Offer premium products and exclusive discounts.",
        1: "Provide loyalty rewards and personalized offers.",
        2: "Promote budget-friendly products and special deals.",
        3: "Encourage higher spending with bundled offers.",
        4: "Target with new arrivals and seasonal promotions."
    }

    st.sidebar.success(f"Predicted Cluster: {cluster}")
    st.sidebar.write("Recommendation:")
    st.sidebar.info(recommendation[cluster])

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    try:
        # Read the uploaded CSV
        data = pd.read_csv(uploaded_file)

        # Display uploaded dataset
        st.subheader("Uploaded Dataset")
        st.dataframe(data)

        # Select features used for clustering
        features = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

        # Scale the features
        scaled_features = scaler.transform(features)

        # Predict customer clusters
        clusters = model.predict(scaled_features)

        # Add cluster labels
        data["Cluster"] = clusters

        # Marketing recommendations
        recommendations = {
            0: "Offer premium products and exclusive discounts.",
            1: "Provide loyalty rewards and personalized offers.",
            2: "Promote budget-friendly products and special deals.",
            3: "Encourage higher spending with bundled offers.",
            4: "Target with new arrivals and seasonal promotions."
        }

        # Add recommendation column
        data["Recommendation"] = data["Cluster"].map(recommendations)

        # Display segmented customers
        st.subheader("Segmented Customers")
        st.dataframe(data)

        # Interactive scatter plot
        st.subheader("Customer Segmentation Visualization")

        fig = px.scatter(
            data,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            color="Cluster",
            hover_data=["Age"],
            title="Customer Segments"
        )

        st.plotly_chart(fig, use_container_width=True)
        # Convert DataFrame to CSV
        csv = data.to_csv(index=False).encode("utf-8")
        # Download button
        st.download_button(
            label="Download Segmented Data",
            data=csv,
            file_name="segmented_customers.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error("Please upload a valid CSV file.")