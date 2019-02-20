

def main():
   top = open('templates/top.html').read()
   center = open('content/index.html').read()
   bottom = open('templates/bottom.html').read()
   print(top + center + bottom)
   

if __name__ == "__main__":
    main()
