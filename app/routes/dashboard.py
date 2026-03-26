from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.cache import cache_service
from tasks import process_video_task, celery_app
from celery.result import AsyncResult
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # fetch data first for clarity
    current_hits = cache_service.increment_hits()
    hostname = os.getenv("HOSTNAME", "Unknown_Clone")
    
    # use keyword arguments: request, name, context
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "hits": current_hits, 
            "server_id": hostname
        }
    )

@router.post("/process-video")
async def trigger_video_processing(video_id: str = Query(...)):
    task = process_video_task.delay(video_id)
    return {"task_id": task.id}

@router.get("/task-status/{task_id}")
async def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "task_status": result.status,
        "task_result": result.result if result.ready() else None
    }