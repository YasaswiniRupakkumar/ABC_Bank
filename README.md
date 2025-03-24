# ABC_Bank
A simple command-line banking system to manage customer accounts. Supports adding customers, viewing details, deposits, withdrawals, and updates. Built with Python, requiring no external dependencies. 

# ABC Bank - Command Line Banking System

## Overview
ABC Bank is a simple command-line banking system that allows users to manage customer accounts. It supports core banking functionalities such as adding new customers, viewing account details, making deposits and withdrawals, and updating customer information.

## Features
- **Add New Customers**: Register new customers with details such as NIC, name, date of birth, address, and phone number.
- **View Customer Details**: Retrieve and display details of a specific customer, including their bank balance.
- **View All Customers**: Display a list of all registered customers along with their balances.
- **Deposit Money**: Deposit funds into a customer's account.
- **Withdraw Money**: Withdraw funds from a customer's account while ensuring sufficient balance.
- **Update Customer Details**: Modify existing customer information such as name, address, and phone number.
- **Exit Option**: A simple exit prompt to close the application.

## Installation
### Requirements
- Python 3.x
- No additional dependencies required

### Running the Application
1. Clone or download the repository.
2. Open a terminal and navigate to the project folder.
3. Run the following command:
   ```sh
   python 20240284.py
   ```

## Usage
Upon running the script, a menu will be displayed with options:
1. Add a new customer
2. View details of a customer
3. View details of all customers
4. Deposit money
5. Withdraw money
6. Update customer details
7. Exit

### Example Commands
- To add a new customer, select option `1` and follow the prompts.
- To deposit money, select option `4`, enter the account number, and input the deposit amount.
- To withdraw funds, select option `5`, enter the account number, and specify the withdrawal amount.
- To exit the program, choose option `7`.

## Data Validation
- **NIC Format**: Must be 10 characters long, with the last character being 'V' or 'X'.
- **Phone Number Format**: Should follow Sri Lanka's format and be entered as `(+94) XXXXXXXX`.
- **Date Validation**: Ensures correct date format and valid birth years.
- **Account Number**: Must be exactly 10 digits.

## Limitations
- Supports only up to 5 customer accounts.
- Data is stored in memory and is lost upon exiting the program.

## Future Improvements
- Implement a persistent database for account storage.
- Add authentication for better security.
- Enhance the interface with a GUI.

## License
This project is open-source and free to use.

## Contributing
Feel free to fork the repository and contribute enhancements via pull requests.

