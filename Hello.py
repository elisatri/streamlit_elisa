import streamlit as st
import pandas as pd

# Load CSV data
data = pd.read_csv("tips.csv")

# User input for column selection (assuming "total_bill" and "tip")
selected_column = st.selectbox("Select Column for Distribution", data.columns)

# Create a distribution chart (assuming "tip" column represents rating)
st.subheader("Distribusi Rating dalam 5 Tahun Terakhir (Assuming 'tip' column)")
if 'datetime' in data.columns:
    data['year'] = pd.to_datetime(data['datetime']).dt.year
    filtered_data = data[data['year'] >= 2018]  # Filter for last 5 years (assuming 2023)
    st.bar_chart(filtered_data[selected_column])  # Assuming 'tip' represents rating
else:
    st.write("Data does not contain a 'datetime' column for year extraction.")

# Streamlit deprecation warning handling
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == "__main__":
    run()
