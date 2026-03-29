# Expense Splitter

## Overview

Managing shared expenses between friends can get confusing when multiple people are paying at different times. This project is a simple program that helps calculate who owes whom and reduces the number of payments required to settle everything.

---

## How It Works

The program takes a list of transactions from the user. Each transaction is entered in the format:

Giver Receiver Amount

For example:
A B 100

This means A gives ₹100 to B.

The program then calculates the net balance for each person and uses a greedy approach to minimize the number of final transactions.

---

## Features

- Simple input system with validation  
- Prevents incorrect formats and invalid values  
- Calculates net balances for each person  
- Minimizes number of transactions using a greedy method  
- Displays clear output like:  
  A pays B ₹50  

---

## How to Run

## Requirements

- Python 3 installed

To check:
python --version

## Setup

Download the project from GitHub and extract it.

Or clone using:

git clone https://github.com/incompetant-jellyfish/expense-splitter

## Navigate to folder

Open terminal and go to the project folder:

cd expense-splitter

## Then

1. Open terminal in the project folder  
2. Run the program: python src/main.py
3. Enter the number of transactions  
4. Enter each transaction in the required format  

## Input Format

Enter number of transactions

Then enter each transaction as:

Giver Receiver Amount

Example:
A B 100

---

## Example

Input:
A B 100  
B C 50  
C A 30  

Output:
A pays B ₹50  
A pays C ₹20  

---
<img width="500" height="595" alt="image" src="https://github.com/user-attachments/assets/fe8ec279-e173-4c68-91ce-caaf52572bed" />

## Concepts Used

- Greedy Algorithm  
- Dictionaries (for storing balances)  
- Sorting  
- Input Validation  

---

## Notes

While building this project, handling user input correctly was one of the main challenges. Initially, the format was unclear, but it was improved by adding validation and clearer prompts.

---

## Future Improvements

- Add support for group expense splitting  
- Store transactions in a file  
- Build a simple user interface  

