install: pip install -r requirements.txt 
run: python main.py 
freeze: python freeze > requirements.txt

# make install     # instead of: pip install -r requirements.txt
# make scrape      # instead of: scrapy crawl books -o output.csv
# make run