# djangoblog-zuri
Blog webapp written in python django

## web address
https://djangoblog-zuri.herokuapp.com/

## Basic Features
Basic Features includes:
+ Post content
+ Read content
+ Update content
+ Delete content

## Advance Features
+ Comment support
+ User registration
+ User Login and Logout
+ Password Recovery

## Installation instruction
Clone repository
```
git clone https://github.com/austinoski/djangoblog-zuri
```

Change to project directory
```
cd djangoblog-zuri
```

Install required packages (recommend installing in a virtual environment)
```
pip install -r requirements.txt
```

Create file named .env in config folder and add
```
SECRET_KEY=replacewithalongrandomtext
DEBUG=True
```

Run database migrations
```
python manage.py migrate
```

Run development server
```
python manage.py run server
```

Open your browser and visit:
```
127.0.0.1:8000/
```
To see the running application.

## Conclusion
A big thanks to Zuriteam and Ingressive4good 
for the opportunity to learn and grow.

