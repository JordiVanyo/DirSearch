import urllib
#import requests
import readFile


if __name__ == "__main__":
	
	#Dictionary with common files
	#files = ["index.html", "index.php", "login.php", "wp-login.php" "wp-content.php"]

	print("Introdueix la url:")

	#Guarda la url (input)
	link = input()

	readFile.readDir(link)

