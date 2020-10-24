"""
Short Exercises #3
"""

#Jake Underland

def find_candidates_from_city(candidates, office_loc):
	"""
	Given a list of candidates, construct a list of the candidate IDs
	for candidates with a campaign headquartered in the specified location.

	Inputs:
	  candidates: list of candidates
	  office_loc (string, string): a tuple of the form (city name, state abbreviation)

	Returns: list of candidate IDs (strings)
	"""

	### EXERCISE 1 -- Replace pass with your code
	candidate_ids = []
	x, y = office_loc

	for entry in candidates:
		if entry["City"] == x and entry["State"] == y:
			candidate_ids.append(entry["Candidate_ID"])
	
	return candidate_ids



def construct_dict_from_lists(keys, values):
	"""
	Given a list of keys and a list of values of equal length,
	construct a dictionary that maps the ith key to the ith value.

	Inputs:
	  keys: a list of (unique) immutable values (strings, ints, etc)
	  values: a list of values

	Returns: dictionary
	"""
	assert len(keys) == len(values)
	# check for repeats in the keys
	assert len(keys) == len(set(keys))

	### EXERCISE 2 -- Replace pass with your code
	d = {}
	for i, key in enumerate(keys):
		d[key] = values[i]
	
	return d


def construct_homestate_dict(candidates):
	"""
	Construct a dictionary that maps a candidate ID to the candidate's
	home state.

	Inputs:
	  candidates: list of candidates

	Returns: dictionary that maps each candidate id (string) to a state
	  abbreviation (string)
	"""

	### EXERCISE 3 -- Replace pass with your code
	d_id_state = {}
	for entry in candidates:
		id = entry["Candidate_ID"]
		state = entry["State"]
		d_id_state[id] = state
	
	return d_id_state


def find_unsuccessful_fund_raisers(cand_to_count, threshold):
	"""
	Given a dictionary that maps candidate IDs to the number
	of donations received by the campaigns, compute a
	list of the candidates who have received strictly fewer than
	the threshold number of contributions.

	Inputs:
	  cand_to_count: dictionary that maps Candidate IDs to integers
	  threshold (int): the threshold for labelling a candidate as a unsuccessful.

	Returns: list of Candidate IDs.
	"""
	### EXERCISE 4 -- Replace pass with your code
	d = {key: cand_to_count[key] for key in cand_to_count.keys() if cand_to_count[key] < threshold}
	lst = []
	for key in d.keys():
		lst.append(key)

	return lst


def construct_cands_by_state(candidates):
	"""
	Construct a mapping from states to the candidates from that state.

	Inputs:
	  candidates: list of candidate dictionaries

	Returns: dictionary that maps a state abbreviation (string) to a
	 list of dictionaries for candidates from that state.
	"""

	### EXERCISE 5 -- Replace pass with your code
	
	d = {}
	for entry in candidates:
		state = entry["State"] 
		if state not in d:
			candidates_per_state = [entry]
			d[state] = candidates_per_state
		else:
			d[state].append(entry)

	return d



