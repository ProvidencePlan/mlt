from fabric.api import local

def deploy():
    local("./manage.py collectstatic --noinput")
    local("epio upload")
    # ensure the compress cache dir exists
    local("epio run_command mkdir -- -p ../data/compress-cache")
    local("epio django compress")
    local("epio django checksecure")
