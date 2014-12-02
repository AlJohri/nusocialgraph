edgelist_nu.txt:
	psql -d nusocialgraph -c "SELECT ff.uid1, ff.uid2 from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid WHERE fu1.nu=1 AND fu2.nu=1;" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_nu.txt:
	psql -d nusocialgraph -c "SELECT uid, name FROM facebook_users fu WHERE fu.nu = 1;" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_2015.txt:
	psql -d nusocialgraph -c "`cat edgelist_2015.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_2015.txt:
	psql -d nusocialgraph -c "`cat nodes_2015.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_cultural.txt:
	psql -d nusocialgraph -c "`cat edgelist_cultural.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_cultural.txt:
	psql -d nusocialgraph -c "`cat nodes_cultural.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_asian.txt:
	psql -d nusocialgraph -c "`cat edgelist_asian.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_asian.txt:
	psql -d nusocialgraph -c "`cat nodes_asian.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_eecs.txt:
	psql -d nusocialgraph -c "`cat edgelist_eecs.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_eecs.txt:
	psql -d nusocialgraph -c "`cat nodes_eecs.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_cs.txt:
	psql -d nusocialgraph -c "`cat edgelist_cs.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_cs.txt:
	psql -d nusocialgraph -c "`cat nodes_cs.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_al.txt:
	psql -d nusocialgraph -c "`cat edgelist_al.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_al.txt:
	psql -d nusocialgraph -c "`cat nodes_al.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_greek.txt:
	psql -d nusocialgraph -c "`cat edgelist_greek.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_greek.txt:
	psql -d nusocialgraph -c "`cat nodes_greek.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only

edgelist_residences.txt:
	psql -d nusocialgraph -c "`cat edgelist_residences.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only
nodes_residences.txt:
	psql -d nusocialgraph -c "`cat nodes_residences.sql`" -o '$@' -F ' ' -A --pset footer --pset tuples_only


num_friends.csv:
	psql -d nusocialgraph -c "`cat num_friends.sql`" -o '$@' -F ',' -A --pset footer --pset tuples_only
num_nu_friends.csv:
	psql -d nusocialgraph -c "`cat num_nu_friends.sql`" -o '$@' -F ',' -A --pset footer --pset tuples_only

edgelist_all.txt:
	psql -d nusocialgraph -c "SELECT ff.uid1, ff.uid2 from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid;" -o '$@' -F ' ' -A --pset footer --pset tuples_only
