import pickle, pandas

data = pickle.load(open("fiscal_note_raw_data_full.txt"))

states = {}

state_left = {}

count = 0

years = {}

for index, datum in enumerate(data):
	date = pandas.to_datetime(datum["bill_action_dates"]["introduced"])
	try:
		if date.year in years:
			years[date.year] += 1
		else:
			years[date.year] = 1
	except AttributeError:
		pass			

# 			count += 1
# 			try:
# 				print(date.year)
# 			except:
# 				print date

# 			if index == 0:
# 				#print(pandas.to_datetime(datum["bill_action_dates"]["introduced"]))
# 				pass
# 			if datum["state"] in states:
# 				states[datum["state"]] += 1
# 			else:
# 				states[datum["state"]] = 1

# 			if datum["state"] in state_left:
# 				state_left[datum["state"]] += datum["political"][0]["Liberal"] - datum["political"][0]["Conservative"]
# 			else:
# 				#print(datum["political"][0]["Liberal"])
# 				state_left[datum["state"]] = datum["political"][0]["Liberal"] - datum["political"][0]["Conservative"]
# print count
# print states
# print state_left

# for state in state_left:
# 	state_left[state] = state_left[state]/states[state]

# print(state_left)

print years