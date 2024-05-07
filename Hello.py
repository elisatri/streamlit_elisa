# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome! 👋")


if __name__ == "__main__":
    run()

import streamlit as st
import pandas as pd

# Load CSV data
data = pd.read_csv("tips.csv")

# Display the data as a table
st.title("Data Visualization")
st.write(data)

# Create a chart from the data
selected_column = "total_bill"  # Replace with your desired column name
if selected_column in data.columns:
    st.bar_chart(data[selected_column])
else:
    st.write("Error: Column '{}' not found in the data.".format(selected_column))

# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome! 👋")


if __name__ == "__main__":
    run()

import streamlit as st
import pandas as pd

# Load CSV data
data = pd.read_csv("tips.csv")

# Display the data as a table
st.title("Data Visualization")
st.write(data)

# Create a chart from the data
selected_column = "total_bill"  # Replace with your desired column name
if selected_column in data.columns:
    st.bar_chart(data[selected_column])
else:
    st.write("Error: Column '{}' not found in the data.".format(selected_column))

 # Distribution plot (histogram)
    st.subheader("Distribution of " + column_name)
    st.write("This histogram shows the frequency distribution of values in the selected column.")
    st.histogram(data[column_name])

# Call the function to create charts based on user selection (or default)
create_charts(selected_column if selected_column else "total_bill")


