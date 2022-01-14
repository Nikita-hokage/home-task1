import requests

while True:
    command = input()
    if command == "add":
        req = requests.get("http://aws.random.cat/meow")
        url = req.text[9:-2]
        url = url.replace("\\", "")
        cat = requests.get(url)
        fin = open("input.jpg", "wb")
        fin.write(cat.content)
        fin.close()
