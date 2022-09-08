from fastapi import FastAPI, Path
from api import users, courses, sections


app = FastAPI(
    title="LMS Using FastAPI",
    description="Just testing out FastAPI with Gwen"
)

app.include_router(router=users.router)
app.include_router(router=courses.router)
app.include_router(router=sections.router)

