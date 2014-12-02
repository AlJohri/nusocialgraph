SELECT fu.uid, fu.name FROM facebook_users fu
	JOIN facebook_groups_users gu ON fu.uid = gu.uid
	JOIN facebook_groups fg ON gu.group_id = fg.group_id
	WHERE fg.group_id IN (358721727508091, 358801190833478, 358739847506279, 617557238291204, 364881846892079, 358772894169641, 358728617507402, 359395334107397);