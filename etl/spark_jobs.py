import sys

from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, substring


def run_spark_etl(raw_path: str, processed_data_path: str):
    spark = SparkSession.builder.appName('esports_etl').getOrCreate()


    raw_df = spark.read.csv(raw_path, header=True)

    players_df = raw_df.filter(col('position') != 'team')
    teams_df = raw_df.filter(col('position') == 'team')

    fact_player_matches = players_df.select(
        'gameid', 'url', 'league', 'side', 'position', 'playername',
        'teamname', 'champion', 
        col('kills').cast('int'), 
        col('deaths').cast('int'), 
        col('assists').cast('int'), 
        col('result').cast('int')
    )

    fact_team_matches = teams_df.select(
        'gameid', 'league', 'teamname', 'side', 
        col('kills').cast('int'), 
        col('dragons').cast('int'), 
        col('barons').cast('int'), 
        col('result').cast('int')
    )


    dim_match = raw_df.select(
        'gameid', 'league', 'date', 'patch', 
        (
            substring(col('gamelength'), 1, 2).cast('int') * 60 + 
            substring(col('gamelength'), 3, 2).cast('int')
        ).alias('gamelength_seconds')
    ).distinct()


    fact_player_matches.write.mode('overwrite').parquet(f'{processed_data_path}/fact_player_matches.parquet')
    fact_team_matches.write.mode('overwrite').parquet(f'{processed_data_path}/fact_team_matches.parquet')
    dim_match.write.mode('overwrite').parquet(f'{processed_data_path}/dim_match.parquet')

    spark.stop()



if __name__ == "__main__":
    raw_path = sys.argv[1]
    processed_data_path = sys.argv[2]
    run_spark_etl(raw_path, processed_data_path)
 