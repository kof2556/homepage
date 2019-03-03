


pages={}

def mk_pages():
    pages.append({
        "filename": "content/first.html",
        "title": "Index",
        "output": "docs/index.html",
        })


def main():
    print("In main")
    list_of_pages= []
    for page in list_of_pages:
          title= page['title']
          filename= page['filename']
          output= page['output']
          base= assign_base(title)
          assemble_page(title, base, filename, output)
          page_title (title, output)  
          print(page)

#file_path = ("content.first.html" + "content.blog.html" + "content.projects.html" + "content.about.html")
#file_name = os.path.basename(file_path)
#print(file_name)
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


if __name__ == '__main__':
    main()
    
