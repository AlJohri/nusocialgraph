WITH greek_facebook_users AS (
	SELECT fu.uid, fu.name FROM facebook_users fu
		JOIN facebook_groups_users gu ON fu.uid = gu.uid
		JOIN facebook_groups fg ON gu.group_id = fg.group_id
		WHERE fg.group_id IN (358801190833478, 358739847506279, 617557238291204, 364881846892079, 358772894169641, 613203448726583, 790154174364842, 784111258302467, 407370042643259, 358782790835318, 452350961478500, 450603564986573))
SELECT uid1 AS source, uid2 AS target
	FROM facebook_friends ff
	LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid
	LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid
	WHERE fu1.nu=1 AND fu2.nu=1 AND (uid1 IN (SELECT uid FROM greek_facebook_users) AND uid2 IN (SELECT uid FROM greek_facebook_users));