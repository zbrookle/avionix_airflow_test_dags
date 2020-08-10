from airflow.models.dag import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.bash_operator import BashOperator

DAG_NAME = "print_env"
default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    "start_date": datetime(2020, 1, 1),
}
with DAG(DAG_NAME, schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    print_my_env = BashOperator(task_id="print_my_env", bash_command="printenv")
