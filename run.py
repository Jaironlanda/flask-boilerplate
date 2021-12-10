from appname import create_app

# command/terminal
# gunicorn -w 4 run:myapp --log-level debug --reload
myapp = create_app()
