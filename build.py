import glob
import os 

pages = []


def main():
    all_html_files = glob.glob("content/*.html")
    print(all_html_files)
    
    for each in all_html_files:
        file_path = each
        file_name = os.path.basename(file_path)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only)
        pages.append({
            'filename': file_path,
            'title': name_only,
            'output': 'docs/' + file_name,
            })
    print(pages)
# replacing all title templates with Homepage
    for page in pages:
       from jinja2 import Template
       index_html = open("content/index.html").read()
       template_html = open("templates/base.html").read()
       template = Template(template_html)
       finished_page = template.render(
            title="Homepage",
            content=index_html,
        )
       open(page["output"], "w+").write(finished_page)
       print('goodbye')
       {% for page in pages %}
       
        
if __name__ == "__main__":
    main()
    
