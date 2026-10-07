from app_WEB import study_group_numbers
import json


if __name__ == "__main__":
    with open("data_groups.json", "w", encoding="utf-8") as f:
        json.dump(study_group_numbers(), f, indent=4, ensure_ascii=False)
