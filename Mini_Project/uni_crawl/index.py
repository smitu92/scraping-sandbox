uni_exam="https://ksv.ac.in/index.php/exampapers"
url1="https://ksv.ac.in/paper/dropdown.php?pageID=2&&sem={semester}&&course_id=6&&year={year}"
import requests
import csv
import os
from bs4 import BeautifulSoup
from create_folder import create_folder, create_subfolder
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": uni_exam,  # you already have this variable — use it!
}

response = requests.get(url1.format(semester=1, year=2023),headers=headers)
# print("Text:",response.text)
# print("content:",response.content)

soup = BeautifulSoup(response.text, 'html.parser')
# print("soup:",soup)


# print("a:",soup.find_all("a"))
# print("a: size ",soup.find_all("a").__len__())
# print("a: 0 ",soup.find_all("a")[0].get_text())
papers=soup.find_all("a")

def clean_metadata(text,year):
    parts = [part.strip() for part in text.split(",")]
    title = list(filter(lambda x:"Semester " not in x and "BACHELOR OF ENGINEERING" not in x, parts))[0]
    date = list(filter(lambda x: str(year) in x, parts))[0].split("-")
    year = date[1].strip()
    code=title.split(" ")[0]
    month=date[0]
    subject=title.split(" ", 1)[1]
    return title, year, code, month, subject

def download_paper(link, subject, month, year,path):
    # Implement the logic to download the paper using the link
    with requests.get(link, stream=True, headers=headers) as r:
        r.raise_for_status()
        print(subject, month, year)
        filename = f"{str(subject)}_{str(month)}_{str(year)}.pdf"  # You can customize the filename as needed
        filepath = os.path.join(path, filename)
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

all_papers = []
for paper in papers:
    link=paper["href"]
    title, year, code, month, subject = clean_metadata(paper.get_text(), 2023)
    all_papers.append({"Title": title, "Year": year, "Code": code, "Month": month, "Subject": subject, "Link": link})

print("All papers:", all_papers[0])



def generate_folder():
    create_folder("Exam_Papers")
    create_subfolder("Exam_Papers", "Papers")
    for paper in all_papers:
        download_paper(paper["Link"], paper["Subject"], paper["Month"], paper["Year"], "Exam_Papers/Papers")
    print("Papers downloaded successfully in 'Exam_Papers/Papers' folder.")

generate_folder()