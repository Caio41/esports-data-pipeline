import streamlit as st
from analytics.queries import player_stats

st.title("Player Stats")


league = st.selectbox('League', ['All', 'LCK', 'LPL', 'LEC', 'CBLOL', 'LCS', 'LCP'])
if league == 'All':
    league = None

df = player_stats(league)

st.markdown('---')

top_player = df.iloc[0]
st.subheader(f"Top Performing Player: {top_player['playername']}")

col1, col2, col3 = st.columns(3) 
with col1: 
    st.metric(
        label='KDA Ratio',
        value=f"{top_player['avg_kda']:.2f}"
    )

with col2:
    st.metric(
        label='Win Rate',
        value=f"{top_player['winrate'] * 100:.1f}%"
    ) 

with col3:
    st.metric(
        label='Total Games Played',
        value=top_player['games']
    )

st.markdown('---')

st.subheader('Full Player Statistics')
st.markdown('Players with more than 20 games played in the seleceted league(s).')
st.dataframe(df)