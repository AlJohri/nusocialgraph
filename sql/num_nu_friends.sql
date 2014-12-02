WITH facebook_friends_complete_nu AS (
	WITH facebook_friends_complete AS (
		WITH facebook_friends_reverse AS (SELECT uid1 AS uid2, uid2 AS uid1 FROM facebook_friends)
			SELECT uid1, uid2 FROM facebook_friends UNION SELECT ffr.uid1, ffr.uid2 FROM facebook_friends_reverse ffr)
	SELECT uid1, uid2, fu1.name FROM facebook_friends_complete ffc
	INNER JOIN facebook_users fu1 ON fu1.uid = ffc.uid1
	INNER JOIN facebook_users fu2 ON fu2.uid = ffc.uid2 
	WHERE fu1.nu = 1 AND fu2.nu = 1)
SELECT ffcnu.uid1 AS uid, ffcnu.name, COUNT(*) AS num_friends FROM facebook_friends_complete_nu ffcnu
GROUP BY ffcnu.uid1, ffcnu.name ORDER BY num_friends DESC;