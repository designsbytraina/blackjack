import time
from random import choice

# welcome user

# rules
# dealer must hit if under 16
# dealer must not hit if 17 or over

# user can hit if they are under 21
# user wins if they did not bust and dealer loses
# user busts if over 21
# user loses if dealer score > user score

def deal_card():
	""""""
	card_values = {
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
		"10": 10,
		"jack": 10,
		"queen": 10,
		"king": 10,
		"ace": 1
	}

	random_card = choice(card_values.keys())
	points = card_values[random_card]

	return random_card, points

def play_round(dealer, user):
	"""Play a round of blackjack"""
	# tell user we are beginning round
	print "The round is starting"
	time.sleep(1)
	print ". . ."
	time.sleep(1)

	# time.sleep() and get an initial card for user
	# time.sleep() and get an initial card for dealer
	dealer_hand = 0
	user_hand = 0
	
	u_card_name, user_card = deal_card()

	if u_card_name != "ace":
		print "You have been dealt a {}".format(u_card_name)
	else:
		print "You have been dealt an {}".format(u_card_name)
	print "Your card is worth {} points".format(user_card)

	if user_card == 1 and user_hand <= 10:
		# print "Do you want your Ace to count as 1 or 11 points?"
		print "(this ace is worth 11 points)"
		user_card = 11

	user_curr_pts = user_card + user

	while user_curr_pts < 21:
		user_choice = raw_input("Would you like to hit? (y or n)").capitalize()
		if user_choice == "Y":
			n_card_name, next_card = deal_card()
			if u_card_name != "ace":
				print "You have been dealt a {}".format(n_card_name)
			else:
				print "You have been dealt an {}".format(n_card_name)
			print "Your card is worth {} points".format(next_card)
			user_curr_pts += next_card
			print "You currently have {} total points".format(user_curr_pts)
		elif user_choice == "N":
			print "You have stayed"
			break
		else:
			print "Please enter a valid response"

	if user_curr_pts > 21:
		print "You have busted!"
		print "You have a hand worth {} points".format(user_curr_pts)

	print "The dealer is now playing"
	time.sleep(1)

	d_card_name, dealer_card = deal_card()

	if d_card_name != "ace":
		print "Dealer has been dealt a {}".format(d_card_name)
	else:
		print "Dealer has been dealt an {}".format(d_card_name)
	print "Dealer's card is worth {} points".format(dealer_card)

	if dealer_card == 1 and dealer_hand <= 10:
		# print "Do you want your Ace to count as 1 or 11 points?"
		print "(this ace is worth 11 points)"
		dealer_card = 11

	dealer_curr_pts = dealer_card + dealer

	while dealer_curr_pts < 21:
		print ". . ."
		time.sleep(1)
		nd_card_name, next_dealer_card = deal_card()

		if nd_card_name != "ace":
			print "Dealer has been dealt a {}".format(nd_card_name)
		else:
			print "Dealer has been dealt an {}".format(nd_card_name)

		print "Dealer's card is worth {} points".format(next_dealer_card)
		dealer_curr_pts += next_dealer_card
		print "Dealer currently has {} total points".format(dealer_curr_pts)

		# if dealer_curr_pts < 16:
		# 	hit_me = choice([True, False])
		# 	if hit_me:
		# 		continue
		# 	else:
		# 		break
		# else:
		# 	continue

	if dealer_curr_pts > 21:
		print "Dealer has busted!"
		print "Dealer has a hand worth {} points".format(dealer_curr_pts)

	return dealer_curr_pts, user_curr_pts


def start_blackjack_repl():
	""""""
	rounds = 1

	while rounds <= 10:
		dealer_score = 0
		user_score = 0
		dealer_score, user_score = play_round(dealer_score, user_score)
		print "Great round! The total scores were: {} for you and {} for the house".format(user_score, dealer_score)
		
		if user_score < dealer_score:
			print "Congratulations! You won :)"
		elif user_score == dealer_score:
			print "Wow! The fates were in everyone's favor tonight. Congrats on the tie, but unfortunately the house always wins!"
		else:
			print "Better luck next time! Remember, the house always wins!"

		rounds += 1

	print "Game over!"


start_blackjack_repl()
