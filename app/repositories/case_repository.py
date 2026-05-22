from app.database import cases_collection


def insert_case(case_data):
    result = cases_collection.insert_one(case_data)
    return {
        "inserted_id": str(result.inserted_id)
    }


def get_resolved_cases():
    return list(
        cases_collection.find({
            "status": "resolved"
        })
    )
