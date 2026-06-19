#list of products
products= ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

# Parallel category list
categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Office",
    "Electronics"
]

# Create set of categories
categories_set = set(categories)

print("Categories Set:")
print(categories_set)

# Add new category
categories_set.add("Networking")

# Add duplicate category
categories_set.add("Electronics")

print("After Adding Categories:")
print(categories_set)

# Check whether category exists
print("Is 'Desk' present?", "Desk" in categories_set)

