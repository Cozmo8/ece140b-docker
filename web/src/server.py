from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
from pyramid.renderers import render_to_response

from dotenv import load_dotenv
import mysql.connector as mysql
import os

load_dotenv('credentials.env')
 
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor(buffered=True)

def get_home(req):
    return FileResponse("templates/home.html")

if __name__ == '__main__':
  with Configurator() as config:
    config.add_route('home', '/')
    config.add_view(get_home, route_name='home')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)
    app = config.make_wsgi_app()
    
server = make_server('0.0.0.0', 6543, app)
print('Web server started on: http://0.0.0.0:6543')
server.serve_forever()