import requests
import os

news_org_api_env = "NEWS_ORG_API"
api_key = os.getenv(news_org_api_env)

url = (
      f"https://newsapi.org/v2/everything?q=tesla&from=2023-10-27"
      f"&sortBy=publishedAt&apiKey="
      f"{api_key}"
)
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["description"])

