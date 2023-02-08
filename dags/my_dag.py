"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def python_task_1():
    print('Caio ran this task firstly!')
    print(f"Caio's time right now: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

def python_task_2():
    print('Caio ran this task secondly!')
    print(f"Caio's time right now: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("my_dag", default_args=default_args, schedule_interval=timedelta(minutes=1), catchup=False)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = PythonOperator(task_id="python_task_1", python_callable=python_task_1, dag=dag)
t2 = PythonOperator(task_id="python_task_2", python_callable=python_task_2, dag=dag)

t1 >> t2
