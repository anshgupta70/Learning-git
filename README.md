# ATM Machine in Python

A beginner-friendly, command-line ATM simulation built with Python. This project demonstrates core programming concepts through common ATM operations such as checking an account balance, depositing money, and withdrawing money.

> **Project status:** Learning project. This application is for educational purposes only and is not intended for real financial transactions.

## Features

- **Balance inquiry** — view the current balance.
- **Cash deposit** — add a positive amount to the balance.
- **Cash withdrawal** — withdraw money while checking the available balance.
- **Input validation** — reject invalid menu choices and non-positive transaction amounts.
- **Transaction counter** — count successful deposits and withdrawals.
- **Menu-driven interface** — continue performing operations until the user exits.

*Features listed above describe the intended improved version. Update this list if any feature has not yet been implemented in your current code.*

## Tech Stack

- **Language:** Python 3
- **Interface:** Command-line / terminal
- **Version control:** Git and GitHub

## Getting Started

### Prerequisites

- Python 3 installed on your computer
- Git installed (optional, if you want to clone the repository)

Check your Python installation:

```bash
python --version
```

On some systems, you may need to use `python3 --version` instead.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anshgupta70/Learning-git.git
   ```

2. Move into the project directory:

   ```bash
   cd Learning-git
   ```

3. Locate the ATM project file. If `Program.py` is in the repository root, run:

   ```bash
   python Program.py
   ```

   If the ATM project is inside a separate folder, navigate to that folder first and run the script there.

## How to Use

1. Start the program from your terminal.
2. Enter the PIN if prompted.
3. Select an option from the ATM menu.
4. Follow the prompts to check your balance, deposit money, or withdraw money.
5. Choose **Exit** to close the application.

## Example Session

```text
Welcome to ATM

--- ATM MENU ---
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit

Write your choice: 2
Enter deposit amount: 5000
Deposit successful!
Current Balance: 105000
```

*Your exact prompts and output may differ depending on your current implementation.*

## Validation and Testing Checklist

Use these cases to verify the program:

| Scenario | Expected behavior |
|---|---|
| Valid deposit | Balance increases by the deposited amount |
| Zero or negative deposit | Transaction is rejected |
| Valid withdrawal within balance | Balance decreases by the withdrawn amount |
| Withdrawal greater than balance | Transaction is rejected; balance stays unchanged |
| Zero or negative withdrawal | Transaction is rejected |
| Invalid menu choice | An error message is displayed |
| Successful deposit or withdrawal | Transaction counter increases by one |
| Balance inquiry | Balance is displayed without changing the transaction counter |

## Current Limitations

- The account balance is stored in memory and resets when the program exits.
- A PIN stored directly in source code is not secure for a real application.
- The project does not connect to a bank, payment gateway, or database.
- This is a single-user simulation and does not provide production-grade authentication, audit logs, or transaction persistence.

## Planned Improvements

- [ ] Add robust handling for non-numeric input.
- [ ] Limit the number of incorrect PIN attempts.
- [ ] Add a transaction history / mini statement.
- [ ] Split operations into reusable functions.
- [ ] Persist account data and transactions using SQLite.
- [ ] Add automated tests for transaction and validation logic.

## Concepts Practiced

- Variables and data types
- User input and output
- `if` / `elif` / `else` conditional statements
- `while` loops and `break` / `continue`
- Arithmetic and assignment operators
- Input validation and exception handling
- Basic Git workflow: add, commit, and push

## Contributing

This is a personal learning project. Suggestions and constructive feedback are welcome. If you spot a bug or have an improvement idea, feel free to open an issue or submit a pull request.

## Author

**Ansh Gupta**

- GitHub: [@anshgupta70](https://github.com/anshgupta70)

## License

No license has been specified yet. Unless a license is added to the repository, others should not assume they have permission to reuse, modify, or distribute this project.
