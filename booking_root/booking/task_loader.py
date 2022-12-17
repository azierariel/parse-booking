import requests


def load_tasks(bucket_url: str) -> list:
    # TODO: exceptions management
    tasks = requests.get(bucket_url)
    return tasks.json()["objects"]
