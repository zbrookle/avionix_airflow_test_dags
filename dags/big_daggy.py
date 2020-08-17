from airflow.models.dag import DAG
from datetime import datetime
from airflow.operators.bash_operator import BashOperator

DAG_NAME = "big_dag"
default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 1, 1),
}
with DAG(DAG_NAME, schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    echo_success = BashOperator(
        task_id="echo_success",
        bash_command="echo success",
        executor_config={
            "KubernetesExecutor": {
                "resources": {
                    "requests": {"cpu": "0.5", "memory": "200Mi"},
                }
            }
        },
    )
