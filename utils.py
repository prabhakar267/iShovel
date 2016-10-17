import json
import requests
import os.path
from time import strftime

from credentials import username as master_username, password as master_password
from constants import GITHUB_API_URL, USERS_API


def get_user_data(username, scorecard):
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
	res_path = "res/"

	data = {
		"cur_time" : strftime("%Y-%m-%d %H:%M:%S"),
		"scorecard" : scorecard,
	}

	fname = res_path + username
	with open(fname, 'w') as outfile:
	    json.dump(data, outfile)


def get_normalised_scorecard(scorecard):
	normalised_scorecard = {}
	return normalised_scorecard
