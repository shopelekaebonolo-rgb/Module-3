#PA1101 - Access the web and fetch internet resources using platform functionalities: Setting things up; Loading URLs

# Import requests library
import requests

# define api endpoint (combination of domain and path)
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

#Display all users
print(data)

for user in data:
    print(user["name"])