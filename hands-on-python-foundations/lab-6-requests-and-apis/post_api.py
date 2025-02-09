import os
import requests


def main():

    # Example 1: POST request to GitHub homepage (expected to return 404)
    github_url = "https://github.com"
    response = requests.post(github_url, json={})
    print(f"{response.status_code} {response.reason}")

    # Example 2: POST request to GitHub API without authentication (expected 401 Unauthorized)
    base_url = "https://api.github.com"
    username = "ariannedee"
    repository = "python-foundations-3-weeks"
    issue_number = 1
    api_url = (
        f"{base_url}/repos/{username}/{repository}/issues/{issue_number}/reactions"
    )

    response = requests.post(api_url)
    print(f"{response.status_code} {response.reason}")

    # Example 3: Authenticated POST request to add a reaction (expected result depends on token validity)
    data = {"content": "+1"}
    token = os.getenv("VISHESHOFFICIAL_PYTHON_TUTORIAL")
    headers = {"Authorization": f"bearer {token}"}

    response = requests.post(api_url, json=data, headers=headers)
    print(f"{response.status_code} {response.reason}")


if __name__ == "__main__":
    main()
