from fastapi import FastAPI
from database import engine, Base
from routers import auth, works, support

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include routers
app.include_router(auth.router)
app.include_router(works.router)
app.include_router(support.router)
