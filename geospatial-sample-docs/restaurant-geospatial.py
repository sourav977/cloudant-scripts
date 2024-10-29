import json
import random

# Function to read restaurant names from a text file
def load_restaurant_names(file_path):
    with open(file_path, 'r') as file:
        # Read lines and strip whitespace/newline characters
        names = [line.strip().strip('"') for line in file if line.strip()]
    return names

# Function to generate a random restaurant name from the loaded names
def generate_restaurant_name(restaurant_names):
    return random.choice(restaurant_names)

# Function to generate a random phone number
def generate_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(456, 789)}-{random.randint(1000, 9999)}"

# Function to generate random coordinates within a 50km range
def generate_coordinates(center_lat=17.443516, center_lon=78.363314, range_km=50):
    lat_offset = random.uniform(-0.45, 0.45)  # approx 50km latitude offset
    lon_offset = random.uniform(-0.45, 0.45)  # approx 50km longitude offset
    return [round(center_lat + lat_offset, 6), round(center_lon + lon_offset, 6)]

# Function to generate random categories
def generate_categories():
    all_categories = [
        "Salads", "Afghan", "Hamburgers", "Filipino", "Italian", "Chinese", 
        "Mexican", "Indian", "Thai", "Japanese", "Mediterranean", "American", "Turkish", "French"
        "Seafood", "Vegetarian", "Vegan", "BBQ", "Desserts", "Fast Food", "Korean"
    ]
    num_categories = random.randint(1, 10)
    return random.sample(all_categories, num_categories)

def generate_document(doc_id, restaurant_names):
    name = generate_restaurant_name(restaurant_names)
    phone = generate_phone_number()
    email = f"{name.lower().replace(' ', '').replace('\'','')}@example.com"
    coordinates = generate_coordinates()
    stars = random.randint(1, 5)
    categories = generate_categories()

    random_data = {
        "_id": doc_id,
        "name": name,
        "contact": {
            "phone": phone,
            "email": email,
            "location": {
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates
                }
            }
        },
        "stars": stars,
        "categories": categories
    }
    return random_data

def generate_documents(file_path, doc_count, restaurant_names):
    with open(file_path, 'w') as file:
        file.write('[') 
        for i in range(doc_count):
            json_document = generate_document(i + 1, restaurant_names)
            json.dump(json_document, file)
            if i < doc_count - 1:
                file.write(',')
        file.write(']') 

    print(f"Generated JSON file: {file_path}")

# Usage
if __name__ == "__main__":
    output_file_path = 'generated_restaurant_documents.json'
    number_of_documents = 1024
    restaurant_names_file = 'restaurant-names.txt'
    
    # Load restaurant names from the file
    restaurant_names = load_restaurant_names(restaurant_names_file)
    
    generate_documents(output_file_path, number_of_documents, restaurant_names)
    print(f"Generated {number_of_documents} documents.")
