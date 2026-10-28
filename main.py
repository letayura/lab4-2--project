from fastapi import Depends, FastAPI, HTTPException

from athlete_model import AthleteBase
from athlete_repository import AthleteRepository
from postgres_athlete_repo import PostgresAthleteRepo

app = FastAPI()


def get_repo() -> AthleteRepository:
    return PostgresAthleteRepo()


@app.get("/athletes/")
def read_athletes(repo: AthleteRepository = Depends(get_repo)):  # noqa: B008
    return repo.get_all()


@app.get("/athletes/{athlete_id}")
def read_athlete(athlete_id: int, repo: AthleteRepository = Depends(get_repo)):  # noqa: B008
    row = repo.get_by_id(athlete_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Not found")
    return row


@app.post("/athletes/")
def create_athlete(athlete: AthleteBase, repo: AthleteRepository = Depends(get_repo)):  # noqa: B008
    return repo.create(athlete)


@app.put("/athletes/{athlete_id}")
def update_athlete(
    athlete_id: int, athlete: AthleteBase, repo: AthleteRepository = Depends(get_repo)
):  # noqa: B008
    row = repo.update(athlete_id, athlete)
    if row is None:
        raise HTTPException(status_code=404, detail="Not found")
    return row


@app.delete("/athletes/{athlete_id}")
def delete_athlete(athlete_id: int, repo: AthleteRepository = Depends(get_repo)):  # noqa: B008
    if not repo.delete(athlete_id):
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted successfully"}
