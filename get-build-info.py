#import sys library
import sys

#import os library for file r/w transactions
import os

#import the json Library
import json

# importing the requests library 
import requests

#import GLOB for file operations
import glob

#defining my root API endpoint URI
my_api_endpoint = "http://<IP AND PORT INFO>/artifactory/"

#definng my Artifactory API Auth Key
my_art_auth_key = "<YOUR AUTH KEY>"

#defining my path root path where JARS will be saved
my_jar_location = "/var/<path to save artifact>"

def main(repo_match, match_name):
	# api-endpoint 
	build_list_URL = my_api_endpoint + "api/search/aql"

	# defining a params dict for the parameters to be sent to the API 
	P1='''items.find({"$and": [{"repo": {"$match":'''
	P2='''}}, {"name": {"$match":'''
	P3='''*.jar"}}]})'''
	PARAMS = P1 + '"' + repo_match + '"' + P2 + '"' +  match_name + P3
 
	# sending get request and saving the response as response object 
	r = requests.post(url = build_list_URL, data = PARAMS,  headers={"X-JFrog-Art-Api": my_art_auth_key})
	
	#check for the status code and take necessary actions
	if(r.status_code == 200):
		# extracting data in json format
		my_build_list_final = json.loads(r.content)

		#sorting data by filtering only results from the json data received
		data_to_sort = my_build_list_final['results']

		#extracting the latest build name based on the sorting of field CREATED in json data
		my_latest_build_data = sorted(data_to_sort,key=lambda i: i['created'], reverse=True)
		
		#print the latest data extracted
		print("DATA sorted and extracted is: ")
		print(my_latest_build_data[0])
		
		#extracting data from my_latest_build_data
		build_name_latest = my_latest_build_data[0]['name']
		build_repo_latest = my_latest_build_data[0]['repo']
		build_path_latest = my_latest_build_data[0]['path']
		
		print("FILE NAME: " + build_name_latest)
		#calling the "downloadJAR" def to download the latest JAR from Artifactory"
                downloadJAR(build_repo_latest,build_path_latest,build_name_latest)
	else:
		print("ERROR connecting to ARTIFACTORY. " + r.status_code + " is the error code. Reach out to your DEVOPS Admin")


# PART 1 COMPLETE - we get the latest name of the build

# PART 2 BEGINS  - we use this variable build_name_latest and download the jar from artifactory

def downloadJAR(build_repo,build_path,build_name):	
	build_path_split = build_path.split('/')
	#build the API Endpoint required to download the JAR
	dwnldJAR_URL = my_api_endpoint + build_repo + "/" + build_path + "/" + build_name
	
	#create a GET request to download the JAR
	r = requests.get(url = dwnldJAR_URL, headers={"X-JFrog-Art-Api": my_art_auth_key})

	#check for staus code and take necessary actions
	if(r.status_code == 200):		
		#we now reach to "/var/<PATH TO YOUR FILE>" folder and check if its repo folder already exists. Else, we create one and download our JAR there
 		art_jar_path = my_jar_location + build_path_split[0] + '/'
		print("FILE LOCATION: " + art_jar_path)

		# to check if the path exists 
		if not os.path.exists(art_jar_path):
			# to check if the script has write permissions on the path specified
    			if(os.access(my_jar_location,os.W_OK)):
				os.makedirs(art_jar_path)
				open(art_jar_path + build_name,'wb').write(r.content)
			else:
				print("ERROR: the script does not have permission to create new directory to save the downloaded JAR file. Please reach to your admin")
		else:
			#to check if the script has write permissions on the path specified
			if(os.access(art_jar_path, os.W_OK)):
				#clear out the existing contents from the folder
				if(empty_dir(art_jar_path)):
					open(art_jar_path + build_name,'wb').write(r.content)
				else:
					print("ERROR: failed to empty the directory. reach to admin")


def empty_dir(dir_to_empty):
	fileList = glob.glob(os.path.join(dir_to_empty, "*.*"))
	
	#loop through all files in the directory except sub folders and remove them
	for f in fileList:
		os.remove(f)
	return True


#main function invoking
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
