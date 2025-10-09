import requests , json
API_URL = 'https://fakestoreapi.com/products'
def fetch_products():
    try:
        response = requests.get(API_URL,timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestsException as e:
        print(f"Error fetching data: {e}")
        return []   
def safe_to_file(data,filename):
    with open(filename,"w") as file:
            json.dump(data,file)
            
def load_from_file(filename):
    try:
        with open(filename,"r") as file:
         return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    