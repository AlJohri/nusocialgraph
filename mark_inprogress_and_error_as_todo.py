from models import Session, FacebookUser, FacebookPage, FacebookGroup
from lib import get_scraper, save_user, save_page

import logging
logging.basicConfig(level=logging.DEBUG)
session = Session()
scraper = get_scraper()

for user in session.query(FacebookUser).filter(FacebookUser.data.like("in progress%")).all():
	user.data="todo"
	session.commit()

for user in session.query(FacebookUser).filter(FacebookUser.data.like("error%")).all():
	user.data="todo"
	session.commit()
