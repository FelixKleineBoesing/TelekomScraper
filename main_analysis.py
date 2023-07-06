import json

with open("data/cleaned_html.json", "r") as f:
    data = json.load(f)

print(data)