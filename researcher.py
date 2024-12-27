import requests
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import re
from ai_model import generate_text
def clean_title(title):
    """Clean and format paper title"""
    # Remove extra whitespace and newlines
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def extract_paper_titles(url):
    """
    Extract paper titles and URLs from HuggingFace papers page
    
    Args:
        url (str): URL to fetch papers from
        
    Returns:
        list: List of dictionaries containing paper information
    """
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Print status code and URL for debugging
        print(f"Response status: {response.status_code}")
        print(f"Final URL: {response.url}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        papers = []
        
        # Try different selectors
        paper_entries = (
            soup.find_all('article') or 
            soup.find_all('div', class_='paper-card') or
            soup.find_all('div', class_='paper') or
            soup.find_all('div', {'data-test': 'paper-card'})
        )
        
        print(f"Found {len(paper_entries)} potential paper entries")
        
        for entry in paper_entries:
            try:
                # Try different title selectors
                title_elem = (
                    entry.find(['h3', 'h4']) or
                    entry.find(class_='paper-title') or
                    entry.find('a', class_='paper-link')
                )
                
                if not title_elem:
                    continue
                
                paper_title = clean_title(title_elem.text)
                if not paper_title or paper_title.startswith('Submitted'):
                    continue
                
                # Get paper URL
                paper_url = url
                link_elem = (
                    title_elem.find('a', href=True) or
                    title_elem.parent.find('a', href=True) or
                    entry.find('a', href=True)
                )
                
                if link_elem and link_elem.get('href'):
                    href = link_elem['href']
                    if href.startswith('http'):
                        paper_url = href
                    else:
                        paper_url = f"https://huggingface.co{href}"
                
                # Only add papers with valid titles and URLs
                if paper_title and paper_url != url:
                    # Generate summary for the paper
                    summary = generate_paper_summary(paper_title, paper_url)
                    
                    papers.append({
                        'title': paper_title,
                        'url': paper_url,
                        'summary': summary
                    })
                    print(f"Added paper: {paper_title[:50]}...")
            
            except Exception as e:
                print(f"Error processing entry: {e}")
                continue
        
        # Debug information
        if not papers:
            print("\nDebug Information:")
            print("Page title:", soup.title.string if soup.title else "No title found")
            print("\nFirst 1000 characters of HTML:")
            print(soup.prettify()[:1000])
            
        return papers
    
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []

def generate_paper_summary(paper_title, paper_url):
    """Generate a summary of a paper"""
    prompt = f"Generate a summary of the following paper using its title and restrict to 200 charactors or less{paper_title} - {paper_url}"
    return generate_text(prompt)


def get_yesterday_date():
    """Get yesterday's date in YYYY-MM-DD format"""
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

def main():
    """
    Test function to verify paper extraction
    """
    url = f"https://huggingface.co/papers?date={get_yesterday_date()}"
    print(f"Fetching papers from: {url}")
    
    papers = extract_paper_titles(url)
    print(f"\nFound {len(papers)} papers:")
    
    for i, paper in enumerate(papers, 1):
        print(f"\n{i}. Paper Details:")
        print(f"Title: {paper['title']}")
        print(f"URL: {paper['url']}")

if __name__ == "__main__":
    main()