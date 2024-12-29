import unittest
from unittest.mock import patch, MagicMock
from researcher import clean_title, extract_paper_titles, generate_paper_summary

class TestResearcher(unittest.TestCase):
    """Test cases for researcher functionality"""

    def test_clean_title(self):
        # Test title cleaning
        dirty_title = "  Test   Title\nWith\tSpaces  "
        clean = clean_title(dirty_title)
        self.assertEqual(clean, "Test Title With Spaces")

    @patch('researcher.requests.get')
    def test_extract_paper_titles(self, mock_get):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.content = """
        <html>
            <article>
                <h3><a href="/paper1">Test Paper 1</a></h3>
            </article>
            <article>
                <h3><a href="/paper2">Test Paper 2</a></h3>
            </article>
        </html>
        """
        mock_get.return_value = mock_response
        
        papers = extract_paper_titles("https://test.com")
        self.assertEqual(len(papers), 2)
        self.assertEqual(papers[0]['title'], "Test Paper 1")

    @patch('researcher.generate_text')
    def test_generate_paper_summary(self, mock_generate_text):
        # Test summary generation
        mock_generate_text.return_value = "Test summary"
        
        summary = generate_paper_summary("Test Paper", "https://test.com")
        self.assertEqual(summary, "Test summary") 