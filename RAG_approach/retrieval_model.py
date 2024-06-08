import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

class RetrievalModel:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.google_search_url = 'https://www.google.com/search?q='

    def search_online(self, query):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(self.google_search_url + query, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        snippets = []
        for span in soup.find_all('span', class_='aCOpRe'):
            snippet_text = span.get_text()
            if snippet_text:
                snippets.append(snippet_text)
        
        if not snippets:
            for div in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
                snippet_text = div.get_text()
                if snippet_text:
                    snippets.append(snippet_text)
        
        if not snippets:
            for span in soup.find_all('span'):
                snippet_text = span.get_text()
                if snippet_text:
                    snippets.append(snippet_text)

        return snippets

    def enrich_with_retrieval(self, extracted_data):
        enriched_data = []
        for item in extracted_data:
            query = item['text']
            snippets = self.search_online(query)
            context = snippets[0] if snippets else 'Context not available.'
            item['retrieved_context'] = context
            enriched_data.append(item)
        return enriched_data
