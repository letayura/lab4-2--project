import psycopg

DSN = "postgresql://postgres:postgres@localhost:5432/postgres"


def init_db():
    with psycopg.connect(DSN) as conn:
        conn.execute("DROP TABLE IF EXISTS athletes CASCADE;")
        conn.execute("DROP TABLE IF EXISTS teams CASCADE;")

        conn.execute("""
            CREATE TABLE teams (
                id serial PRIMARY KEY, 
                name text NOT NULL,
                city text NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE athletes (
                id serial PRIMARY KEY, 
                first_name text NOT NULL,
                last_name text NOT NULL,
                phone text NOT NULL,
                team_id int REFERENCES teams(id) ON DELETE CASCADE
            )
        """)

        conn.execute(
            "INSERT INTO teams (name, city) VALUES (%s, %s)", ("Динамо", "Київ")
        )

        for i in range(1, 55):
            conn.execute(
                "INSERT INTO athletes (first_name, last_name, phone, team_id) VALUES (%s, %s, %s, %s)",
                (f"Ім'я{i}", f"Прізвище{i}", f"+3805012345{i:02d}", 1),
            )
        print("Базу успішно ініціалізовано. Додано 54 спортсмени.")


if __name__ == "__main__":
    init_db()
