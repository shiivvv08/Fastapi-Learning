#  web-crawling in python

"""import requests
from bs4 import BeautifulSoup

url = "https://hcesonepat.org/"

response = requests.get(url)
soup = BeautifulSoup(requests.text,"html.parse")
print(soup)
"""

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://indianexpress.com/"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text , "html.parser")
    title = []
    for item in soup.find_all("a" , class_="topblockNews_sidebarLink"):
        title.append(item.text)
        
    return {
        "news": title
    }
    
    
    
    