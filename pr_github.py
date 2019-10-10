import sys

print("This script exports github pr data to CSV file."
	+"\nProvide input through command line as \n\"$ python3 <github_token> <owner_name> <repo_name>\"")

if __name__== "__main__":
	#first argument is token, second and third are owner and repo name

	if len(sys.argv)>1:
		token = sys.argv[1]
		headers={"Accept":"application/vnd.github.v3+json", "Authorization":"token "+token}
	else:
		# token not given, so maximum request count per hour is 60
		headers={"Accept":"application/vnd.github.v3+json"}
	if len(sys.argv)>2:
		owner = sys.argv[2]
		repo_name = argv[3]
	else:
		#default owner and repo name
		owner = 'pandas-dev'
		repo_name = 'pandas'


	import json
	import requests

	request_number = 1;
	last10reqs = []

	base_url = 'https://api.github.com/repos/'+owner+'/'+repo_name+'/pulls?state=all&per_page=100&page='

	with open('outputFile.csv','w') as output_file:
		output_file.write('Title, user_login, user_id, closed_at, merged_at\n')
	try:
		while(True):
			print("getting page ",request_number)
			url = base_url+str(request_number)
			req = requests.get(url,headers=headers)
			received_data = req.json()
			if req.status_code !=200:
				print(received_data["message"])
				break

			if len(received_data)==0:
				break

			last10reqs.append(received_data)
			request_number+=1

			if request_number%10==0: #push output after every 10th request
				with open('outputFile.csv','a') as output_file:
					print("writing to output file")
					for stored_req in last10reqs:
						for data in stored_req:
							title = data['title'] if data['title']!=None else 'null'
							user_login = data['user']['login'] if data['user']['login']!=None else 'null'
							user_id = str(data['user']['id']) if data['user']['id']!=None else 'null'
							closed_at = data['closed_at'] if data['closed_at']!=None else 'null'
							merged_at = data['merged_at'] if data['merged_at']!=None else 'null'
							stringToWrite = '"'+title+'"'+',"'+ user_login+'","'+user_id+'","'+closed_at+'","'+merged_at+'"'
							output_file.write(stringToWrite+'\n')
				last10reqs = []

		with open('outputFile.csv','a') as output_file:
			print("writing to output file")
			for stored_req in last10reqs:
				for data in stored_req:
					title = data['title'] if data['title']!=None else 'null'
					user_login = data['user']['login'] if data['user']['login']!=None else 'null'
					user_id = str(data['user']['id']) if data['user']['id']!=None else 'null'
					closed_at = data['closed_at'] if data['closed_at']!=None else 'null'
					merged_at = data['merged_at'] if data['merged_at']!=None else 'null'
					stringToWrite = '"'+title+'"'+',"'+ user_login+'","'+user_id+'","'+closed_at+'","'+merged_at+'"'
					output_file.write(stringToWrite+'\n')
		print("Finished !!")

	except Exception as E:
		print("Exception",E)



