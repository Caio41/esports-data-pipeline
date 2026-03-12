import duckdb 

def champion_winrate(league: str | None = None):
    con = duckdb.connect()
    query = '''
        SELECT champion, AVG(result) AS winrate, COUNT(*) AS games
        FROM 'data/processed/fact_player_matches.parquet'
        WHERE league IN ('LCK','LEC','LCS','LPL','CBLOL','LCP')
    '''

    params = [] 
    if league:
        query += ' AND league = ?'
        params.append(league)
    
    query += '''
        GROUP BY champion
        ORDER BY games DESC 
    '''

    return con.execute(query, params).df()


def player_stats(league: str | None = None):
    con = duckdb.connect()
    query = '''
        SELECT playername, COUNT(*) AS games, 
        AVG(result) AS winrate,
        AVG(kills) AS avg_kills, 
        AVG(deaths) AS avg_deaths,
        AVG(assists) AS avg_assists,
        AVG((kills+ assists) / NULLIF(deaths, 0)) AS avg_kda
        FROM 'data/processed/fact_player_matches.parquet'
        WHERE league IN ('LCK','LEC','LCS','LPL','CBLOL','LCP')
    '''

    params = [] 
    if league:
        query += ' AND league = ?'
        params.append(league)
    
    query += '''
        GROUP BY playername
        HAVING COUNT(*) > 20
        ORDER BY avg_kda DESC 
    '''
        
    return con.execute(query, params).df()


def team_stats(league: str | None = None):
    con = duckdb.connect()

    query = '''
        SELECT
            teamname,
            COUNT(*) AS games,
            AVG(result) AS winrate,
            AVG(kills) AS avg_kills,
            AVG(dragons) AS avg_dragons,
            AVG(barons) AS avg_barons
        FROM 'data/processed/fact_team_matches.parquet'
        WHERE league IN ('LCK','LEC','LCS','LPL','CBLOL','LCP')
    '''

    params = []

    if league:
        query += " AND league = ?"
        params.append(league)

    query += '''
        GROUP BY teamname
        HAVING COUNT(*) > 10
        ORDER BY winrate DESC
    '''

    return con.execute(query, params).df()


def avg_game_time(league: str | None = None):
    con = duckdb.connect()

    query = '''
        SELECT league, AVG(gamelength_seconds) / 60 AS avg_game_minutes
        FROM 'data/processed/dim_match.parquet'
        WHERE league IN ('LCK','LEC','LCS','LPL','CBLOL','LCP')
    '''
    params = []

    if league:
        query += " AND league = ?"
        params.append(league)

    query += '''
        GROUP BY league
        ORDER BY avg_game_minutes
    '''

    return con.execute(query, params).df()


def winrate_by_side(league: str | None = None):
    con = duckdb.connect()

    query = '''
        SELECT side, AVG(result) AS winrate, COUNT(*) AS games
        FROM 'data/processed/fact_team_matches.parquet'
        WHERE league IN ('LCK','LEC','LCS','LPL','CBLOL','LCP')
    '''
    params = []

    if league:
        query += " AND league = ?"
        params.append(league)

    query += '''
        GROUP BY side
    '''

    return con.execute(query, params).df()