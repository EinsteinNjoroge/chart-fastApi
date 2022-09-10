from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uuid
from fastapi.middleware.cors import CORSMiddleware
from static_data import chart_data, industries, comments


class Comment(BaseModel):
    username: str
    message: str
    year: str
    industry: str


origins = ["*"]
allowed_methods = ["POST", 'GET']

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=allowed_methods,
)


@app.get("/")
async def home():
    return "Server is running"


@app.get("/chart-data")
async def fetch_chart_data():
    return {
        "chart_data": chart_data,
        "industries": industries,
    }


@app.get("/comments")
async def fetch_all_comments():
    return comments


@app.post("/comments", status_code=status.HTTP_201_CREATED)
async def create_new_comment(comment: Comment, response: Response):
    if comment.industry in industries:
        new_comment = {
            "id": uuid.uuid4(),
            "username": comment.username,
            "message": comment.message
        }

        if comment.year in comments[comment.industry]:
            comments[comment.industry][comment.year].append(new_comment)
        else:
            comments[comment.industry][comment.year] = [new_comment]
        return {
            "success": True,
            "message": "Comment created",
            "comment": new_comment
        }

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {
        "success": False,
        "message": "Could not create the comment, check your payload"
    }
