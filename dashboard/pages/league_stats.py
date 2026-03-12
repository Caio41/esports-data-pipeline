import streamlit as st

from analytics.queries import winrate_by_side, avg_game_time

league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None


st.title("League Stats")

df_winrate_by_side = winrate_by_side(league)
df_avg_game_time = avg_game_time(league)

st.dataframe(df_winrate_by_side)
st.dataframe(df_avg_game_time)