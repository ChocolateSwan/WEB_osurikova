import multiprocessing
bind='localhost:8000'
errorlog = '/home/olyasur/PycharmProjects/ask_osurikova/gunicorn.log'
workers = multiprocessing.cpu_count() * 2 + 1
