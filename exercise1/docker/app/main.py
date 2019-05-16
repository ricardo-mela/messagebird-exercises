from flask import Flask, request, send_file
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter
from datetime import datetime
from pytz import timezone


app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})



homer_counter = Counter('homer_hits', 'Homer Simpson requests')
covilha_counter = Counter('covilha_hits', 'Covilha requests')

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/homersimpson")
def homer():
  homer_counter.inc()
  return send_file("/static_assets/index.html", mimetype='text/html')

@app.route("/covilha")
def covilha():
  myformat = "%Y-%m-%d %H:%M:%S %Z%z"
  now_utc = datetime.now(timezone('UTC'))
  now_covilha = now_utc.astimezone(timezone('Europe/Lisbon'))
  covilha_counter.inc()
  return "The time in Covilha City is "+ now_covilha.strftime(myformat) 

if __name__ == '__main__':
    app.run()
