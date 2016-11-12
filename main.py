import random
import ConfigParser
from termcolor import colored
from tabulate import tabulate
from collections import OrderedDict

from utils import get_user_data, update_scorecard, get_normalised_scorecard

config = ConfigParser.ConfigParser()
config.read("project.cfg")

def main():
	usernames = []
	team_scorecard = {}
	final_ans = {}

	print "Enter the usernames of your team-members:"

	while True:
		user_input = raw_input().lower()
		if user_input:
			usernames.append(user_input)
		else:
			if len(usernames) == 0:
				print colored("You did not enter any usernames. Try again!", "red")
				exit()
			else:
				for username in usernames:
					print colored("\tExtracting {0} profile".format(username), "green")
					user_scorecard = get_user_data(username)
					normalised_user_scorecard = get_normalised_scorecard(user_scorecard)

					team_scorecard = update_scorecard(team_scorecard, normalised_user_scorecard)
			break

	normalised_scorecard = get_normalised_scorecard(team_scorecard)
	# LANGUAGES = get_rand_languages()
	LANGUAGES = config.get("Languages", "seed").split("\n")
	IGNORE_LANGUAGES = config.get("Languages", "ignore").split("\n")

	for lang in team_scorecard:
		if lang not in LANGUAGES:
			LANGUAGES.append(lang)

	LANGUAGES = [lang for lang in LANGUAGES if lang not in IGNORE_LANGUAGES]

	score = [0] * len(LANGUAGES)

	i = 0
	COUNT = len(LANGUAGES) * 10000
	while i < COUNT:
	  	ctr = random.choice(LANGUAGES)
	  	score[LANGUAGES.index(ctr)] += 1
	  	i += 1


	ctr = 0
	for lang in LANGUAGES:
		normalisation = 1
		if lang in normalised_scorecard.keys():
			normalisation = normalised_scorecard[lang] + 1

		final_ans[lang] = score[ctr] * normalisation
		ctr += 1


	final_score_list = []
	od = OrderedDict(sorted(final_ans.items(), key=lambda(k,v):(v,k), reverse=True))

	language_total_score = sum(final_ans.values())
	for i in od:
		language_per_score = od[i] / language_total_score * 100
		final_score_list.append([i, language_per_score]);

	print_headers = ["Language", "Percentage Score"]
	print tabulate(final_score_list, headers= print_headers, tablefmt='orgtbl')


if __name__ == '__main__':
	main()
