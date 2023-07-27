# library-portal-jassim


# Flask Library

![img](https://raw.githubusercontent.com/UP2039019/library-portal-jassim/main/projeto/static/img/poster.jpg)

A simple library prototype using [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.1.x/).

## Features

- Create Books
- Search Books
- Delete Books
- Update Books
- Review Books
- User Registration & Login
- Account Info & Update

## TODO

- Create a table for Authors.
- Create the interface for Authors.

## Installation

### Clone the Repository

```
git clone https://github.com/UP2039019/library-portal-jassim.git
```

### Inside the Main Directory

Create a Virtual Environment:

```
python -m venv myvenv
```

Activate the Virtual Environment:

```
source myvenv/bin/activate
```

Install Requirements:

```
pip install -r requirements.txt
```

Run the Application:

```
python run.py
```

Open your Web Browser and navigate to `http://127.0.0.1:5000/`.

## Managing the Database

### Inside the Main Directory

Start a new [Python REPL](https://python.land/introduction-to-python/the-repl) in your terminal:

```
python
```

Creating a new database:

```python
>>> from projeto import db
>>> db.create_all()
```

Initiating a new app context:

```python
>>> from projeto import create_app
>>> app = create_app()
>>> app.app_context().push()
```

Importing the database models:

```python
>>> from projeto.models import User, Book, Analysis
```

Inserting a new user in the database:

```python
user = User(
    username='up2039019', 
    email='up2039019@myport.ac.uk', 
    image_file='default.jpg', 
    password='a1234'
)
db.session.add(user)
db.session.commit()
```

Querying for all users in the database:

```python
>>> users = User.query.all()
>>> [user.email for user in users]
```

Search for a user with a specific ID:

```python
>>> User.query.get(1)
```

Order users by email ascending:

```python
>>> users = User.query.order_by(User.email.asc())
>>> [user for user in users]
```

Search for a specific user in the database:

```python
>>> users = User.query.filter(User.username.contains('up2'))
>>> [user for user in users]
```

Add a new book to the database with the current user:

```python
book = Book(
    title='To Kill A Mockingbird', 
    author='Harper Lee', 
    genre='Philosophy', 
    summary='Account Of a Lawyer', 
    user=user
)
db.session.add(book)
db.session.commit()
```

Create a review for the book:

```python
review = Analysis(
    rating='Excellent', 
    review='Amazing read. Unputdownable', 
    book_id=book.id, 
    user=user
)
db.session.add(review)
db.session.commit()
```

