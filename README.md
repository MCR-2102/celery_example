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

PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app

- Start Celery beat:

PEX_SCRIPT=celery ./dist/example.celery.pex beat --app=app.worker.app

- Start Flask with gunicorn:

PEX_SCRIPT=gunicorn ./dist/example.celery.pex app:app -c config.ini


# Celery headless worker issue demonstration

PEX_SCRIPT=celery ./dist/example.celery.pex worker --app=app.worker.app --detach

The above command fails quietly. I believe this is due to the detached instance being started outside of the pex environment and so without the required dependencies.

