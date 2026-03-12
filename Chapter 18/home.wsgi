import bottle
application = bottle.default_app()

@bottle.rout('/')
def home():
    return "apache and wsgi, sitting in a tree"