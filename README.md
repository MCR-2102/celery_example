# celery_example
Example of packaging Flask and Celery with PEX. 

This demonstrates headless celery worker running issue.


# To Build PEX file

Clone repo.

Run 'make clean build'.

Pex file will be created in ./dist sub dir.

(dist dir and .pex has also been included here).


# To run Flask and Celery from the PEX

- Start Celery worker:

PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --loglevel=DEBUG --logfile=./celeryWorker.log

- Start Celery beat:

PEX_SCRIPT=celery ./dist/example.celery.pex beat --app=app.worker.app --loglevel=DEBUG --logfile=./celeryBeat.log

- Start Flask with gunicorn:

PEX_SCRIPT=gunicorn ./dist/example.celery.pex app:app -c config.ini


# Celery headless issue demonstration

PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --detach --loglevel=DEBUG --logfile=./celeryWorkerDetach.log

The above command works.

Now running the beat detached:

PEX_SCRIPT=celery ./dist/example.celery.pex beat --app=app.worker.app --detach --loglevel=DEBUG --logfile=./celeryBeat.log




