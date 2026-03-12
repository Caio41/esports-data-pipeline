import pandas as pd 

raw_df = pd.read_csv('data/raw/2026_LoL_esports_match_data_from_OraclesElixir.csv')

players_df = raw_df[raw_df['position'] != 'team']
teams_df = raw_df[raw_df['position'] == 'team']

print(list(raw_df.columns))


fact_player_matches = players_df[
    [
        'gameid',
        'url',
        'league',
        'side',
        'position',
        'playername',
        'teamname',
        'champion',
        'kills',
        'deaths',
        'assists',
        'result'
    ]
]

fact_team_matches = teams_df[
    [
        'gameid',
        'league',
        'teamname',
        'side',
        'kills',
        'dragons',
        'barons',
        'result'
    ]
]

dim_match = raw_df[
    [
        'gameid',
        'league',
        'date',
        'patch',
        'gamelength'
    ]
].drop_duplicates()


fact_player_matches.to_parquet('data/processed/fact_player_matches.parquet')
fact_team_matches.to_parquet('data/processed/fact_team_matches.parquet')
dim_match.to_parquet('data/processed/dim_match.parquet')
