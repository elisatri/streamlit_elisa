import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Import for scatter plot

# Load CSV data
data = pd.read_csv("tips.csv")

# Display the data as a table (assuming "tips.csv" has relevant columns)
st.title("Data Visualization")
st.write(data)

# User input for column selection (assuming "total_bill" and "tip")
selected_x_column = st.selectbox("Select X-axis Column", data.columns)
selected_y_column = st.selectbox("Select Y-axis Column", data.columns)

# Create a scatter plot using Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))  # Set figure size for better visualization
ax.scatter(data[selected_x_column], data[selected_y_column])

# Customize scatter plot (optional)
ax.set_xlabel(selected_x_column)
ax.set_ylabel(selected_y_column)
ax.set_title(f"Scatter Plot of {selected_x_column} vs. {selected_y_column}")

# Display the scatter plot using Streamlit
st.subheader("Scatter Plot")
st.pyplot(fig)

# Additional subheader and chart based on ratings' feedback
st.subheader("Distribusi Rating dalam 5 Tahun Terakhir (Assuming 'tip' column)")
# Assuming data has a 'datetime' column for year extraction
if 'datetime' in data.columns:
    data['year'] = pd.to_datetime(data['datetime']).dt.year
    filtered_data = data[data['year'] >= 2018]  # Filter for last 5 years (assuming 2023)
    st.bar_chart(filtered_data['tip'])  # Assuming 'tip' represents rating
else:
    st.write("Data does not contain a 'datetime' column for year extraction.")

# Streamlit deprecation warning handling
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == "__main__":
    run()
