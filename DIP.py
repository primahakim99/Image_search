import os
import io
from google.cloud import vision
import pandas as pd
import requests
#from google_images_search import GoogleImagesSearch

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

file_name = r'img5.jpg'
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

print(df)

key = df.iloc[0, 0],"+",df.iloc[1, 0],"+",df.iloc[2, 0],"+",df.iloc[3, 0],"+",df.iloc[4, 0],"+",df.iloc[5, 0],"+",df.iloc[6, 0],"+",df.iloc[7, 0],"+",df.iloc[8, 0],"+",df.iloc[9, 0]
print(key)

url = "https://google-search72.p.rapidapi.com/imagesearch"

querystring = {"query":{key},"gl":"id","lr":"id","num":"10","start":"0","sort":"relevance"}

headers = {
	"X-RapidAPI-Key": "2dbc626e73mshb5c1b669c11bedcp146b63jsne88d81f0677a",
	"X-RapidAPI-Host": "google-search72.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


#<script async src="https://cse.google.com/cse.js?cx=532c0976f0f1646f5">
#</script>
#<div class="gcse-search"></div>