from utils import get_user_data, get_normalised_scorecard, store_score_card

# username = raw_input("username:")
username = "prabhakar267"
x = get_user_data(username, {})
# print x
store_score_card(username, x)
print get_normalised_scorecard(x)
