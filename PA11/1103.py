#import requests

import requests

#define the api url
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

# send get request with parameters
response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Request URL:", response.url)

data = response.json()

for post in data:
    print("Post ID:", post["id"])
    print("Post Title:", post["title"])
    print("-------------------------")


#Post Request 
#Send information to an api

new_post ={
    "title": "Learning Python",
    "body": "We are learning GET AND POST request",
    "userId": 1
}
response = requests.post(url, json=new_post)
print("Post status Code:", response.status_code)