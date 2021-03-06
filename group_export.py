import json
import csv

from facebook import GraphAPI, GraphAPIError
from socialscraper.facebook import graphapi

from models import Session, FacebookUser, FacebookGroup
from lib import save_user, save_group

session = Session()

with open("group_export.csv", "w") as f:
	writer = csv.writer(f)

	writer.writerow(['id', 'name', '#', 'privacy', 'normalized name', 'parent'])

	for group in session.query(FacebookGroup).all():
		
		supergroup_name = group.supergroup.name if group.supergroup else ""
		supergroup_parent_name = group.supergroup.parents[0].name if group.supergroup and group.supergroup.parents else ""

		row = [group.group_id, group.name.encode('utf-8'), len(group.users), group.privacy, supergroup_name, supergroup_parent_name]
		print row
		writer.writerow(row)