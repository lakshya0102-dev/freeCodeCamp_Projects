# Medical Data Validator

Simple script for validating medical record dictionaries (FreeCodeCamp example).

## Overview

`medical_data_validator.py` defines two helper functions:

- `validate_record(record)` — returns `True` if a single record matches expected formats.
- `validate(medical_records)` — prints validation results for a list of records.

The repository includes a small sample dataset and prints validation results when run.

## Requirements

- Python 3.8+
- No external packages required (uses the standard `re` module).

## Usage

Run the script directly:

```bash
python medical_data_validator.py
```

Example output:

```
Record 1: Valid format.
Record 2: Invalid format.
```

## Validation rules

- `patient_id`: must match `p\d+` (case-insensitive), e.g. `P123`.
- `age`: digits only and between 0 and 120 inclusive.
- `blood_pressure`: format `NN/NN` or `NNN/NNN`, matched by `\d{2,3}/\d{2,3}`.
- `temperature`: numeric with optional single decimal, matched by `\d{2,3}(\.\d)?` (e.g. `98.6`).
- `last_visit_id`: must match `v\d+` (case-insensitive), e.g. `V456`.

## As a module

You can import the validator functions into your own scripts:

```python
from medical_data_validator import validate, validate_record

records = [
    {"patient_id": "P1", "age": "30", "blood_pressure": "120/80", "temperature": "98.6", "last_visit_id": "V1"}
]
validate(records)
```

## Notes

- The script uses an in-file sample dataset. To validate your own data, replace `medical_records` or call `validate()` with your list of record dicts.

---

See the main script: [medical_data_validator.py](medical_data_validator.py)
