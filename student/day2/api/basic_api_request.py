import requests


try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    response.raise_for_status()

    print("Status code:", response.status_code)

    data = response.json()

    print("Response data:")
    print(data)

    print("Name:", data["name"])
    print("Email:", data["email"])

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
