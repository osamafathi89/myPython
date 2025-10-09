from data_handler import fetch_products, safe_to_file, load_from_file
from product import Product

products = fetch_products()
if products:
    safe_to_file(products,"products.json")
    loaded_products = load_from_file("products.json")
    for item in loaded_products[:5]:  # Display first 5 products
        prod = Product(item['title'], item['price'], item['category'])
        prod.show()
else:
    print("No products found.")