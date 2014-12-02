WITH greek_facebook_groups AS (
	SELECT fg.group_id, fg.name, sg.name, sgg.child_id FROM supergroupsgroups sgg
	INNER JOIN supergroups sg ON sg.id = sgg.child_id
	INNER JOIN facebook_groups fg ON fg.supergroup_id = sg.id
	WHERE sgg.parent_id = 21)
SELECT fu.uid, fu.name FROM facebook_users fu
	JOIN facebook_groups_users gu ON fu.uid = gu.uid
	JOIN facebook_groups fg ON gu.group_id = fg.group_id
	WHERE fg.group_id IN (SELECT group_id FROM greek_facebook_groups);