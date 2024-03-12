import streamlit as st
import pandas as pd

st.set_page_config(page_title="Historical UFC Rax", page_icon="🥊", layout="wide", initial_sidebar_state="collapsed")

st.title("Historical UFC Rax")
st.write("Click on 'more data' for RAX calculation. Displays top 30 but data exists for 2405 fighters.")
st.write("Made by @yangsl")
st.markdown("""<br><br>""", unsafe_allow_html=True)

df = pd.read_csv("final_values.csv")

# Search bar
search_query = st.text_input("Search by fighter name:", "")

num_rows_to_display = st.selectbox("Number of rows to display:", options=[10, 20, 30, 40, 50, 100], index=2)  # Default to 30

st.markdown("""<br><br>""", unsafe_allow_html=True)

if search_query:
    df_filtered = df[df['name'].str.contains(search_query, case=False)]
else:
    df_filtered = df.head(num_rows_to_display)

multipliers = [1.2, 1.4, 1.6, 2.0, 2.5]

for _, row in df_filtered.iterrows():

    value_key = f"value_{row['name'].replace(' ', '_')}"
    

    if value_key not in st.session_state:
        st.session_state[value_key] = row['Value']
    
    col1, col2, *button_cols = st.columns([2, 1] + [0.6 for _ in multipliers])

    with col1:
        st.markdown(f"## {row['name']}")

    with col2:
        value_placeholder = st.markdown(f"<h2 style='color: #90ee90;'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)

    for i, multiplier in enumerate(multipliers):
        if button_cols[i].button(f'{multiplier}x', key=f'{multiplier}_{row.name}'):
            st.session_state[value_key] = row['Value'] * multiplier
            value_placeholder.markdown(f"<h2 style='color: #90ee90;'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)

    with st.expander("More Data"):
        data_for_chart = row.drop(labels=['name', 'Value'])
        chart_data = pd.DataFrame(data_for_chart)
        chart_data = chart_data.rename(columns={row.name: 'Value'}).reset_index()
        chart_data.columns = ['Category', 'Value']
        st.bar_chart(chart_data.set_index('Category'))