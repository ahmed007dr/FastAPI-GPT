from fastapi import FastAPI , BackgroundTasks , HTTPException ,Request , Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from schemas import *

app = FastAPI()


# setup for Jinja templates
templates = Jinja2Templates(directory = 'templates')


@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# Translation Route
@app.post('/translate', response_model=TaskResponse)
def translate(request: TranslationRequest):
    # Simulate a task ID generation (in a real app, this would be stored in a database)
    task_id = 1  # Example ID, should be dynamically generated

    return {"task_id": task_id}
