import re


def validate_record(record):
    patient_id = record.get("patient_id", "")
    age = record.get("age", "")
    blood_pressure = record.get("blood_pressure", "")
    temperature = record.get("temperature", "")
    last_visit_id = record.get("last_visit_id", "")

    is_valid = (
        re.fullmatch(r"p\d+", patient_id, re.IGNORECASE)
        and age.isdigit()
        and 0 <= int(age) <= 120
        and re.fullmatch(r"\d{2,3}/\d{2,3}", blood_pressure)
        and re.fullmatch(r"\d{2,3}(\.\d)?", temperature)
        and re.fullmatch(r"v\d+", last_visit_id, re.IGNORECASE)
    )

    return bool(is_valid)


def validate(medical_records):
    for index, record in enumerate(medical_records, start=1):
        if validate_record(record):
            print(f"Record {index}: Valid format.")
        else:
            print(f"Record {index}: Invalid format.")


medical_records = [
    {
        "patient_id": "P123",
        "age": "25",
        "blood_pressure": "120/80",
        "temperature": "98.6",
        "last_visit_id": "V456"
    },
    {
        "patient_id": "X123",
        "age": "150",
        "blood_pressure": "120-80",
        "temperature": "98.6",
        "last_visit_id": "A456"
    }
]


validate(medical_records)