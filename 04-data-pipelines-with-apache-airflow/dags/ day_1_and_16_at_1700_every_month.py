from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone


with DAG(
    "day_1_and_16_at_1700_every_month",
    start_date=timezone.datetime(2024,3,10),
    schedule="0 17 1,16 * 1",
    tags=["DEB","skooldio"],
    catchup=False,
          
):
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")

    t1 >> t2
