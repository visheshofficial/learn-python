import requests
import sys
import json


def main():
    # Define the URL of the API endpoint.
    url = "https://ariannedee.pythonanywhere.com/test_requests"

    # Define the data to be sent.
    data = {"username": "abcde", "password": "12345"}

    # 1. POST request with form data.
    response = requests.post(url, data=data)
    print(f"{response.status_code} - {response.reason}")
    # If the server returns a status code >= 300 (error/redirect), exit the program.
    if response.status_code >= 300:
        sys.exit("Error: POST request failed.")

    # Print the text of the response.
    print(response.text)

    # Print the actual request body that was sent.
    # For form data, this is typically URL-encoded, e.g., "username=abcde&password=12345"
    print("Request body (form data):", response.request.body)

    # 2. Attempt to send JSON data as form data (incorrect method).
    # Convert the data dictionary to a JSON string.
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data)
    # This request is likely to fail (e.g., return 400 - Bad Request)
    print(f"{response.status_code} - {response.reason}")

    # 3. Send JSON data with the correct Content-Type header.
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json_data, headers=headers)
    # Now the server recognizes the payload as JSON and should return 200 - OK.
    print(f"{response.status_code} - {response.reason}")
    # The request body will be the JSON string.
    print("Request body (JSON with header):", response.request.body)

    # 4. Send JSON data using the json parameter.
    # When using the json parameter, requests automatically encodes the data as JSON
    # and sets the Content-Type header to "application/json".
    response = requests.post(url, json=data)
    print(f"{response.status_code} - {response.reason}")
    print("Request body (using json parameter):", response.request.body)


if __name__ == "__main__":
    main()
