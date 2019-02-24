def build_page(page_data):    
    template = open("templates/base.html").read()
    content = open(page_data["filename"]).read()
    return template.replace("{{content}}", content)
    
def write_page(page, finished_page):
    open(page["output"], "w+").write(finished_page)


def main():
   


    pages = [
        {
        "filename": "content/about.html",
        "output": "docs/about.html",  
        "title": "About Me", 
        },
        {
        "filename": "content/projects.html",
        "output": "docs/project.html",  
        "title": "Projects", 
        },
        {
        "filename": "content/blog.html",
        "output": "docs/blog.html",  
        "title": "Blog", 
        },
        {
        "filename": "content/first.html",
        "output": "docs/index.html",  
        "title": "Index", 
        },         
    ]
    for page in pages:
        finished_page = build_page(page)
        write_page(page, finished_page)
        
        print('done')
   
if __name__ == "__main__":
    main()   
