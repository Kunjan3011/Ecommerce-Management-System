import mysql.connector

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="123",  # Replace with your MySQL password
    database="ecommerce_db"  # Ensure this database is created in MySQL Workbench
)
cursor = conn.cursor()


# Create tables if not exists
def setup_database():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock INT NOT NULL,
        category VARCHAR(255) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        total_amount DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderDetails (
        order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        product_id INT,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
    ''')
    print("Database setup complete.")


# Feature: Add a product to the inventory
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    category = input("Enter product category: ")

    query = '''
    INSERT INTO Products (name, price, stock, category) 
    VALUES (%s, %s, %s, %s)
    '''
    values = (name, price, stock, category)

    cursor.execute(query, values)
    conn.commit()
    print("Product added successfully!")


# Feature: View all products
def view_products():
    query = "SELECT * FROM Products"
    cursor.execute(query)
    products = cursor.fetchall()

    print("\nAvailable Products:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}, Category: {product[4]}")


# Feature: Add a customer
def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    query = '''
    INSERT INTO Customers (name, email) 
    VALUES (%s, %s)
    '''
    values = (name, email)

    cursor.execute(query, values)
    conn.commit()
    print("Customer added successfully!")


# Feature: Place an order
def place_order():
    customer_id = int(input("Enter customer ID: "))
    total_amount = 0
    order_items = []

    while True:
        product_id = int(input("Enter product ID (or 0 to finish): "))
        if product_id == 0:
            break
        quantity = int(input("Enter quantity: "))

        # Fetch product details
        query = "SELECT price, stock FROM Products WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()

        if product and product[1] >= quantity:
            price = product[0] * quantity
            total_amount += price
            order_items.append((product_id, quantity, price))

            # Update stock
            update_query = "UPDATE Products SET stock = stock - %s WHERE product_id = %s"
            cursor.execute(update_query, (quantity, product_id))
        else:
            print("Insufficient stock or invalid product ID.")

    # Insert order
    query = "INSERT INTO Orders (customer_id, total_amount) VALUES (%s, %s)"
    cursor.execute(query, (customer_id, total_amount))
    order_id = cursor.lastrowid

    # Insert order details
    for item in order_items:
        detail_query = '''
        INSERT INTO OrderDetails (order_id, product_id, quantity, price) 
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(detail_query, (order_id, item[0], item[1], item[2]))

    conn.commit()
    print(f"Order placed successfully! Total Amount: {total_amount}")


# Feature: View all orders
def view_orders():
    query = '''
    SELECT o.order_id, c.name AS customer_name, o.order_date, o.total_amount
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    '''
    cursor.execute(query)
    orders = cursor.fetchall()

    print("\nOrders:")
    for order in orders:
        print(f"Order ID: {order[0]}, Customer: {order[1]}, Date: {order[2]}, Total Amount: {order[3]}")


# Menu-Driven CLI
def show_menu():
    print("\nEcommerce Management System")
    print("1. Add a Product")
    print("2. View Products")
    print("3. Add a Customer")
    print("4. View Customers")
    print("5. Place an Order")
    print("6. View Orders")
    print("7. Exit")


# Main program
if __name__ == "__main__":
    setup_database()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            print("Feature not implemented yet.")  # Placeholder for future enhancement
        elif choice == "5":
            place_order()
        elif choice == "6":
            view_orders()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")