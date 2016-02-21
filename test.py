import requests, indicoio, pickle

total_responses = []

for p in range(150):
	params = {
		"apikey" : "PAXCY03JG4B4QZ0Z",
		"q" : "*",
		"count" : 100,
		"page" : p,
		"view" : "full"
	}

	resp = requests.get("https://api.fiscalnote.com/bills", params=params).json()
	for response in resp:
		try:
			political = indicoio.political(response["description"], api_key="df43365f5a827d884eb683b836fcb78a"), response["title"]
			#print response["title"]
			response["political"] = political
			total_responses += [response]
			if len(total_responses) % 100 == 0:
				print(len(total_responses))
		except:
			pass

print(len(total_responses))

pickle.dump(total_responses, open("fiscal_note_raw_data_full.txt", "w+"))