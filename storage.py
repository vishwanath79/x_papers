import json
import os

class PaperStorage:
    def __init__(self, filename='papers_database.json'):
        self.filename = filename
        self.papers = self._load_papers()

    def _load_papers(self):
        """Load papers from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_papers(self):
        """Save papers to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.papers, f, indent=2)

    def add_paper(self, paper):
        """Add a paper if it doesn't exist"""
        if not any(p['url'] == paper['url'] for p in self.papers):
            # Ensure paper has all required fields
            paper_data = {
                'title': paper['title'],
                'url': paper['url'],
                'summary': paper.get('summary', ''),  # Include summary if available
                'date_added': get_yesterday_date()
            }
            self.papers.append(paper_data)
            self.save_papers()
            return True
        return False

    def get_all_papers(self):
        """Get all papers"""
        return self.papers 