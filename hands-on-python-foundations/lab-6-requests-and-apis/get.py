import sys
import requests


def main():
    url = "https://automatetheboringstuff.com/"

    # Get user information to customize the User-Agent header.
    name = input("Your name: ")
    email = input("Your email: ")

    headers = {"User-Agent": f"{name} ({email})"}

    # Perform the GET request.
    response = requests.get(url, headers=headers)
    print(f"{response.status_code} - {response.reason}")

    # If the response status code indicates an error (300 or higher), exit gracefully.
    if response.status_code >= 300:
        sys.exit("Request failed. Exiting.")

    # Print the response body.
    print(response.text)

    # Optionally, save the response to a file.
    # Uncomment the lines below to enable file saving.
    #
    # output_file = "data/get_output.html"
    # with open(output_file, "w", encoding="utf-8") as file:
    #     file.write(response.text)
    # print(f"File saved to '{output_file}'")


if __name__ == "__main__":
    main()
