import os
import io
from google.cloud import vision
import pandas as pd
import requests

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = r'img1.jpg'
image_path = f'.\Images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
    
image = vision.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

df = pd.DataFrame(columns=['description', 'score'])
for label in labels:
    df = df.append(
        dict(
            description = label.description,
            score = label.score
        ),ignore_index = True
    )


key = df.iloc[0, 0], df.iloc[1, 0], df.iloc[2, 0]
print(key)

url = "https://real-time-web-search.p.rapidapi.com/search"

querystring = {"q":{key},"limit":"5"}

headers = {
	"X-RapidAPI-Key": "2dbc626e73mshb5c1b669c11bedcp146b63jsne88d81f0677a",
	"X-RapidAPI-Host": "real-time-web-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
