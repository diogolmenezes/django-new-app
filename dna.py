# coding: utf-8
import sys
import os
from shutil import move

class DjangoNewApp(object):

    def pip(self):
        if os.name == 'nt':
            return '%s/Scripts/pip.exe' % self.virtualenv_path
        else:
            return '%s/bin/pip' % self.virtualenv_path

    def dj_admin(self):
        if os.name == 'nt':
            return '%s/Scripts/django-admin.py' % self.virtualenv_path
        else:
            return '%s/bin/django-admin.py' % self.virtualenv_path

    def create_virtual_env(self):
        print 'creating new virtualenv %s...' % self.virtualenv
        if self.use_wrapper:
            os.chdir(os.environ['WORKON_HOME'])
            os.system('virtualenv %s --no-site-packages --distribute' % self.virtualenv)
            os.chdir(self.base_dir)
            self.virtualenv_path = '%s/%s' % (os.environ['WORKON_HOME'], self.virtualenv)
        else:
            os.system('virtualenv %s --no-site-packages --distribute' % self.virtualenv)
            self.virtualenv_path = '%s/%s' % (self.base_dir, self.virtualenv)

    def install_django(self):
        print 'installing django ...'
        os.system('%s install django' % self.pip())

    def create_django_project(self):
        print 'creating django project ...'
        if self.use_wrapper:
            os.system('%s startproject %s' % (self.dj_admin(), self.project))
            self.project_dir = '%s/%s/%s' % (os.getcwd(), self.project, self.project)
        else:
            os.chdir('./%s' % self.virtualenv)
            os.system('%s startproject %s .' % (self.dj_admin(), self.project))
            self.project_dir = '%s/%s/' % (os.getcwd(), self.project)
            os.chdir(self.base_dir)

    def create_first_app_core(self):
        print 'creating first app [core] ...'
        os.chdir(self.project_dir)
        os.system('%s startapp core' % self.dj_admin())
        os.chdir(self.base_dir)

    def create_static_media(self):
        print 'creating static and media folders ...'
        os.mkdir('%s/media' % self.project_dir)
        os.mkdir('%s/static' % self.project_dir)
        os.mkdir('%s/core/template' % self.project_dir)
        os.mkdir('%s/core/template/css' % self.project_dir)
        os.mkdir('%s/core/template/img' % self.project_dir)
        os.mkdir('%s/core/template/js' % self.project_dir)

    def create_requirements(self):
        print 'creating requirements.txt ...'
        file = open('%s/requirements.txt' % self.project_dir, 'w')
        file.write('django==1.5.1')
        file.close()

    def convert_test_to_module(self):
        print 'converting tests.py to a python module ...'
        os.mkdir('%s/core/tests' % self.project_dir)
        file = open('%s/core/tests/__init__.py' % self.project_dir, 'w')
        file.write('from .simple_test import *')
        file.close()
        move('%s/core/tests.py' % self.project_dir, '%s/core/tests/simple_test.py' % self.project_dir)

    def git(self):
        print 'creating a git repo and making the first commit ...'
        os.chdir(self.project_dir)
        file = open('.gitignore', 'w')
        file.write('*.pyc\n.DS_Store')
        file.close()
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.chdir(self.base_dir)

    def run(self):
        print 'starting the party ...'
        self.base_dir = os.getcwd()
        self.create_virtual_env()
        self.install_django()
        self.create_django_project()
        self.create_first_app_core()
        self.create_static_media()
        self.create_requirements()
        self.convert_test_to_module()
        self.git()
        print 'Done. Have fun with %s :)' % self.project

    def __init__(self):
        self.parameters = sys.argv[1:]
        if len(self.parameters) > 0:
            self.project = self.parameters[0]
            self.virtualenv = self.project
            try:
                self.use_wrapper = self.parameters[1] == '-w'
            except:
                self.use_wrapper = False
                pass
        else:
            print 'ERROR: You must set the name of project'

dna = DjangoNewApp()
dna.run()