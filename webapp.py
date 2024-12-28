import gradio as gr
import css_styles
from researcher import extract_paper_titles
from storage import PaperStorage
import time
import os
from gradio import Interface

# Initialize paper storage
paper_storage = PaperStorage()

def get_papers_list():
    """
    Fetch and format papers for display
    """
    # Use paper_storage's get_yesterday_date method
    yesterday = paper_storage.get_yesterday_date()
    url = f"https://huggingface.co/papers?date={yesterday}"
    new_papers = extract_paper_titles(url)
    
    # Add new papers to storage
    for paper in new_papers:
        paper_storage.add_paper(paper)
    
    # Format recent papers
    html_content = "<div class='container'>"
    
    # New papers section
    html_content += "<h1 class='section-title'>Latest AI Research Papers</h1>"
    html_content += "<div class='papers-list'>"
    for paper in new_papers:
        html_content += f"""
        <div class='paper-item'>
            <div class='paper-content'>
                <a href='{paper['url']}' class='title' target='_blank'>{paper['title']}</a>
                <div class='summary'>{paper.get('summary', '')}</div>
                <div class='meta'>
                    <span class='time'>{yesterday}</span> • 
                    <a href='{paper['url']}' class='view-link' target='_blank'>Read Paper</a>
                </div>
            </div>
        </div>
        """
    html_content += "</div>"
    
    # Older papers section
    html_content += """
    <div class='older-papers'>
        <h2>Research Archive</h2>
        <table class='papers-table'>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
    """
    
    # Add all papers from storage
    all_papers = paper_storage.get_all_papers()
    for paper in all_papers:
        html_content += f"""
            <tr>
                <td>{paper['title']}</td>
                <td>{yesterday}</td>
                <td><a href='{paper['url']}' target='_blank'>View Paper</a></td>
            </tr>
        """
    
    html_content += """
            </tbody>
        </table>
    </div>
    <div class='footer'>
        © 2025 <a href="https://vishsubramanian.me" target="_blank">vishsubramanian.me</a>
    </div>
    </div>
    """
    
    return html_content

def create_app():
    """
    Create and configure the Gradio interface
    """
    with gr.Blocks(css=css_styles.CUSTOM_CSS) as app:
        gr.HTML("""
            <div class='header'>
                <div class='logo'>
                    <a href='/'>AI Research</a>
                </div>
                <div class='nav'>

                    <a href='https://vishsubramanian.me/about/' target='_blank'>About</a>
                </div>
            </div>
        """)
        
        # Papers list container
        papers_html = gr.HTML(get_papers_list)
        
        # Refresh button (hidden but functional)
        refresh_btn = gr.Button("Refresh Papers", visible=False)
        refresh_btn.click(fn=get_papers_list, outputs=papers_html)
        
        # Auto-refresh every 5 minutes
        gr.HTML("""
            <script>
            setInterval(function() {
                document.querySelector('button[class*="refresh"]').click();
            }, 300000);
            </script>
        """)

    return app



if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    demo = create_app()
    demo.launch(server_name="0.0.0.0", 
               server_port=port,
               show_error=True,
               share=True) 