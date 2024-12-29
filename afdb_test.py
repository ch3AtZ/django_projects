from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from random import randint
from datetime import datetime

# Define Python functions
def first_task():
    return randint(1, 10)

def second_task():
    return randint(1, 10)

def third_task():
    return randint(1, 10)

def best(ti):
    # Pull accuracies from XCom
    accuracies = ti.xcom_pull(task_ids=['first', 'second', 'third'])
    best_accuracy = max(accuracies)
    # Branch logic
    if best_accuracy > 8:
        return 'accurate'
    else:
        return 'inaccurate'

# Define the DAG
with DAG(
    "my_dag_1_2",
    start_date=datetime(2024, 11, 25),
    schedule="@daily",
    catchup=False
) as dag:

    # Define tasks
    first_task_A = PythonOperator(
        task_id="first",
        python_callable=first_task
    )

    second_task_A = PythonOperator(
        task_id="second",
        python_callable=second_task
    )

    third_task_A = PythonOperator(
        task_id="third",
        python_callable=third_task
    )

    choose_best_choice = BranchPythonOperator(
        task_id="best",
        python_callable=best
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
    )

    in_accurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )

    # Set dependencies
    [first_task_A, second_task_A, third_task_A] >> choose_best_choice
    choose_best_choice >> [accurate, in_accurate]
