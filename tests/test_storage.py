import unittest
from datetime import datetime, timedelta
from storage import PaperStorage

class TestPaperStorage(unittest.TestCase):
    """Test cases for paper storage functionality"""

    def setUp(self):
        self.storage = PaperStorage()

    def test_add_paper(self):
        # Test adding a new paper
        paper = {
            'title': 'Test Paper',
            'url': 'https://test.com/paper1'
        }
        self.storage.add_paper(paper)
        self.assertEqual(len(self.storage.papers), 1)

    def test_duplicate_paper(self):
        # Test adding duplicate paper
        paper = {
            'title': 'Test Paper',
            'url': 'https://test.com/paper1'
        }
        self.storage.add_paper(paper)
        self.storage.add_paper(paper)
        self.assertEqual(len(self.storage.papers), 1)

    def test_get_yesterday_date(self):
        # Test yesterday's date format
        yesterday = self.storage.get_yesterday_date()
        expected = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        self.assertEqual(yesterday, expected)

    def test_get_all_papers(self):
        # Test retrieving all papers
        papers = [
            {'title': 'Paper 1', 'url': 'https://test.com/1'},
            {'title': 'Paper 2', 'url': 'https://test.com/2'}
        ]
        for paper in papers:
            self.storage.add_paper(paper)
        
        all_papers = self.storage.get_all_papers()
        self.assertEqual(len(all_papers), 2) 