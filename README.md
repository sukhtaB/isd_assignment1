# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Sukhtab Singh Warya

## Assignment
Assignment1: Classes, Encapsulation and Unit Test Planning.
In this assignment you will leverage the knowledge gained in Module 01 to develop classes to support a larger system. This is the first of many assignments in this course, each of which will build on the previous assignment in order to produce a complete system. The focus of this assignment aligns with the focus of the first module - that is, classes, encapsulation and unit test planning.

## Encapsulation
Encapsulation is about keeping the details of how an object works hidden and only allowing access through specific methods.

1. Private Data: BankAccount keeps its balance private, not directly accessible from outside the class.
2. Controlled Access: Balance can only be changed through methods like deposit() and withdraw().
3. Data Protection: Encapsulation ensures data integrity by preventing unauthorized access and modifications.
4. Secure Methods: The Transaction class also hides its internal details and exposes only necessary methods.

## Assignment2: 
This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

## Polymorphism
In our banking app, we utilize polymorphism to allow different account types to handle service charges in their own specific ways. Each account type—ChequingAccount, SavingsAccount, and InvestmentAccount—derives from a base class called BankAccount.

Key Points:
- Method Overriding: Each subclass defines its own version of the get_service_charges method. For example:
  - ChequingAccount calculates charges based on overdraft limits.
  - SavingsAccount imposes higher fees if the balance is below a certain minimum.
  - InvestmentAccount may waive fees depending on how long the account has been open.

- Dynamic Behavior: When the get_service_charges method is called on an account, Python dynamically determines which subclass method to use based on the account type. This approach allows for flexible and reusable code, as the correct method is executed automatically.


## Assignment3
This assignment will address issues associated with the scalability and maintainability of the current service charge calculation functionality. If PiXELL River Financial decided to add several new account types each with their own formula for calculating service charges, several issues could begin to arise such as bloated subclasses, duplication of functionality, and with each potential change to service charge policy, the need to update every subclass. As such, this current polymorphic solution is not scalable. In this assignment the Strategy Pattern will be applied to simplify and add scalability to the service charge functionality. In addition, the Observer Pattern will be introduced. Using the Observer Pattern a client will be notified whenever a large transaction takes place and/or whenever an account balance drops below a minimum value.

## Strategy
The Strategy Pattern is used to manage different service charges for various account types. By setting up specific service charge strategies like OverdraftStrategy, ManagementFeeStrategy, and MinimumBalanceStrategy, the app can apply different fee calculations based on how the account is used and its rules. This setup makes it easy to add or update service charge strategies without changing the main account classes much.

Here are the classes that use the Strategy Pattern:
- ServiceChargeStrategy: The base class with the calculate_service_charges method.
- OverdraftStrategy: For Chequing Accounts to add overdraft fees.
- ManagementFeeStrategy: For Investment Accounts to calculate fees based on how long the account has been open.
- MinimumBalanceStrategy: For Savings Accounts to apply fees if the balance is too low.

## Observer
The Observer Pattern is used to send real-time notifications to clients about important account activities. Clients (Observers) are linked to accounts (Subjects) and get alerts when things like low balances or big transactions happen. This pattern makes it easy to manage notifications, so clients stay informed without changing the account classes.

Here are the classes that use the Observer Pattern:
- Observer: The base class for things that respond to notifications.
- Client: A specific observer that listens for changes in their accounts and gets email notifications.
- Subject: Keeps a list of observers (clients) and tells them about important changes.


## Assignment4
This assignment will incorporate a Graphical User Interface (GUI) into the PiXELL-River Financial banking system. The end product will include a lookup window from which users can view existing Client and corresponding Bank Account data. The user can then select a Bank Account and perform deposit and withdraw transactions against the selected Bank Account. PySide6 will be used to produce the windows and the design of these windows will be given so that students can focus on implementing the Event Driven Programming Paradigm into their existing set of classes.

## Assignment5
In this assignment we will incorporate a filtering algorithm into the GUI application such that the user may filter the bank account listing based on user-defined criteria. Additionally, the project will be wrapped up by generating html help files for each of the classes based on the docstrings coded throughout the semester. As well, the project will be packaged up into a user-friendly installer such that it may be distributed to users.


# PiXELL-River Financial System

## Overview
The PiXELL-River Financial System is a user-friendly application designed to manage clients, bank accounts, and transactions. It incorporates key features such as client lookup, account details management, and robust filtering functionality for improved usability and efficiency.

---

## Features

- **Client Lookup**: Search and display client information and associated bank accounts based on the client number.
- **Account Management**: View account details, update balances, and log transactions.
- **Filtering**: Easily refine account listings based on specific criteria (explained below).

---

## Filtering

### Purpose
The filtering functionality allows users to refine the list of bank accounts displayed, making it easier to locate specific accounts or information. This feature enhances the user experience by providing a quick and efficient way to search through account data.

### How It Works
1. **Filter Criteria**:
   - Users can select a filter criterion (e.g., Account Number, Balance, Date Created) using a dropdown menu.
2. **Filter Value**:
   - Enter the desired value in the filter input field.
3. **Apply Filter**:
   - Click the **"Apply Filter"** button to display only the rows in the table that match the filter criteria.
4. **Reset Filter**:
   - Click the **"Reset"** button to clear the filter and restore the full table.

### Implementation
The filtering functionality was implemented using PyQt and includes:
- A dropdown menu (filter_combo_box) for selecting the filter criterion.
- A text input field (filter_edit) for entering the filter value.
- A button (filter_button) that toggles between **"Apply Filter"** and **"Reset"** based on the current state.
- Dynamic table updates to show or hide rows that match the filter criteria.

### Example Usage
1. Enter a valid **Client Number** and click **Lookup Client**.
2. View the associated bank accounts in the table.
3. Select **"Balance"** in the filter dropdown menu.
4. Enter a value (e.g., 1000) in the filter input field and click **Apply Filter**.
5. The table will display only the accounts with a balance matching 1000.
6. Click **Reset** to restore the full table.

---

## Installation
To install and run the application:
1. Run the installer PixellAccountManager-installer.exe provided.
2. Follow the on-screen instructions to complete the installation.
3. Launch the application via the desktop shortcut or start menu.

---

## Documentation
Detailed documentation, including all classes and methods, is available in the `docs/` directory or can be viewed online at [Documentation Link].

---

## Contributors
- **Sukhtab Singh Warya**

---

## License
This project is licensed under the terms outlined in the `license.txt` file.
