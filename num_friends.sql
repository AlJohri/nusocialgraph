WITH facebook_friends_complete AS (
	WITH facebook_friends_reverse AS (SELECT uid1 AS uid2, uid2 AS uid1 FROM facebook_friends)
		SELECT uid1, uid2 FROM facebook_friends UNION SELECT ffr.uid1, ffr.uid2 FROM facebook_friends_reverse ffr)
SELECT ffc.uid1 AS uid, fu.name, COUNT(*) AS num_friends FROM facebook_friends_complete ffc
INNER JOIN facebook_users fu ON fu.uid = ffc.uid1
GROUP BY ffc.uid1, fu.name ORDER BY num_friends DESC;