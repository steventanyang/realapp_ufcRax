import streamlit as st
import pandas as pd

st.set_page_config(page_title="Historical UFC Rax", page_icon="🥊", layout="wide", initial_sidebar_state="collapsed")

st.title("Historical UFC Rax")
st.write("Click on 'more data' for RAX calculation.")
st.write("Made by @yangsl")
st.markdown("""<br><br>""", unsafe_allow_html=True)

df = pd.read_csv("test.csv")

# Search bar
search_query = st.text_input("Search by fighter name:", "")

num_rows_to_display = st.selectbox("Number of rows to display:", options=[10, 20, 30, 40, 50, 100], index=2)  # Default to 30

st.markdown("""<br><br>""", unsafe_allow_html=True)

reset_button = st.button("Reset All Multipliers")

def reset_multipliers():
    for key in st.session_state.keys():
        if key.startswith("multiplier_"):
            st.session_state[key] = 1.2
        if key.startswith("value_"):
            fighter_name = key.replace("value_", "").replace("_", " ")
            original_value = df.loc[df['name'] == fighter_name, 'Value'].values[0]
            st.session_state[key] = round(original_value * 1.2)

if reset_button:
    reset_multipliers()

st.markdown("""<br><br>""", unsafe_allow_html=True)

if search_query:
    df_filtered = df[df['name'].str.contains(search_query, case=False)]
else:
    df_filtered = df.head(num_rows_to_display)

multipliers = [1.2, 1.4, 1.6, 2.0, 2.5, 4.0, 6.0]
multiplier_colors = {
    1.2: '#6591B2',  # common
    1.4: '#689F6D',  # uncommon
    1.6: '#BA8057',  # rare
    2.0: '#AE5353',  # epic
    2.5: '#7258A9',  # legendary
    4.0: '#B9985A',  # mystic
    6.0: '#AB6FB0',  # iconic
}
multiplier_names = {
    1.2: 'Common',  # common
    1.4: 'Uncommon',  # uncommon
    1.6: 'Rare',  # rare
    2.0: 'Epic',  # epic
    2.5: 'Legendary',  # legendary
    4.0: 'Mystic',  # mystic
    6.0: 'Iconic',  # iconic
}

for _, row in df_filtered.iterrows():

    value_key = f"value_{row['name'].replace(' ', '_')}"
    multiplier_key = f"multiplier_{row['name'].replace(' ', '_')}"

    if value_key not in st.session_state:
        st.session_state[value_key] = round(row['Value'] * 1.2)
    
    if multiplier_key not in st.session_state:
        st.session_state[multiplier_key] = 1.2
    
    col1, col2, *button_cols = st.columns([2, 1] + [0.6 for _ in multipliers])

    with col1:
        st.markdown(f"## {row['name']}")

    with col2:
        color = multiplier_colors[st.session_state[multiplier_key]]
        value_placeholder = st.markdown(f"<h2 style='color: {color};'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)

   # Here we add a loop over the button columns to add spacing
    for i, multiplier in enumerate(multipliers):
        with button_cols[i]:
            
            st.markdown(f"<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            if st.button(f'{multiplier}x', key=f'{multiplier}_{row.name}'):
                # new_value = round(row['Value'] * multiplier)
                new_value = round(row[multiplier_names[multiplier]])
                st.session_state[value_key] = new_value
                st.session_state[multiplier_key] = multiplier
                color = multiplier_colors[multiplier]
                value_placeholder.markdown(f"<h2 style='color: {color};'>{st.session_state[value_key]}</h2>", unsafe_allow_html=True)


    with st.expander("More Data"):
        data_for_chart = row.drop(labels=['name', 'Value'])
        chart_data = pd.DataFrame(data_for_chart)
        chart_data = chart_data.rename(columns={row.name: 'Value'}).reset_index()
        chart_data.columns = ['Category', 'Value']
        st.bar_chart(chart_data.set_index('Category'))