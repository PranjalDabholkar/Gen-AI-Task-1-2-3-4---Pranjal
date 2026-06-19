# Gen-AI-Task-1-2-3-4---Pranjal
# Python Product Catalog Manager

Welcome to the Product Catalog Manager! This repository contains a series of Python scripts designed to teach and demonstrate how to manage an inventory system using fundamental Python data structures: Lists, Tuples, Sets, and Dictionaries.

## Interactive Task Tracker
*Check off the modules as you review and run the code:*
- [ ] **Module 1**: Basic List and Tuple Operations
- [ ] **Module 2**: Set Operations and Deduplication
- [ ] **Module 3**: Dictionary Price Manipulations
- [ ] **Module 4**: Advanced Catalog Building

---

## Project Modules

*Click on the sections below to expand and read about each script's functionality!*

<details>
<summary><b>1. Product Collection (Lists & Tuples)</b></summary>
<br>
This module handles basic product additions and lookups using sequence data types:

* Initializes a primary list of 6 products: "Laptop", "Mouse", "Keyboard", "Monitor", "Printer", and "Speaker"[cite: 1].
* Creates a tuple named `sample_product` to store a single product's name, price, and category (e.g., `"Laptop", 66000, "Electronics"`)[cite: 1].
* Demonstrates indexing by printing specific items, specifically the 2nd and last products from the list[cite: 1].
* Appends two new products ("Webcam" and "Router") and prints the updated list[cite: 1].

</details>

<details>
<summary><b>2. Categories (Sets)</b></summary>
<br>
This module demonstrates how to manage unique product categories:

* Uses a parallel list of categories that corresponds to the main product list[cite: 2].
* Converts the list into a `categories_set` to automatically filter out duplicate entries[cite: 2].
* Adds a new category ("Networking") and attempts to add a duplicate category ("Electronics") to demonstrate how sets inherently maintain uniqueness[cite: 2].
* Performs a boolean membership check to determine if the category "Desk" is present in the set[cite: 2].

</details>

<details>
<summary><b>3. Product Pricing (Dictionaries)</b></summary>
<br>
This module manages the financial data of the catalog using key-value pairs:

* Creates a `price_dict` to map each specific product to its respective cost[cite: 3].
* Adds a new product key ("Webcam" for 1800) and updates the price of an existing product ("Laptop" to 70000)[cite: 3].
* Removes a product ("Printer") from the dictionary using the `del` command[cite: 3].
* Calculates and outputs the average price of all items currently stored in the dictionary[cite: 3].

</details>

<details>
<summary><b>4. Combined Operations</b></summary>
<br>
This module synthesizes lists, dicts, and tuples into a complex, realistic inventory structure:

* Combines the raw products list, the price dictionary, and the category list into a single `catalog` consisting of formatted tuples[cite: 4].
* Builds a `category_to_products` dictionary that maps individual categories (e.g., "Electronics", "Accessories", "Office") to a grouped list of their corresponding products[cite: 4].
* Identifies the category containing the maximum number of products ("Electronics") and loops through it to print its specific items[cite: 4].

</details>

---

##  How to Run

1. Ensure you have [Python 3.x](https://www.python.org/) installed on your machine.
2. Clone this repository or download the source code files.
3. Open your terminal or command prompt.
4. Run any of the individual scripts using the python command (e.g., `python lists_tuples.py`).
