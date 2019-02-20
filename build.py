
pages = []
def main():
    top = open('templates/top.html').read()
    center = open('content/index.html').read()
    bottom = open('templates/bottom.html').read()
    print(top + center + bottom)




pages = [
     {
        "filename": "content/about.html",
        "output": "docs/about.html",  
        "title": "About Me", 
    },
    {
        "filename": "content/projects.html",
        "output": "docs/about.html",  
        "title": "Projects", 
    },
    {
        "filename": "content/blog.html",
        "output": "docs/about.html",  
        "title": "Blog", 
    },
    {
        "filename": "content/index.html",
        "output": "docs/about.html",  
        "title": "Index", 
    }         
]
for page in pages:
    page_title = page['title']
    print(page_title)
   
if __name__ == "__main__":
    main()   
  


 


