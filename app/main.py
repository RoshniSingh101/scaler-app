from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os, redis, pymemcache
from tasks import process_video_task, celery_app

from celery.result import AsyncResult

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# connections
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, decode_responses=True)
mem_cache = pymemcache.client.base.Client(('memcached', 11211))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    hits = cache.incr("hits")
    server_id = os.getenv("HOSTNAME", "Unknown_Clone")
    
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"hits": hits, "server_id": server_id}
)

@app.post("/process-video")
async def trigger_video_processing(video_id: str):
    task = process_video_task.delay(video_id)
    # return TASK ID to tell browser which task to track
    return {"task_id": task.id}

@app.get("/task-status/{task_id}")
async def get_status(task_id: str):
    # look into Redis for the specific ID
    result = AsyncResult(task_id, app=celery_app)
    
    response = {
        "task_id": task_id,
        "task_status": result.status, # PENDING, SUCCESS, or FAILURE
        "task_result": None
    }
    
    if result.ready():
        response["task_result"] = result.result
        
    return response