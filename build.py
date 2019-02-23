
def main():
    content = open('docs/index.html')
    resulting



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
        def apply_template(content):
           template = open("templates/base.html").read()
        return results
        def main()
           content = open(page["filename"]).read()
           resulting_html_for_index = apply_template(content)
        
        finished_page = template.replace("{{content}}", content)
        open(page["output"], "w+").write(finished_page)
        
     
        print('done')
   
if __name__ == "__main__":
    main()   
  

