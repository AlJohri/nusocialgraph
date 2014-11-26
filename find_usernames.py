from models import Session, FacebookUser, FacebookPage, FacebookGroup
from lib import get_scraper, save_user, save_page

import logging
logging.basicConfig(level=logging.DEBUG)
session = Session()
scraper = get_scraper(True)

for user in session.query(FacebookUser).filter(FacebookUser.data=="todo").filter("username ~ '^\d+$'").all():
	user.username = scraper.get_username_api(str(user.uid)) or str(user.uid)
	print user.uid, user.username
	session.commit()