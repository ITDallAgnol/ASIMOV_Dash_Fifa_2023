import streamlit as st 

df_data = st.session_state["data"]
df_data

clubes = df_data["Club"].value_counts().index #or df_data["Club"].unique
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[( df_data["Club"] == club )]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)