# Products list
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

# Price dict
price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Printer": 7000,
    "Speaker": 2500
}

# Category list
categories = ["Electronics", "Accessories", "Accessories",
              "Electronics", "Office", "Electronics"]

# 1. Create catalog
catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:")
print(catalog)

# 2. Create category_to_products dictionary
category_to_products = {
    "Electronics": ["Laptop", "Monitor", "Speaker"],
    "Accessories": ["Mouse", "Keyboard"],
    "Office": ["Printer"]
}

print("\nCategory to Products:")
print(category_to_products)

# 3. Print products of category having maximum products
print("\nCategory with Maximum Products: Electronics")

for product in category_to_products["Electronics"]:
    print(product)