import sys, csv
from pydantic import  ValidationError
from models.csv_user import User

def validar_csv(fileName: str) -> None:
    # 2. Read and validate rows
    valid_users = []

    with open(fileName, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
    
        for row_number, row in enumerate(reader, start=2): # Header is line 1
            try:
                # model_validate parses the dictionary and enforces types
                user = User.model_validate(row)
                valid_users.append(user)
            except ValidationError as e:
                print(f"Row {row_number} failed validation:")
                print(e.errors())


if __name__ == "__main__":
    argc = len(sys.argv) 
    filename = "users.csv"
    if argc > 1:
        filename = sys.argv[1]
    validar_csv(filename)  
