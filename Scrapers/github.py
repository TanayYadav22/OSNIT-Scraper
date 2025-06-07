import requests

def scrape(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"User {username} not found on GitHub."}

    data = response.json()
    return {
        "name": data.get("name"),
        "bio": data.get("bio"),
        "location": data.get("location"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "created_at": data.get("created_at")
    }
