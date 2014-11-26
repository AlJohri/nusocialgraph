```
# http://postgresguide.com/utilities/backup-restore.html
psql -d nusocialgraph -c "SELECT uid1, uid2 FROM facebook_friends" -o 'edgelist.csv' -F ',' -A --pset footer
psql -d nusocialgraph -c "SELECT name, uid, nu FROM facebook_users" -o 'users.csv' -F ',' -A --pset footer

SELECT COUNT(*) FROM facebook_users;

SELECT ff.uid1, ff.uid2 from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid WHERE fu1.nu=1 AND fu2.nu=1;

SELECT COUNT(*) from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid WHERE fu1.nu=1 AND fu2.nu=1;

SELECT COUNT(DISTINCT(ff.uid1)) from facebook_friends ff LEFT OUTER JOIN facebook_users fu1 ON ff.uid1=fu1.uid LEFT OUTER JOIN facebook_users fu2 ON ff.uid2=fu2.uid WHERE fu1.nu=1 AND fu2.nu=1;
```

```
pg_restore -Fc -d nusocialgraph latest.dump.bak
```

```
brew install graphviz
```

```
nx.info()
	Name:
	Type: Graph
	Number of nodes: 1252220
	Number of edges: 2040134
	Average degree:   3.2584

pickle.dump(G, open("network.pickle", "wb"))
```

```
import matplotlib
matplotlib.matplotlib_fname()
# /Users/`whoami`/.virtualenvs/nusocialgraph/lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc
```

```
pip install -r requirements.txt
sublime /Users/`whoami`/.virtualenvs/nusocialgraph/lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc
```