"""One Boss, Multiple Workers
ref. http://sdiehl.github.io/gevent-tutorial/#queues
"""
import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(n):
    for i in xrange(1, 5):
        api = {
            'name': n,
            'value': i,
        }
        tasks.put_nowait(api)


def boss():
    while not tasks.empty():
        api = tasks.get()
        print('boss got %s, value %s ' % (api['name'], api['value']))
        gevent.sleep(0)
    print('Quitting time!')


worker_list = []
for i in range(3):
    worker_list.append(gevent.spawn(worker, 'worker%s' % i))
gevent.joinall(worker_list)

gevent.spawn(boss).join()
