from requests import Session

# Wattpad denies all requests that don't have headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# Data payload with username/email and password
data = {"username": "Example_Username/Email", "password": "Example_Password"}

# Use a requests Session to manage cookies
with Session() as session:
    # Make HTTP POST request to receive authentication cookies
    # Cookies are automatically saved to the Session object
    with session.post(
        "https://www.wattpad.com/auth/login?&_data=routes%2Fauth.login",
        data=data,
        headers=headers,
    ) as response:
        if not response.cookies.items():
            print("Didn't receive any cookies, is the login info correct?")
            exit()

    # Example usage of authentication cookies
    # Prints out the titles of the first 20 stories in the user's library
    with session.get(
        "https://www.wattpad.com/library?limit=20&offset=0&_data=routes/_currentReads.library",
        headers=headers,
    ) as response:
        json = response.json()
        for story in json["libraryStories"]["stories"]:
            print(story["title"])
