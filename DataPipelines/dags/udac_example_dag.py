from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (CreateTablesOperator, StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from airflow.operators import CreateTablesOperator
from helpers import SqlQueries

#AWS_KEY = os.environ.get("AWS_KEY")
#AWS_SECRET = os.environ.get("AWS_SECRET")

v_s3_bucket = "udacity-dend"
v_log_data_key  = "log_data"
v_song_data_key = "song_data/A"
v_redshift_conn_id = "redshift"
v_aws_credentials_id = "aws_credentials"

default_args = {
    "owner": "Sparkify",
    "start_date": datetime(2021, 1, 12),
    "depends_on_past" : False,
    "retries": 3,
    "email_on_retry": False,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
}

dag = DAG("dag",
          default_args=default_args,
          description="Load and transform data in Redshift with Airflow",
          schedule_interval="0 * * * *",
          max_active_runs=1
        )

start_operator = CreateTablesOperator(task_id="Begin_execution", 
                                      dag=dag,
                                      redshift_conn_id=v_redshift_conn_id,
                                      provide_context=True)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id="Stage_events",
    dag=dag,
    table="public.staging_events",
    redshift_conn_id=v_redshift_conn_id,
    aws_credentials_id=v_aws_credentials_id,
    s3_bucket=v_s3_bucket,
    s3_key=v_log_data_key,
    provide_context=True
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id="Stage_songs",
    dag=dag,
    table="public.staging_songs",
    redshift_conn_id=v_redshift_conn_id,
    aws_credentials_id=v_aws_credentials_id,
    s3_bucket=v_s3_bucket,
    s3_key=v_song_data_key,
    provide_context=True
)

load_songplays_table = LoadFactOperator(
    task_id="Load_songplays_fact_table",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    sql=SqlQueries.songplay_table_insert
)

load_user_dimension_table = LoadDimensionOperator(
    task_id="Load_user_dim_table",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    sql=SqlQueries.user_table_insert,
    mode=LoadDimensionOperator.append,
    table="public.users"
)

load_song_dimension_table = LoadDimensionOperator(
    task_id="Load_song_dim_table",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    sql=SqlQueries.song_table_insert,
    mode=LoadDimensionOperator.append,
    table="public.songs"
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id="Load_artist_dim_table",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    sql=SqlQueries.artist_table_insert,
    ode=LoadDimensionOperator.append,
    table="public.artists"
)

load_time_dimension_table = LoadDimensionOperator(
    task_id="Load_time_dim_table",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    sql=SqlQueries.time_table_insert,
    ode=LoadDimensionOperator.append,
    table="public.time"
)

run_quality_checks = DataQualityOperator(
    task_id="Run_data_quality_checks",
    dag=dag,
    redshift_conn_id=v_redshift_conn_id,
    tables=["public.songplays",
            "public.users",
            "public.songs",
            "public.artists",
            "public.time"]
)

end_operator = DummyOperator(task_id="Stop_execution",  dag=dag)

start_operator >> [stage_events_to_redshift, stage_songs_to_redshift] >> load_songplays_table
load_songplays_table >> [load_song_dimension_table, load_user_dimension_table, load_artist_dimension_table, load_time_dimension_table] >> run_quality_checks
run_quality_checks >> end_operator