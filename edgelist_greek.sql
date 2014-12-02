WITH greek_facebook_users AS (
	WITH greek_facebook_groups AS (
		SELECT fg.group_id, fg.name, sg.name, sgg.child_id FROM supergroupsgroups sgg
			INNER JOIN supergroups sg ON sg.id = sgg.child_id
			INNER JOIN facebook_groups fg ON fg.supergroup_id = sg.id
			WHERE sgg.parent_id = 21)
	SELECT fu.uid, fu.name FROM facebook_users fu
		JOIN facebook_groups_users gu ON fu.uid = gu.uid
		JOIN facebook_groups fg ON gu.group_id = fg.group_id
		WHERE fg.group_id IN (SELECT group_id FROM greek_facebook_groups))
SELECT uid1 AS source, uid2 AS target
	FROM facebook_friends ff
	LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid
	LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid
	WHERE fu1.nu=1 AND fu2.nu=1 AND (uid1 IN (SELECT uid FROM greek_facebook_users) AND uid2 IN (SELECT uid FROM greek_facebook_users));