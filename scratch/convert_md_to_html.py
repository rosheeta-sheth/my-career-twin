import glob
import os
import markdown

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background-color: #f9f9f9;
        }}
        .container {{
            background: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 0.5rem; }}
        h2 {{ color: #34495e; margin-top: 1.5rem; }}
        p {{ margin-bottom: 1rem; }}
        ul {{ padding-left: 1.5rem; }}
        li {{ margin-bottom: 0.5rem; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

base_dir = os.path.dirname(os.path.dirname(__file__))
md_files = glob.glob(os.path.join(base_dir, "detailed_projects", "*.md"))

for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    html_content = markdown.markdown(text)
    
    # Extract title from first line if possible
    title = os.path.basename(md_file).replace(".md", "").replace("_", " ").title()
    if text.startswith("# "):
        title = text.split("\n")[0].replace("# ", "").strip()
        
    final_html = html_template.format(title=title, content=html_content)
    
    html_file = md_file.replace(".md", ".html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Converted {os.path.basename(md_file)} to {os.path.basename(html_file)}")
