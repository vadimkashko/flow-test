from prefect import task, flow
from
from prefect_gitlab import GitLabRepository, GitLabCredentials


gitlab_repository_block = GitLabRepository.load("default")
# gitlab_credentials_block = GitLabCredentials.load("vkashko-creds")

@task
def my_task():
    print("I'm a task!")


@flow
def my_flow():
    print("Flow starts!")
    my_task()
    print("Flow finished!")


if __name__ == "__main__":
    # print(gitlab_credentials_block.token.get_secret_value())
    # print(gitlab_credentials_block.url)
    # print(gitlab_repository_block._create_repo_url())
    my_flow.from_source(
        source=gitlab_repository_block,
        entrypoint="flows/test_flow.py:my_flow",
    ).deploy(
        name="deployment",
        work_pool_name="td-analysts",
    )
    # my_flow()
