import requests
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import re
from ai_model import generate_text
from storage import PaperStorage

def clean_title(title):
    """Clean and format paper title"""
    # Remove extra whitespace and newlines
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def extract_paper_titles(url):
    """Extract paper titles and URLs from HuggingFace papers page"""
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        papers = []
        
        # Try different selectors
        paper_entries = (
            soup.find_all('article') or 
            soup.find_all('div', class_='paper-card') or
            soup.find_all('div', class_='paper')
        )
        
        for entry in paper_entries:
            try:
                title_elem = entry.find(['h3', 'h4']) or entry.find(class_='paper-title')
                if not title_elem:
                    continue
                
                paper_title = clean_title(title_elem.text)
                if not paper_title:
                    continue
                
                # Get paper URL
                paper_url = url
                link_elem = title_elem.find('a', href=True) or title_elem.parent.find('a', href=True)
                if link_elem and link_elem.get('href'):
                    paper_url = f"https://huggingface.co{link_elem['href']}"
                
                # Generate summary for the paper
                summary = generate_paper_summary(paper_title, paper_url)
                
                papers.append({
                    'title': paper_title,
                    'url': paper_url,
                    'summary': summary
                })
            
            except Exception as e:
                print(f"Error processing entry: {e}")
                continue
        
        return papers
    
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []

def generate_paper_summary(paper_title, paper_url):
    """Generate a summary of a paper"""
    prompt = f"Generate a summary of the following paper using its title and restrict to 200 charactors or less{paper_title} - {paper_url}"
    return generate_text(prompt)

def main():
    """Test function to verify paper extraction"""
    storage = PaperStorage()
    url = f"https://huggingface.co/papers?date={storage.get_yesterday_date()}"
    print(f"Fetching papers from: {url}")
    
    papers = extract_paper_titles(url)
    print(f"\nFound {len(papers)} papers:")
    
    for i, paper in enumerate(papers, 1):
        print(f"\n{i}. Paper Details:")
        print(f"Title: {paper['title']}")
        print(f"URL: {paper['url']}")

if __name__ == "__main__":
    main()