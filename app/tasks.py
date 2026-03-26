from celery import Celery
import time

celery_app = Celery('tasks', 
            broker='pyamqp://guest@rabbitmq//', 
            backend='redis://redis:6379/0') 

celery_app.conf.broker_connection_retry_on_startup = True

@celery_app.task(bind=True)
def process_video_task(self, video_id):
    print(f"Starting heavy work on {video_id}...")
    time.sleep(5)  # simulate the 5-second process
    print(f"Finished {video_id}!")
    
    # return value browser is waiting for (see js code in index.html)
    return {"success": True, "message": "Video Processed Successfully"}