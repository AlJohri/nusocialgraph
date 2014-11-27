nodes.csv:
	psql -d nusocialgraph -c "SELECT uid, name, username FROM facebook_users WHERE nu=1 LIMIT 1;" -o 'nodes.csv' -F ',' -A --pset footer

edgelist_user.txt:
	psql -d nusocialgraph -c "`cat user_friends_query.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_all.txt:
	psql -d nusocialgraph -c "SELECT ff.uid1, ff.uid2 from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid WHERE fu1.nu=1 AND fu2.nu=1;" -o '$@' -F ' ' -A --pset footer --pset tuples_only