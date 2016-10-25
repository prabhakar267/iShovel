import json
import requests
import os.path
import datetime
from time import strftime

from credentials import username as master_username, password as master_password
from constants import GITHUB_API_URL, USERS_API


res_path = "res/"


def get_user_data(username, scorecard={}):
	user_history = check_hist(username)
	if user_history:
		return user_history

	# get new user data
	try:
		url = GITHUB_API_URL + USERS_API + username + "/repos?per_page=100&type=all"
		response = requests.get(url, auth=(master_username, master_password))

		if "message" in response.json():
			raise Exception("API Limit exceeded") 
		
		repo_check_list = list()

		ctr = 1
		for repo in response.json():
			if not repo['fork']:
				repo_check_list.append(repo['languages_url'])

		for repo_url in repo_check_list:
			print repo_url
			repo_response = requests.get(repo_url, auth=(master_username, master_password))
			language_json = repo_response.json()

			if "message" in language_json:
				raise Exception("API Limit exceeded") 

			for language in language_json.keys():
				scorecard = update_lang_score(scorecard, language, language_json[language])

		# store updated data
		store_score_card(username, scorecard)
		return scorecard
	except requests.exceptions.ConnectionError:
		print "Internet connection not found!"
	except Exception, e:
		print e


def update_lang_score(scorecard, lang, score):
	if lang in scorecard.keys():
		scorecard[lang] += score
	else:
		scorecard[lang] = score

	return scorecard


def store_score_card(username, scorecard):
	data = {
		"cur_time" : strftime("%Y-%m-%d %H:%M:%S"),
		"scorecard" : scorecard,
	}

	fname = res_path + username
	with open(fname, 'w') as outfile:
		json.dump(data, outfile)


def check_hist(username):
	fname = res_path + username

	if os.path.isfile(fname):
		with open(fname) as outfile:
			data = json.load(outfile)

		data_expiry = datetime.datetime.now() - datetime.timedelta(days=7)
		data_expiry_string = data_expiry.strftime("%Y-%m-%d %H:%M:%S")

		if data_expiry_string < data['cur_time']:
			# data not older than 1 week, use this data
			return data['scorecard']

	return False

def get_normalised_scorecard(scorecard):
	normalised_scorecard = {}
	score_sum = sum(scorecard.values())

	for lang in scorecard.keys():
		normalised_scorecard[lang] = float(scorecard[lang]) / score_sum * 100
	return normalised_scorecard

def update_scorecard(parent_scorecard, child_scorecard):
	for key in child_scorecard.keys():
		if key in parent_scorecard.keys():
			parent_scorecard[key] += child_scorecard[key]
		else:
			parent_scorecard[key] = child_scorecard[key]
	return parent_scorecard
