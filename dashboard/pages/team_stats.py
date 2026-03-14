import streamlit as st
from analytics.queries import team_stats

st.title("Team Metrics")

league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None

df = team_stats(league)

st.subheader('Top 10 Teams by Win Rate')

st.bar_chart(
    df.head(10),
    x="teamname",
    y="winrate",
    sort=False
)

st.dataframe(df)