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

    When install new dependencies, save to file after of install:
    <li><code>pip freeze > requirements.txt</code></li>

**Mode DEV (Web)**
	Into web forder :
  <li><code>yarn install</code></li>

**Init server**

	python run.py

**API**

    Issue Model to POST and PUT:
        {
            "title": "I have a problem",
            "description": "Help please!!!"
        }

	http://localhost:5000/ [GET]
	    Return APP Index

	http://localhost:5000/issues [GET]
	    Return Array
            {
                "data":[
                    {
                        "title": "aaaa",
                        "description": "bbbb"
                    },
                    ...
                ]
            }

	http://localhost:5000/issues [POST]
	    Send Object

	    Return Object Saved
            {
                "title": "aaaa",
                "description": "bbbb"
            }

    http://localhost:5000/issues/597bff623d01c55f66a10577 [DELETE]
        Send ID
        Return Object
            {
                "message": "Issue delatada com sucesso"
            }

	http://localhost:5000/issues [PUT]
	    Send Object
	        {
                "_id": "597c09093d01c56671841402",
                "title": "I have other probleasasdm",
                "description": "ffff"
            }
	    Return Object
	        {
                "message": "Issue atualizada com sucesso"
            }


**Resolved Issues**

	Problem: heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/"
	Fix: heroku ps:scale web=1 --app godinez