CUSTOM_CSS = """
/* Science News inspired CSS */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    font-size: 16px;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    color: #333;
}

.header {
    background-color: #005587;
    padding: 15px 20px;
    color: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.logo {
    display: inline-block;
    margin-right: 20px;
    font-weight: bold;
    font-size: 24px;
}

.logo a {
    color: white;
    text-decoration: none;
}

.nav {
    display: inline-block;
    margin-left: 20px;
}

.nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
    font-size: 16px;
    opacity: 0.9;
    padding: 5px 10px;
    border-radius: 4px;
    transition: all 0.2s ease;
}

.nav a:hover {
    opacity: 1;
    background-color: rgba(255, 255, 255, 0.1);
}

.nav a.active {
    background-color: rgba(255, 255, 255, 0.2);
    opacity: 1;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    color: #005587;
    margin: 30px 0 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #eee;
}

.papers-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

.paper-item {
    background: #fff;
    border: 1px solid #eee;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.paper-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.paper-content {
    padding: 20px;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
}

.title {
    color: #005587;
    text-decoration: none;
    font-size: 18px;
    font-weight: 600;
    line-height: 1.4;
    display: block;
    margin-bottom: 15px;
}

.title:hover {
    color: #0077be;
}

.meta {
    font-size: 14px;
    color: #666;
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #eee;
}

.meta a {
    color: #005587;
    text-decoration: none;
}

.meta a:hover {
    text-decoration: underline;
}

/* Archive section */
.older-papers {
    margin-top: 40px;
    background: #f8f8f8;
    padding: 30px;
    border-radius: 8px;
}

.older-papers h2 {
    color: #005587;
    font-size: 24px;
    margin-bottom: 20px;
}

.papers-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.papers-table th {
    background: #005587;
    color: white;
    font-weight: 500;
    text-align: left;
    padding: 15px;
}

.papers-table td {
    padding: 15px;
    border-bottom: 1px solid #eee;
}

.papers-table tr:last-child td {
    border-bottom: none;
}

.papers-table tr:hover {
    background-color: #f5f9fc;
}

/* Gradio customizations */
.gradio-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    background: white !important;
}

button.refresh {
    display: none !important;
}

.summary {
    font-size: 14px;
    color: #666;
    margin: 15px 0;
    line-height: 1.6;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.footer {
    margin-top: 40px;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #eee;
    color: #666;
    font-size: 14px;
}

.footer a {
    color: #005587;
    text-decoration: none;
    font-weight: 500;
}

.footer a:hover {
    text-decoration: underline;
}
""" 