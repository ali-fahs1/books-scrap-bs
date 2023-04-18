import requests
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest


books = []
for i in range(1,5):
  
  
  url = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
  
  
  soup = BeautifulSoup(url.content,"lxml")
  results = soup.find_all("article",class_="product_pod")
  for result in results:
    title = result.find("img").attrs["alt"]
    price = result.find("p",class_="price_color").text
    # img.append(result.find("img"))
    # src.append(result.find("img").attrs["src"])
    stars = result.find("p").attrs["class"][1]
    books.append([title,stars,price])
    
  


with open("this.csv","w") as f:
    
    # exported = zip_longest(*file_list)
    wr= csv.writer(f)
    wr.writerow(["title","stars","price"])
    wr.writerows(books)
    