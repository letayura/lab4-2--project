import csv
import json
import yaml
import logging
from athlete_opp import Athlete

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(message)s")


def load_config(config_path="config.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def process_athletes():
    config = load_config()
    input_csv = config["files"]["input_csv"]
    output_jsonl = config["files"]["output_jsonl"]

    file_handler = logging.FileHandler(config["files"]["error_log"])
    logging.getLogger().addHandler(file_handler)

    success_records = []

    with open(input_csv, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row_num, row in enumerate(reader, start=1):
            try:
                athlete = Athlete(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    phone=row["phone"],
                    team_id=int(row["team_id"]),
                )
                success_records.append(athlete.to_dict())
            except Exception as e:
                error_msg = f"Помилка у рядку {row_num} ({row}): {e}"
                print(error_msg)
                logging.error(error_msg)

    with open(output_jsonl, mode="w", encoding="utf-8") as jsonl_file:
        for record in success_records:
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    process_athletes()
