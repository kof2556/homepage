
nola = open('templates/top.html').read()
saints = open('content/index.html').read()
pelicans = open('templates/bottom.html').read()

print(nola + saints + pelicans)

