import requests
from models import Session, FacebookUser, FacebookPage, FacebookGroup
from lib import get_scraper, save_user, save_page

import logging
logging.basicConfig(level=logging.DEBUG)

scraper = get_scraper()

def get_friends(username=None):

	session = Session()
	session.expire_on_commit = False

	fan = session.query(FacebookUser).filter(FacebookUser.username==username).first()

	print "Friends of %s" % fan.username

	fan.data = "in progress"
	session.commit()

	for result in scraper.get_friends_nograph(fan.username):
		print result
		current_user = save_user(result, session, log=False)
		fan.friend(current_user)
		print "\t-", fan.username, "is friends with", current_user.username
		session.commit()

	fan.data = "done"
	fan_friends_count = fan.friends.count()

	session.commit()
	session.close()

	return "downloaded %d friends for %s" % (fan_friends_count, fan.username)

# try:
# 	# requests.get('asdfasdf')
# except requests.exceptions.ConnectionError as e:
