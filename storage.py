from datetime import datetime, timedelta

class PaperStorage:
    def __init__(self):
        self.papers = []

    def add_paper(self, paper):
        # Add date_added using local get_yesterday_date function
        paper['date_added'] = self.get_yesterday_date()
        # Check if paper with same URL already exists
        if not any(p['url'] == paper['url'] for p in self.papers):
            self.papers.append(paper)

    def get_all_papers(self):
        return self.papers

    @staticmethod
    def get_yesterday_date():
        """Get yesterday's date in YYYY-MM-DD format"""
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d') 