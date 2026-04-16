#beautifulsoup4 is a library in Python that allows you to parse HTML and XML documents. It provides a simple way to navigate and search through the document tree, making it easier to extract data from web pages. BeautifulSoup is commonly used for web scraping tasks, where you want to extract specific information from websites.
from  bs4 import BeautifulSoup  
import requests  
import csv
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# product_pod

books=soup.find_all("article",class_="product_pod") #returns a list of all the elements with the class "product_pod"

# print(books[0])
# print("books:",books[0].find("p", class_="price_color"))
# print("books:",books[0].find("p", class_="price_color").text)

# print("books:",books[0].find("p", class_="star-rating")["class"][1])
# print("books:",books[0].find("p", class_="star-rating")["class"])

# print(books[0].find("a"))
# print(books[0].find("a")["href"])

all_books = []
for book in books:
    title=book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    image=book.find("a").img["src"]
    link=book.find("a")["href"]
    all_books.append({"Title": title, "Price": price, "Rating": rating, "Image": image, "Link": link})

    # price2=book.find("div",class_="product_price").p.text
    # print(f"Title: {title}, Price: {price}, Rating: {rating}, Price2: {price2}")


with open("books.csv","a", newline='', encoding='utf-8') as f:
    writer=csv.DictWriter(f, fieldnames=["Title", "Price", "Rating", "Image", "Link"])   
    writer.writeheader()
    writer.writerows(all_books)