import streamlit as st
import json
import os

st.title('Interactive Attribute Menu')
basePath = os.path.dirname(os.path.abspath(__file__))
with open('game_data/items.json') as f:
    items = json.load(f)
top_level = st.selectbox('Pick a top level category.',['armor_components','armor_pieces','weapon_types'])
mid_level_options = list(items[top_level].keys())
mid_level = st.selectbox('Pick a secondary category.', mid_level_options)

st.write(items[top_level][mid_level])

st.write('Add a new element:')
for key in items[top_level][mid_level][0]:
    st.text_input(key, items[top_level][mid_level][0][key])