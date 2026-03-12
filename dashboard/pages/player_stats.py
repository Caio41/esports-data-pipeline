import streamlit as st
from analytics.queries import player_stats

st.title("Player Stats")


league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None

df = player_stats(league)

st.dataframe(df)