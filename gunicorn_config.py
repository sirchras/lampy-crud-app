workers = 4
worker_class = 'uvicorn.workers.UvicornWorker'
bind = 'localhost:8080'
reload = True

# logging
accesslog = '-'
errorlog = '-'

