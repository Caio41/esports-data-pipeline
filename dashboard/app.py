import streamlit as st 

st.set_page_config(
    page_title='LoL Esports Analytics',
    layout='wide'
)

st.title("LoL Esports Analytics Dashboard")

tab_pt, tab_en = st.tabs(['Português', 'English'])

with tab_pt:

    st.markdown("""
    ### Pipeline de dados para análise de partidas profissionais de League of Legends.

    **Stack do projeto**:

    - **Spark** → ETL
    - **Airflow** → Orquestração
    - **DuckDB** → Database
    - **Streamlit** → Dashboard
                

    Acesse os dashboards através do menu na esquerda.
    """)


with tab_en:
     st.markdown("""
    ### Data pipeline for professional League of Legends match analysis.

    **Project Stack**:

    - **Spark** → ETL
    - **Airflow** → Orchestration
    - **DuckDB** → Database
    - **Streamlit** → Dashboard
                

    Access the dashboards through the menu on the left.
    """)