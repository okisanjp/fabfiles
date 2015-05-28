from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['densho-now.com']

def commit_push():
    local("git add . && git commit")
    local("git push")

def deploy():
    code_dir = '/var/www/densho-now.com'
    with cd(code_dir):
        run("sudo git pull")

def cache_clear():
    run("sudo find /var/www/densho-now.com/app/tmp/cache/views -name 'densho*' -print | xargs rm")

def commit_push_deploy():
    commit()
    deploy()
