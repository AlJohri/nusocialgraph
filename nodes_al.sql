WITH user_friends AS (
        SELECT uid1, uid2 FROM facebook_friends ff
		LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid
		LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid
		WHERE (uid1 = 100000862956701 OR uid2 = 100000862956701)
     ),
     user_distinct_friends AS (
      SELECT DISTINCT(uid1) AS uid FROM user_friends UNION SELECT DISTINCT(uid2) FROM user_friends
     )
SELECT udf.uid AS id, fu.name AS label FROM user_distinct_friends udf INNER JOIN facebook_users fu ON fu.uid=udf.uid WHERE udf.uid != 100000862956701;