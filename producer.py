from redis import Redis
from rq import Queue
from models import Session, FacebookUser, FacebookPage, FacebookGroup

session = Session()

q = Queue(connection=Redis())

from get_friends import get_friends

# incomplete_students = session.query(FacebookUser).filter(FacebookUser.data=="in progress").all()
todo_students = session.query(FacebookUser).filter(FacebookUser.data=="todo").filter("username ~ '[a-zA-Z]+'").all()

# session.query(FacebookUser).filter("username ~ '^\d+$'").count()
# session.query(FacebookUser).filter("username ~ '[a-zA-Z]+'").count()

print "Grabbing friends of %s fans" % len(todo_students)
for i, student in enumerate(todo_students):
	# result = q.enqueue(get_friends, student.username) # default timeout is 180 seconds
	result = q.enqueue_call(func=get_friends, args=(student.username,), timeout=3600)