import urllib
import requests


#Check the if the server has "files"
def checking(url):
	#url = link
	for i in files:
		response = requests.get(url + "/" + i)
			
		if response.status_code == 200:
			print(i, "\n")

	response.close()


if __name__ == "__main__":
	
	#Dictionary with common files
	files = ["index.html", "index.php", "login.php", "wp-login.php" "wp-content.php"]

	print("Enter the url mamahuevo :/ ")

	#Store the url (input)
	link = input()

	#Call to the funcion
	checking(link)

