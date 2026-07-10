url = input("URL: ").strip()
username = url.replace("https://github.com/", "") # replace with nothing
username = url.removeprefix("https://github.com/")
print(username)