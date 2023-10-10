from celery import shared_task


@shared_task
def detect_problem(upload_path, result_path):
    # DO MAGIC
    return result_path