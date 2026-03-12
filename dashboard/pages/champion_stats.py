import streamlit as st
from analytics.queries import champion_winrate

st.title("Champion Stats")

league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None

df = champion_winrate(league)

st.dataframe(df)
st.bar_chart(df.head(10), x="champion", y="winrate")