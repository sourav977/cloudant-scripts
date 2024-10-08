import json
import random
import string
from datetime import datetime, timedelta

BRANDS = [
    "Levis", "CK", "Killer", "Wrangler", "Snitch", "Wrong", 
    "Pepe Jeans", "Flying Machine", "Rare Rabbit", "H and M", 
    "Louis Philippe Jeans", "Dennis Lingo", "Highlander", 
    "Duke", "Fcuk", "Indian Terrain", "Lee", "Blackberry"
]

SIZES = [28, 30, 32, 34, 36, 38, 40]
AM_SIZE_MAP = {28: "SS", 30: "S", 32: "M", 34: "L", 36: "XL", 38: "XXL", 40: "XXXL"}
COLORS = ["black", "blue", "red", "green", "yellow", "white", "gray", "navy", "orange", "purple"]
STRETCH_OPTIONS = ["non-stretchable", "stretchable"]
FIT_OPTIONS = ["slim fit", "skinny fit", "tapered fit", "jogger", "regular fit", "relaxed fit", "straight fit"]
FABRIC_OPTIONS = ["elastane", "polyester", "cotton", "linen", "viscose rayon"]

def generate_item_code(brand):
    hex_string = ''.join(random.choices(string.hexdigits.lower(), k=32))
    return f"Br_{brand}_{hex_string}"

def generate_document(doc_id):
    brand = random.choice(BRANDS)
    size = random.choice(SIZES)
    am_size = AM_SIZE_MAP[size]
    color = random.choice(COLORS)
    price = random.randint(1199, 9999)
    stretch = random.choice(STRETCH_OPTIONS)
    fit = random.choice(FIT_OPTIONS)
    fabric = random.choice(FABRIC_OPTIONS)
    mfg_date = (datetime.now() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    brand_id = f"Br_{brand.replace(' ', '_')}"
    random_data = {
        "_id": str(doc_id),
        "brand_id": brand_id,
        "size": size,
        "am_size": am_size,
        "color": color,
        "price": price,
        "stretch": stretch,
        "fit": fit,
        "fabric": fabric,
        "item_code": generate_item_code(brand.replace(' ', '_')),
        "mfg_date": mfg_date
    }
    return random_data


def generate_documents(file_path, doc_count):
    with open(file_path, 'w') as file:
        file.write('{"docs": [') 
        for i in range(doc_count) :
            if i < doc_count:
                json_document = generate_document(i)
                json.dump(json_document, file)
                if i < doc_count - 1:
                    file.write(',')
        file.write(']}') 

    print(f"Generated JSON file: {file_path}")


# Usage
if __name__ == "__main__":
    output_file_path = 'generated_documents.json'
    number_of_documents = 1000
    generate_documents(output_file_path, number_of_documents)
    print(f"Generated {number_of_documents} documents.")

