import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("data.csv")

# User input for selecting columns (optional)
selected_columns = st.multiselect("Select Columns for Visualization", data.columns)

# Display the data as a table (optional)
st.header("Data")
st.write(data.head(10))

# Create charts
st.subheader("Data Visualization")
if selected_columns:
    for col in selected_columns:
        st.bar_chart(data[col])  # Replace with appropriate chart type
else:
    st.write("Select columns to visualize.")

# Streamlit deprecation warning handling
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == "__main__":
    pass  # Keep this line to avoid errors when running the script directly
