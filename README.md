# godinez
Software to index issues resolved and to learn develop with python

**Install DB**
    <li>https://www.mongodb.com/download-center#community</li>
    <li>`config.py` - comments mode dev/production</li>

**Mode DEV (Server)**
	Into root forder :
	<li><code>pip install virtualenv</code></li>
	<li><code>virtualenv venv</code></li>
 	<li><code>source ./venv/bin/activate</code></li>
	<li><code>pip install -r requirements.txt</code></li>
  	<li><code>yarn install</code></li>

    When install new dependencies, save to file after of install:
    <li><code>pip freeze > requirements.txt</code></li>

**Init server**

	python run.py

**Mode DEV (Web)**
	Into web forder :
  	<li><code>yarn install</code></li>

**Access**

	http://localhost:5000
	http://localhost:5000/find -> return json list

**Resolved Issues**

	Problem: heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/"
	Fix: heroku ps:scale web=1 --app godinez