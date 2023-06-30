![Language](https://img.shields.io/badge/Python-3.10.x-important)&nbsp;
![Django](https://img.shields.io/badge/Django-4.2.x-important)&nbsp;
![Update](https://img.shields.io/badge/Last%20Update-June%2030,%202023-brightgreen)&nbsp;
![Completed](https://img.shields.io/badge/Progress-60/111-important)

- Pipenv Doc — https://pipenv-fork.readthedocs.io/
- PyCon 2018 — [Pipenv: The Future of Python Dependency Management](https://www.youtube.com/watch?v=GBQAKldqgZs) 

## Virtual Environment

- Go to the directory and type `pip install pipenv`.
- After being installed successfully type `pipenv install` to create virtual environment.
- To activate the virtual environment type `pipenv shell`.
- To install django type `pipenv install django` | `pipenv install django==x.x.x`.
- To check if there is any virtual environment available for this project type `pipenv --venv` & if it exists then will display the location of the virtual environment else return a message.
- To exit the virtual environment type `exit` or `CTRL + d` & terminal will back to the normal prompt.
- Create Django project `django-admin startproject "NameOfProject"`.
- Create django app `python manage.py startapp "NameofApp"`.
- Migration command `python manage.py makemigrations` then `python manage.py migrate`.
- Remove virtualenv `pipenv --rm`. It will delete the virtual environment for this current project.
- Create `requirements.txt` file type `pip freeze > requirements.txt`.
- Install all dependencies after cloning the repo type `pipenv install` then `pipenv install -r requirements.txt`.
- Check Django version `python -m django --version`.

## Tricks/Cheatsheet

- [Classy Class-Based Views](https://ccbv.co.uk/)
- [Classy Django REST Framework](https://www.cdrf.co/)
- [Classy Django Forms](https://cdf.9vo.lt/)
- [adamghill/django-fbv](https://github.com/adamghill/django-fbv)

## Commonly Used Apps

- [model_bakery](https://github.com/model-bakers/model_bakery)
- [factory-boy](https://github.com/FactoryBoy/factory_boy) `fetching fake data`
- [django-braces](https://github.com/brack3t/django-braces) `classed based view`
- [djang-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) `awesome`
- [django-guardian](https://github.com/django-guardian/django-guardian)
- [django-jimmypage](https://github.com/yourcelf/django-jimmypage) `caching`
- [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
- [pytest](https://github.com/pytest-dev/pytest)
- [coveragepy](https://github.com/nedbat/coveragepy)

## Newsletters

- [Django News](https://django-news.com/)
- [Django Trending Packages](https://django.wtf/)
- [Django Books](https://djangobook.com/)
- [Discover the latest content from the Django community](https://djangofeeds.com/) `videos/articles`
- [Django Packages](https://djangopackages.org/)

## Tutorials/Articles

- [Mastering Django Tutorials](https://masteringdjango.com/mastering-django-tutorials/)
- [Understanding Django](https://www.mattlayman.com/understand-django/)

## Conferences

- [Django: Under The Hood 2014](https://www.youtube.com/playlist?list=PLQdy7QUATciaUglAUzka6E7zrN3UWomws)
- [Django: Under the Hood 2016](https://www.youtube.com/playlist?list=PLQdy7QUATciZ4V3g3iCTnG5fvkZkuNGyg)
- [DjangoCon US](https://www.youtube.com/@DjangoConUS/videos)
- [DjangoCon Europe](https://www.youtube.com/@DjangoConEurope/videos)

## Podcasts

- [Django Riffs](https://djangoriffs.com/)
- [Django Chat](https://djangochat.com/)
