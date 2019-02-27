


def build_page(page_data):    
    template = open("templates/base.html").read()
    content = open(page_data["filename"]).read()
    return template.replace("{{content}}", content)
    
def write_page(page, finished_page):
    open(page["output"], "w+").write(finished_page)
    


def main():
      


    pages = [
       
    ]
    for page in pages:
        finished_page = build_page(page)
        write_page(page, finished_page)
import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

pages = []
pages.append({
"filename": "content/index.html",
"title": "Index",
"output": "docs/index.html",
})
print(pages)
         
if __name__ == "__main__":
    main()   
