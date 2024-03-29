from prefect import task, flow
# from prefect_github import GitHubRepository, GitHubCredentials
# from prefect_gitlab import GitLabRepository, GitLabCredentials


# gitlab_repository_block = GitLabRepository.load("default")
# gitlab_credentials_block = GitLabCredentials.load("vkashko-creds")
# github_repository_block = GitHubRepository.load("github-repo")


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
        source="https://prefect:glpat-nzcQr3RS9hzzAzzjpkn2@gitlab.trainingdata.int/td/business-intelligence/dwh/prefect-test.git",
        entrypoint="flows/test_flow.py:my_flow",
    ).deploy(
        name="deployment",
        work_pool_name="td-analysts",
    )
    # my_flow()
