
# 🐍Python Deer.io search API
A simple implementation of API. Deer.io doesn't provide any API for developers, so that flask-server solves that problem.

It parse HTML-page and returns JSON object.

✅ Tested on Python **3.6.5**

## Params
**q**: [string] the query string

**outofstock**: [bool] if true returns "out of stock" items too.

# 🚀Installation
Create virtual environment.
```bash
virtualenv venv
```

Activate it. If you're on Linux type:
```bash
source venv/bin/activate
```
If Windows:
```
venv\scripts\activate
```

Then install requirements.
```bash
pip install -r requirements.txt
```

And... Run the server 🙂
```bash
python app.py
```

# 🤔Using
Open your browser at `http://localhost:8080/`, and provide a query: `https://localhost:8080/?q=twitter`.

The output should look like:
```json
{
    "shops": [
        {
            "id": 0,
            "title": "shop title",
            "link": "http://site.url/",
            "since": 1507161600,
            "description": "shop's description"
        }
    ],

    "items": [
        {
            "shop_id": 0,
            "title": "product's title",
            "count": 1234,
            "price": 11.0
        }
    ]
}
```

# 😊Thank you!
Have a nice day and thanks for spending time checking my repository.
