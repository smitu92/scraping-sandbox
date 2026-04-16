# import requests

# url = 'https://example.com'
# response = requests.get(url)

# # Always check if the request was successful
# if response.status_code == 200:
#     with open('local_filename.zip', 'wb') as f:
#         f.write(response.content)


# with requests.get(url, stream=True) as r:
#     r.raise_for_status()
#     with open('large_file.zip', 'wb') as f:
#         for chunk in r.iter_content(chunk_size=8192): 
#             f.write(chunk)
