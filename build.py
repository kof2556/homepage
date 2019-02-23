
def main():
    #template = open("base.html").read()
    #index_content = open("content/index.html").read()
    #finished_index_page = template.replace("{{content}}", index_content)
    #open("docs/index.html", "w+").write(finished_index_page)
    #top = open('templates/top.html').read()
    #center = open('content/index.html').read()
    #bottom = open('templates/bottom.html').read()
    #print(top + center + bottom)




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
        template = open("templates/base.html").read()
        content = open(page["filename"]).read()
        finished_page = template.replace("{{content}}", content)
        open(page["output"], "w+").write(finished_page)
        def recess(x):
            print("template/base.html" + x)
           
        recess("filename")
          
        
        

        
main()   
  

