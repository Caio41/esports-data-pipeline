import streamlit as st

from analytics.queries import winrate_by_side, avg_game_time

league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None


st.title("League Stats")

df_winrate_by_side = winrate_by_side(league)
df_avg_game_time = avg_game_time(league)

st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Win Rate by Side')
    st.bar_chart(df_winrate_by_side, x='side', y='winrate')
   
with col2:
    st.subheader('Avarage Game Time by League')
    st.bar_chart(df_avg_game_time, x='league', y='avg_game_minutes')
    
#st.dataframe(df_winrate_by_side)
#st.dataframe(df_avg_game_time)