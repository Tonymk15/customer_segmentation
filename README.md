CUSTOMER SEGMENTATION USING K-MEANS CLUSTERING
PROJECT OVERVIEW
-This project uses K-Means Clustering, an unsupervised machine learning algorithm to segment customers into different groups based on their demographic characteristics and also their spending behavior.
-The project also includes an interactive Streamlit web application that allows the users to enter customer information and receive a predicted customer segment.

PROJECT OBJECTIVES

1 Identify distinct customer segments based on their characteristics and spending behavior.
2 Apply K-Means clustering to group customers with similar patterns.
3 Visualize the identified customer segments.
4 Develop an interactive application for customer segmentation.
5 Provide insights that can help businesses understand their customers and develop targeted marketing strategies.

DATASET
-The project uses the Mall Customers dataset, which contains information about customers, including:
1 Customer ID
2 Gender
3 Age
4 Annual Income
5 Spending Score
-The clustering analysis primarily uses Age, Annual Income and Spending Score to identify customer segments.

TECHNOLOGIES USED

1 Python – Programming language
2 Pandas – Data manipulation and analysis
3 Scikit-learn – Machine learning and K-Means clustering
4 Plotly – Interactive data visualization
5 Streamlit – Web application development
6 Joblib – Saving and loading machine learning models
7 Jupyter Notebook / Google Colab – Model development and analysis

MACHINE LEARNING APPROACH
1. Data Preparation- The dataset was loaded and examined to understand its structure and identify the variables relevant to customer segmentation.
2. Feature Selection- Relevant customer characteristics were selected for clustering, including:

- Age
- Annual Income
- Spending Score
3. Feature Scaling- The selected features were scaled before applying K-Means clustering to ensure that differences in the numerical ranges of the variables did not disproportionately affect the clustering results.
4. K-Means Clustering- K-Means clustering was applied to divide customers into groups with similar characteristics.
  The appropriate number of clusters was determined using clustering evaluation techniques such as the **Elbow Method**.
5. Visualization- The resulting customer segments were visualized using interactive Plotly charts to make the differences between the clusters easier to understand.
6. Prediction Application- The trained clustering model and scaler were saved using Joblib and integrated into a Streamlit application.
  Users can enter customer information and receive the corresponding predicted customer segment.

CUSTOMER SEGMENTS

The clustering analysis identifies groups of customers with different combinations of age, income, and spending behavior.
These segments can help businesses understand differences in customer behavior and potentially support:
- Targeted marketing
- Customer profiling
- Personalized promotions
- Customer relationship strategies
- Business decision-making

AUTHOR

Tony Murigi Kiarie
