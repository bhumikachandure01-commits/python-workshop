import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999"
    )

    response.raise_for_status()
    data = response.json()
    print("Name:", data["name"])
    print("Email:", data["email"])
    
except requests.exceptions.HTTPError as error:
    print(f"API request failed:{error}")

except requests.exceptions.RequestException as error:
    print(f"Request failed:{error}")
