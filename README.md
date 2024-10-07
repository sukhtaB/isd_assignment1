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