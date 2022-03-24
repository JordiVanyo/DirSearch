#import requests
import readFile
import urllib

#Funcio per a llegir directoris
def readDir(url):
    link = url
    directoriesAll = open("arxiusComuns.txt")
    for i, j in enumerate(directoriesAll):
        directories = directoriesAll.readline()
        #print("Dir num ", i, " es " + directories)
        checking(url, directories)
        i = i + 1
    
    directoriesAll.close()

#Comprovar que la web conte "files"
def checking(link, dir):
	#for i in directories:
	response = requests.get(link + "/" + dir)
			
	if response.status_code == 200:
		print(i, "\n")

	response.close()
