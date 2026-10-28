import psycopg
from psycopg.rows import dict_row

from athlete_model import AthleteBase


class PostgresAthleteRepo:
    DSN = "postgresql://postgres:postgres@localhost:5432/postgres"

    def get_all(self) -> list[dict]:
        with psycopg.connect(self.DSN, row_factory=dict_row) as conn:
            return conn.execute("SELECT * FROM athletes").fetchall()

    def get_by_id(self, athlete_id: int) -> dict | None:
        with psycopg.connect(self.DSN, row_factory=dict_row) as conn:
            return conn.execute(
                "SELECT * FROM athletes WHERE id=%s", (athlete_id,)
            ).fetchone()

    def create(self, athlete: AthleteBase) -> dict | None:
        with psycopg.connect(self.DSN, row_factory=dict_row) as conn:
            return conn.execute(
                """
                INSERT INTO athletes (first_name, last_name, phone, team_id) 
                VALUES (%s, %s, %s, %s) 
                RETURNING *
                """,
                (
                    athlete.first_name,
                    athlete.last_name,
                    athlete.phone,
                    athlete.team_id,
                ),
            ).fetchone()

    def delete(self, athlete_id: int) -> bool:
        with psycopg.connect(self.DSN) as conn:
            res = conn.execute(
                "DELETE FROM athletes WHERE id=%s", (athlete_id,)
            )
            return res.rowcount > 0