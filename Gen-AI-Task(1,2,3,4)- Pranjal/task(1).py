#list containing 6 product names
products= ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

#tuple named sample_product that stores (product_name, price, category) for one product
sample_product= ("Laptop", 66000, "Electronics")

#print 2nd and last product from the list
print("2nd Product:- ",products[1])
print("Last Product:- ",products[-1])

#append two new product and print updated list
products.append("Webcam")
products.append("Router")

print("Updated Products List: ")
print(products)