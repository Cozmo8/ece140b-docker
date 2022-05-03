from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
from pyramid.renderers import render_to_response
import os

def get_home(req):
    return FileResponse("templates/home.html")

def get_product(req):
    return FileResponse("templates/product.html")

def get_proposition(req):
    return FileResponse("templates/proposition.html")

def get_team(req):
    return FileResponse("templates/team.html")

def get_assignments(req):
    return FileResponse("templates/assignments.html")

if __name__ == '__main__':
  with Configurator() as config:
    config.add_route('home', '/')
    config.add_view(get_home, route_name='home')

    config.add_route('product', '/product')
    config.add_view(get_product, route_name='product')

    config.add_route('proposition', '/proposition')
    config.add_view(get_proposition, route_name='proposition')

    config.add_route('team', '/team')
    config.add_view(get_team, route_name='team')

    config.add_route('assignments', '/assignments')
    config.add_view(get_assignments, route_name='assignments')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)
    app = config.make_wsgi_app()
    
server = make_server('0.0.0.0', 6000, app)
server.serve_forever()