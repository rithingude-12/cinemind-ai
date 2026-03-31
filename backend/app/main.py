from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, recommend, watchlist, rating, insights
from app.db.init_db import init_db
from fastapi.staticfiles import StaticFiles

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(recommend.router, prefix=f"{settings.API_V1_STR}/recommend", tags=["recommend"])
app.include_router(watchlist.router, prefix=f"{settings.API_V1_STR}/watchlist", tags=["watchlist"])
app.include_router(rating.router, prefix=f"{settings.API_V1_STR}/rating", tags=["rating"])
app.include_router(insights.router, prefix=f"{settings.API_V1_STR}/insights", tags=["insights"])

# Optional: Host static images if needed locally, but frontend will likely proxy them
# import os
# posters_path = os.path.join(settings.DATASET_PATH, 'posters')
# if os.path.exists(posters_path):
#    app.mount("/posters", StaticFiles(directory=posters_path), name="posters")
