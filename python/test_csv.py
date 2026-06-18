import csv
from pydantic import  ValidationError
import models.user_csv as csv_user


# 2. Read and validate rows
valid_users = []

with open("users.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row_number, row in enumerate(reader, start=2): # Header is line 1
        try:
            # model_validate parses the dictionary and enforces types
            user = csv_user.User.model_validate(row)
            valid_users.append(user)
        except ValidationError as e:
            print(f"Row {row_number} failed validation:")
            print(e.errors())
