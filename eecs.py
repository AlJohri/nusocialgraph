from models import Session, FacebookUser

session = Session()

import csv
with open('eecs professors.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0] and row[1]: continue
        user = session.query(FacebookUser).filter_by(uid=row[1]).first()
        if not user:
            user = FacebookUser(uid=row[1], username=row[0], name=row[2])
            user.created_at = datetime.datetime.now()
            session.add(user)
            print user.name, "created"
        else:
            print user.name, "exists"
        user.data = "todo"
        user.nu = 1

session.commit()