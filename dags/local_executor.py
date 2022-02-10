"""
Example to demonstrate "python operator" of airflow
This is an example of local executor
 """

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time


def v1():
    print("viola!")
    time.sleep(5)


def v2():
    print("viola bye!")
    time.sleep(2)


def v3():
    print("10")


args_dag = {
    "owner": "airflow",
    "start_date": datetime(2022, 2, 10),
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG(
    dag_id="local_executor_demo",
    schedule_interval="@hourly",
    default_args=args_dag,
    catchup=False,
)

task_01 = PythonOperator(task_id="v1", python_callable=v1, dag=dag)
task_02 = PythonOperator(task_id="v2", python_callable=v1, dag=dag)
task_03 = PythonOperator(task_id="v3", python_callable=v3, dag=dag)

task_01 >> task_03 >> task_02