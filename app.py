import streamlit as st
import pandas as pd

st.set_page_config(page_title="historial ufc rax", page_icon="🥊", layout="wide")

st.title("Historical UFC Rax")
st.write("click on 'more data' for rax calculation. Displays top 30 but data exists for 2405 fighters.")

# st.write("made by @yangsl")
st.write("made by @yangsl")
st.markdown("""<br><br>""", unsafe_allow_html=True)

df = pd.read_csv("final_values.csv")

# Search bar
search_query = st.text_input("Search by fighter name:", "")

num_rows_to_display = st.selectbox("Number of rows to display:", options=[10, 20, 30, 40, 50, 100], index=2)  # Default to 30

if search_query:
    df_filtered = df[df['name'].str.contains(search_query, case=False)]
else:
    df_filtered = df.head(num_rows_to_display)  # Show only the selected number of rows

for _, row in df_filtered.iterrows():
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown(f"## {row['name']}")
    
    with col2:
        st.markdown(f"<h2 style='color: #90ee90;'>{row['Value']}</h2>", unsafe_allow_html=True)
    
    with st.expander("More Data"):
        data_for_chart = row.drop(labels=['name', 'Value'])
        
        chart_data = pd.DataFrame(data_for_chart)
        chart_data = chart_data.rename(columns={row.name: 'Value'}).reset_index()

        chart_data.columns = ['Category', 'Value']
        
        st.bar_chart(chart_data.set_index('Category'))