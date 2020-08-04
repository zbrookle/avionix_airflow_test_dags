from airflow.models.dag import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.bash_operator import BashOperator

DAG_NAME = "test"
default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "start_date": datetime(2020, 1, 1),
}
with DAG(DAG_NAME, schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    run_this_1 = DummyOperator(task_id="run_this_1")
    run_this_2 = DummyOperator(task_id="run_this_2")
    run_this_2.set_upstream(run_this_1)
    run_this_3 = BashOperator(
        task_id="run_this_3",
        bash_command="echo success",
        executor_config={"service_account_name": "airflow-pod-account"},
    )
    run_this_3.set_upstream(run_this_2)
