from termcolor import colored

from utils import get_user_data, update_scorecard, get_normalised_scorecard


def main():
	usernames = []
	team_scorecard = {}
	print "Enter the usernames of your team-members:"

	while True:
		user_input = raw_input().lower()
		if not user_input:
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
		else:
			usernames.append(user_input)

	print team_scorecard
	print get_normalised_scorecard(team_scorecard)

if __name__ == '__main__':
	main()
