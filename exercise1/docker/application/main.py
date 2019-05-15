from prometheus_client import Counter

c = Counter('covinha_count', 'Covinha site hit count')
def application(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/plain')])
    c.inc()
    return ["Hello World!\n"]
