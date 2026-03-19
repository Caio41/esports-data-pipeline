from pyspark.sql import DataFrame
from pyspark.sql.functions import col, substring

def transform_player_matches(raw_df: DataFrame) -> DataFrame:
    players_df = raw_df.filter(col('position') != 'team')
    
    fact_player_matches = players_df.select(
        'gameid', 'url', 'league', 'side', 'position', 'playername',
        'teamname', 'champion', 
        col('kills').cast('int'), 
        col('deaths').cast('int'), 
        col('assists').cast('int'), 
        col('result').cast('int')
    )

    return fact_player_matches


def transform_team_matches(raw_df: DataFrame) -> DataFrame:
    teams_df = raw_df.filter(col('position') == 'team')

    fact_team_matches = teams_df.select(
        'gameid', 'league', 'teamname', 'side', 
        col('kills').cast('int'), 
        col('dragons').cast('int'), 
        col('barons').cast('int'), 
        col('result').cast('int')
    )
    
    return fact_team_matches


def transform_match_dim(raw_df: DataFrame) -> DataFrame:
    
    dim_match = raw_df.select(
        'gameid', 'league', 'date', 'patch', 
        (
            substring(col('gamelength'), 1, 2).cast('int') * 60 + 
            substring(col('gamelength'), 3, 2).cast('int')
        ).alias('gamelength_seconds')
    ).distinct()

    return dim_match

