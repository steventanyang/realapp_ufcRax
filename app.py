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

multiplier_colors = {
    1.2: '#FFD700', 
    1.4: '#C0C0C0', 
    1.6: '#CD7F32',  
    2.0: '#FF4500',  
    2.5: '#008000',  
}

for _, row in df_filtered.iterrows():

    value_key = f"value_{row['name'].replace(' ', '_')}"
    color_key = f"color_{row['name'].replace(' ', '_')}"

    if value_key not in st.session_state:
        st.session_state[value_key] = round(row['Value'] * 1.2)  # Default to 1.2x the 'Value'

    if color_key not in st.session_state:
        st.session_state[color_key] = multiplier_colors[1.2]  # Color corresponding to 1.2x

    
    full_row, col1, col2, *button_cols = st.columns([0.1, 2, 1] + [0.6 for _ in multipliers])

    with col1:
        st.markdown(f"## {row['name']}")

    with col2:
        # Use the color from session state
        value_placeholder = st.markdown(f"<h2 style='color: {st.session_state[color_key]};'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)

    for i, multiplier in enumerate(multipliers):
        with button_cols[i]:
            if st.button(f'{multiplier}x', key=f'{multiplier}_{row.name}'):
                new_value = round(row['Value'] * multiplier)
                st.session_state[value_key] = new_value
                # Update the color in the session state based on the multiplier clicked
                st.session_state[color_key] = multiplier_colors[multiplier]
                value_placeholder.markdown(f"<h2 style='color: {st.session_state[color_key]};'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)

    with st.expander("More Data"):
        data_for_chart = row.drop(labels=['name', 'Value'])
        chart_data = pd.DataFrame(data_for_chart)
        chart_data = chart_data.rename(columns={row.name: 'Value'}).reset_index()
        chart_data.columns = ['Category', 'Value']
        st.bar_chart(chart_data.set_index('Category'))