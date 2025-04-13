

# Ecommerce Management System

## Project Updates
For the latest version of this project, visit:



## Project Overview

The **Ecommerce Management System** is a Python-based application integrated with a MySQL backend, designed to streamline the management of inventory, customers, and orders. It simulates key functionalities of a real-world ecommerce platform, focusing on CRUD operations, relational database design, and efficient workflows. This project highlights proficiency in backend development, database management, and Python programming.

## Features

- **Database Setup**:  
  - Automatically creates tables for `Products`, `Customers`, `Orders`, and `OrderDetails` with primary and foreign key relationships.

- **Inventory Management**:  
  - Add new products, view inventory, and update stock dynamically.

- **Customer Management**:  
  - Add and manage customer details with unique email validation.

- **Order Processing**:  
  - Place orders with real-time stock validation.
  - Calculate total order amounts and generate order records.

- **Order Tracking**:  
  - Retrieve and view order details, including customer information and total amounts.

## Technologies Used

- **Programming Language**: Python  
- **Database**: MySQL  
- **Libraries**: MySQL Connector for Python  

## Setup Instructions

### Prerequisites:
1. Install Python (version 3.8 or higher).
2. Install MySQL and MySQL Workbench.
3. Install the MySQL Connector for Python:
   ```bash
   pip install mysql-connector-python
   ```

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-management-system.git
   ```

2. Open MySQL Workbench and create a database named `ecommerce_db`.

3. Update the connection parameters (host, port, username, password, database name) in the Python script to match your MySQL setup.

4. Run the script to initialize tables and interact with the system via the menu-driven CLI.

## Usage

### Interaction:
- **Add Products**: Input product details such as name, price, stock, and category.  
- **View Products**: Fetch and display all products from the inventory.  
- **Add Customers**: Register customer details with email validation.  
- **Place Orders**: Choose customer IDs, add products with quantities, and process orders with automatic stock updates.  
- **View Orders**: Retrieve order history along with customer and product details.

### Running the Script:
1. Execute the Python file:
   ```bash
   python ecommerce_management_system.py
   ```
2. Use the CLI menu to select operations.

## Example Output

### Sample Order Placement:
```
Enter customer ID: 2
Enter product ID (or 0 to finish): 1
Enter quantity: 2
Enter product ID (or 0 to finish): 3
Enter quantity: 1
Order placed successfully! Total Amount: ₹2150.00
```

## Future Enhancements

- Implement customer authentication for personalized experiences.
- Add advanced reporting features like sales analysis and order trends.
- Integrate visualization tools (e.g., Power BI) for inventory and sales data insights.


---

## Contact

For questions, collaborations, or feedback, connect with me:  
- **LinkedIn**: [LinkedIn Profile](https://linkedin.com/in/kunjan-chittroda)  
- **GitHub**: [GitHub Profile](https://github.com/Kunjan3011)


