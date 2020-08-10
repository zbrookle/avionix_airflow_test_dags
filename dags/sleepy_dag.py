from airflow.models.dag import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from time import sleep

DAG_NAME = "sleepy_test"
default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "start_date": datetime(2020, 1, 1),
}


def sleepy_func():
    for i in range(5):
        print("I'm sleepy...")
        print("zzzzzz...")
        sleep(2)


with DAG(DAG_NAME, schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    sleepy_time = PythonOperator(task_id="sleepy_time", python_callable=sleepy_func)
