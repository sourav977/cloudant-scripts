import json
import random
import string
import uuid
from datetime import datetime, timedelta

def generate_random_json_document():
    ts = (datetime.now() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    random_data = {
        "_id": str(uuid.uuid4()),
        "name": ''.join(random.choices(string.ascii_letters, k=10)),
        "rand_value": random.uniform(0.0, 1000.0),
        "color": random.choice(["black", "blue", "red", "green", "yellow", "white", "gray", "navy", "orange", "purple"]),
        "is_active": random.choice([True, False]),
        "date": ts
    }
    return random_data

def generate_large_json_file(file_path, file_size_gb):
    file_size_bytes = file_size_gb * (1024**3)
    first_document = True
    
    with open(file_path, 'w') as file:
        file.write("[")  # Start of the array
        while file.tell() < file_size_bytes:
            json_document = generate_random_json_document()
            json.dump(json_document, file)
            file.write(',')
        file.seek(file.tell() - 1)
        file.write("]")  # End of the array

    print(f"Generated JSON file: {file_path}")

if __name__ == "__main__":
    output_file_path = 'sample_json_2MB.json'
    target_file_size_gb = 0.002
    generate_large_json_file(output_file_path, target_file_size_gb)
