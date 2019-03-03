import glob
import os 

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



def main():
    for page in pages:
        template = open("templates/base.html").read()
        content = open(page["filename"]).read()
        finished_page = template.replace("{{content}}", content)
        open(page["output"], "w+").write(finished_page)
        

           
if __name__ == "__main__":
    main()
    
