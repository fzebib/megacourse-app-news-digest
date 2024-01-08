import requests
import os
from send_email import send_email

news_org_api_env = "NEWS_ORG_API"
api_key = os.getenv(news_org_api_env)

url = (
      f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-27"
      f"&sortBy=publishedAt&apiKey="
      f"{api_key}"
)
request = requests.get(url)
content = request.json()
email_content = {'title': [], 'description':[] }

body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
      body = body + article["title"] + "\n" + article["description"] + 2*"\n"
   #email_content[article["title"]] = article["title"]
#    email_content["title"].append(article["title"])
#    email_content["description"].append(article["description"])

body = body.encode("utf-8")
send_email(message=body)


    



