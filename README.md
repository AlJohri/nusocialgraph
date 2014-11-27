Usage
```
workon nusocialgraph

# several points of entry
	python -i models.py
	psql nusocialgraph
	python -i network.py
```

Setup
```
mkvirtualenv nusocialgraph
pip install -r requirements.txt

# Fix Matplotlib Backend for Mac OS (set to qt4agg)
# http://matplotlib.org/users/customizing.html
# matplotlib.matplotlib_fname() => /Users/`whoami`/.virtualenvs/nusocialgraph/lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc

# install pyside

createdb nusocialgraph
pg_restore -Fc -d nusocialgraph latest.dump.bak
```

Restore Database
```
wget https://s3.amazonaws.com/al-johri/latest.dump.bak
dropdb nusocialgraph; createdb nusocialgraph
pg_restore -Fc -d nusocialgraph latest.dump.bak
```

Random Instructions and Links
```
brew install graphviz
brew install igraph
http://stackoverflow.com/a/16166290/1667241
export PKG_CONFIG_PATH=/opt/X11/lib/pkgconfig:$PKG_CONFIG_PATH
https://github.com/yyuu/pyenv/issues/16#issuecomment-17818298
http://cairographics.org/pycairo/
http://stackoverflow.com/a/25903802/1667241
```