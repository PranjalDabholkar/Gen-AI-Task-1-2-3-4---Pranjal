# Create dictionary
price_dict = {
    "Laptop": 66000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Printer": 7000,
    "Speaker": 2500
}

#new product
price_dict["Webcam"] = 1800

# Update price of existing product
price_dict["Laptop"] = 70000

# Remove a product
del price_dict["Printer"]

print(price_dict)

# Calculate average price
total_price = sum(price_dict.values())
average_price = total_price / len(price_dict)

print("Average Price:", average_price)
