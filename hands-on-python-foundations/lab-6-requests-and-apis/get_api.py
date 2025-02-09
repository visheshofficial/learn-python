"""
Get the reactions to a GitHub issue

Issue: https://github.com/ariannedee/python-foundations-3-weeks/issues/1
API endpoint: https://docs.github.com/en/rest/reference/issues#get-an-issue
"""

import csv
import sys
import requests
from pprint import pprint


def main():
    base_url = "https://api.github.com"
    username = "ariannedee"
    repository = "python-foundations-3-weeks"
    issue_number = 1
    url = f"{base_url}/repos/{username}/{repository}/issues/{issue_number}"

    response = requests.get(url)
    print(f"{response.status_code} - {response.reason}")
    if response.status_code >= 300:
        sys.exit("Error: GET request failed.")

    # Parse the JSON response.
    issue_data = response.json()
    reactions = issue_data.get("reactions", {})

    # Build a list of dictionaries for CSV output, filtering out non-reaction keys.
    reactions_to_csv = []
    for reaction, count in reactions.items():
        if reaction in ("url", "total_count"):
            continue
        reactions_to_csv.append({"Reaction": reaction, "Count": count})

    pprint(reactions_to_csv)

    # Write the reaction data to a CSV file.
    with open("reactions.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Reaction", "Count"])
        writer.writeheader()
        writer.writerows(reactions_to_csv)

    # Map reaction names to emojis.
    reaction_to_emoji = {
        "+1": "👍",
        "-1": "👎",
        "laugh": "😄",
        "hooray": "🎉",
        "confused": "😕",
        "heart": "❤️",
        "rocket": "🚀",
        "eyes": "👀",
    }

    # Build a string with each emoji repeated according to its count.
    output_str = ""
    for reaction in reactions_to_csv:
        name = reaction["Reaction"]
        as_emoji = reaction_to_emoji.get(name, "")
        count = reaction["Count"]
        output_str += as_emoji * count

    print(output_str)


if __name__ == "__main__":
    main()
