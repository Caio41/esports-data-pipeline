import sys

from pyspark.sql import SparkSession 

from etl.transform import transform_match_dim, transform_player_matches, transform_team_matches


def run_spark_etl(raw_path: str, processed_data_path: str):
    print('Reading data...')
    spark = SparkSession.builder.appName('esports_etl').getOrCreate()

    raw_df = spark.read.csv(raw_path, header=True)

    print('Processing data...')
    fact_player_matches = transform_player_matches(raw_df)
    fact_team_matches = transform_team_matches(raw_df)
    dim_match = transform_match_dim(raw_df) 

    print('Saving data...')
    fact_player_matches.write.mode('overwrite').parquet(f'{processed_data_path}/fact_player_matches.parquet')
    fact_team_matches.write.mode('overwrite').parquet(f'{processed_data_path}/fact_team_matches.parquet')
    dim_match.write.mode('overwrite').parquet(f'{processed_data_path}/dim_match.parquet')

    spark.stop()
    print('Job finished')



if __name__ == "__main__":
    raw_path = sys.argv[1]
    processed_data_path = sys.argv[2]
    run_spark_etl(raw_path, processed_data_path)
 