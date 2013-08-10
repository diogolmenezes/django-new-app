DNA (django-new-app)
====================

python script able to create an improved skeleton of a Django application

features
=====================

* creates virtualenv or virtualenvwrapper environments
* install newer django
* creates django project and django application (core)
* creates requirementes.txt file
* creates git repository and makes the first commit
* creates .gitignore file with *.pyc and .DS_STORE
* converts the tests.py file to a python module
* creates media, static and templates{js,css,img} folders

requirements
===============
* python 2.7+
* virtualenv or virtualenvwrapper

installation and run
======================
* clone esse repositorio

* run on virtualenvwrapper
  * python dna.py myProject -w
* run on virtual env
  * python dna.py myProject

have fun :)



Help me to improve dna
=======================
* include support for others versions of django, passing parameters, something like (python dna.py myProject -w -d1.5.1)
