from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from static_data import chart_data, industries, comments

origins = ["*"]
allowed_methods = ["POST", 'GET']

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=allowed_methods,
)


@app.get("/chart-data")
async def fetch_chart_data():
    return {
        "chart_data": chart_data,
        "industries": industries,
    }


@app.get("/comments")
async def fetch_all_comments():
    return comments
