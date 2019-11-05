# Note make sure Celery and RabbitMQ are installed.
# Next, make sure rabbitmq.service is running.
# Then, in one command line run "celery -A add_task worker --loglevel=info"
# Finally, in another command line run "python add_task_main.py"

import add_task

result = add_task.add.delay(5, 5)
