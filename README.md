# godinez
Software to index issues resolved and to learn develop with python

**Mode DEV**
	Into forder of project `godinez`:
	<li><code>pip install virtualenv</code></li>
	<li><code>sudo virtualenv venv # it needs sudo to be installed</code></li>
 	<li><code>source ./venv/bin/activate</code></li>
	<li><code>pip install flask</code></li>
  	<li><code>pip freeze > requirements.txt</code></li>
  	<li><code>yarn install</code></li>

**Init server**

	python run.py

**Access**

	http://localhost:5000
	http://localhost:5000/find -> return json list

**Resolved Issues**

	Problem: heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/"
	Fix: heroku ps:scale web=1 --app godinez