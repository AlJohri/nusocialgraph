SELECT fu.uid, fu.name FROM facebook_users fu
	JOIN facebook_groups_users gu ON fu.uid = gu.uid
	JOIN facebook_groups fg ON gu.group_id = fg.group_id
	WHERE fg.name ILIKE '%Sigma Chi%';