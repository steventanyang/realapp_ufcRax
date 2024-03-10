import streamlit as st
import pandas as pd

st.set_page_config(page_title="historial ufc rax", page_icon="🥊", layout="wide")

st.title("Historical UFC Rax")
st.write("click on 'more data' for rax calculation")

# st.write("made by @yangsl")
st.write("made by @yangsl")
st.markdown("""<br><br>""", unsafe_allow_html=True)

df = pd.read_csv("final_values.csv")

# Loop through each row in your DataFrame
for _, row in df.iterrows():
    # Create two columns: one for the name, and one for the value
    col1, col2 = st.columns([2,4])  # Adjust the ratio as needed

    with col1:
        # Display fighter's name
        st.markdown(f"## {row['name']}")
    
    with col2:
        # Display fighter's value in bigger, green text using HTML in markdown
        st.markdown(f"<h2 style='color: #90ee90;'>{row['Value']}</h2>", unsafe_allow_html=True)
    
    # Create an expander for more data
    with st.expander("More Data"):
        # Prepare the data for the bar chart, excluding 'name' and 'Value' columns
        data_for_chart = row.drop(labels=['name', 'Value'])
        
        # Convert the Series to a DataFrame and use its index as a column, necessary for bar_chart
        chart_data = pd.DataFrame(data_for_chart)
        chart_data = chart_data.rename(columns={row.name: 'Value'}).reset_index()
        # Rename columns for clarity in the chart
        chart_data.columns = ['Category', 'Value']
        
        # Display the bar chart
        st.bar_chart(chart_data.set_index('Category'))
