django-new-app
==============

Shell Script responsável por criar uma nova aplicação django simples.

Utilizacao
===============
* clone esse repositorio
* dê permissao de escrita para esse script 
  * chmod +x iniciar-projeto.sh
* execute 
  * ./iniciar-projeto.sh nomedoprojeto


Qual sera o resultado
=====================

* criacao de uma virtualenv com o nome ve + nomedoprojeto
* projeto django 1.5.1 + aplicacao core
* criacao e primeiro commit em um repositorio git local
* conversao do tests.py para um modulo tests
* conversao do settings.py para um modulo contendo 3 arquivos de configuracao
* criacao dos diretorios de statics e media
* criacao do requirementes.txt já incluindo o django 1.5.1
* criacaro do .gitignore excluindo os arquivos .pyc
* inicia o servidor e poe a app rodando manage runserver :)
