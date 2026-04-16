s="BACHELOR OF ENGINEERING, Semester 6, ME605-N-E IOT &amp; SMART MANUFACTURING, December-2023"

# print(s.split(","))
splited = s.split(",")

# filtered = list(filter(lambda x: "Semester 6" not in x and "BACHELOR OF ENGINEERING" not in x , splited))
# year=list(filter(lambda x: "2023" in x, splited))
# print("year:", year)
# print(filtered)

parts = [part.strip() for part in s.split(",")]
# print("parts:", parts)



#test download_paper function
import os,requests
from index import headers
def download_paper(link, subject, month, year,path):

    response = requests.get(link, stream=True,headers=headers)
    print(subject, month, year)
    filename = f"{str(subject)}_{str(month)}_{str(year)}.pdf"
    filename = filename.replace(' ', '_').replace('/', '_')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)

    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Saved: {filepath}")
    else:
        print(f"Failed to download {link}: HTTP {response.status_code}")


download_paper("https://ksv.ac.in/paper/upload/Exams/Papers/1706340113.pdf", "ME605-N-E IOT & SMART MANUFACTURING", "December", "2023", "Exam_Papers/Papers")