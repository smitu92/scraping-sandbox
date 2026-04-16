# def get_all_papers(semester, year):
#     response = requests.get(url1.format(semester=semester, year=year),headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     papers=soup.find_all("a")
#     all_papers = []
#     for paper in papers:
#         link=paper["href"]
#         title, year, code, month, subject = clean_metadata(paper.get_text(), year)
#         all_papers.append({"Title": title, "Year": year, "Code": code, "Month": month, "Subject": subject, "Link": link})
#     return all_papers