#!/bin/bash

#valida utilizacao
if [ -z $1 ]; then
   echo -e "USO: \t\aInsira o nome do projeto"
   exit 1
fi

#criando e configurando virtual env
virtualenv --no-site-packages --distribute --unzip-setuptools ve$1
cd ve$1
source bin/activate
pip install django

#criando e configurando projeto
django-admin.py startproject $1 .
cd $1

#transformando o settings em modulo
mkdir settings
mv settings.py settings/production.py
touch settings/{__init__,stage,development}.py
echo "from production import *" > settings/stage.py
echo "from production import *" > settings/development.py
echo "import os" > settings/__init__.py
echo "global_settings = os.path.join(os.path.dirname(__file__), 'development.py')" >> settings/__init__.py
echo "execfile(global_settings)" >> settings/__init__.py

#criando e configurando a aplicacao
django-admin.py startapp core
mkdir static #diretorio para collect static
mkdir media
mkdir -p core/templates/core
mkdir -p core/static/{css,img,js}

#transformando os testes em modulo
mkdir core/tests
mv core/tests.py core/tests/simple_test.py
echo "from .simple_test import *" > core/tests/__init__.py

#criando o arquivo de requirements
pip freeze | grep -i django > requirements.txt

#configurando o repositorio do git
git init
echo "*.pyc" > .gitignore
git add .
git commit -m "first commit :)"

#iniciando o servidor
python ../manage.py runserver
