from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<html>
<head><title>Sample Title</title></head>
<body>
    <h1>Heading 1</h1>
    <p>This is a <strong>sample</strong> paragraph.</p>
    <div class="content">
        <p>Another paragraph inside a div.</p>
    </div>
</body>
</html>
"""

# Parse the HTML and extract text
soup = BeautifulSoup(html_content, 'lxml')
text = soup.get_text()

print(text)
