from airflow.sdk import dag,task
from datetime import datetime

@dag(
    dag_id="first_learning_dag",
    description="This is my first learning DAG",
    schedule=None, 
    start_date=datetime(2023, 1, 1),
    catchup=False,
)
def first_learning_dag():


    @task
    def print_hello():
        print("Hello World!")

    @task
    def print_goodbye():
        print("Goodbye World!")

    task1 = print_hello()
    task2 = print_goodbye()

    task1 >> task2

first_learning_dag()
