from prefect import task, flow


@task
def my_task():
    print("I'm a task!")

@flow
def my_flow():
    print("Flow starts!")
    my_task()
    print("Flow finished!")

if __name__ == "__main__":
    my_flow()