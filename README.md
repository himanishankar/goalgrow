# GoalGrow 🌱

> Set a goal. Save smart. Watch it grow.

A command-line savings goal tracker built in Python. Set a goal with a deadline, log your savings, and see exactly how much to save each month to reach it on time.

## Features
- Create savings goals with a target amount and deadline
- Add savings anytime and see a live progress bar
- Automatic monthly saving suggestion
- Multiple goals supported
- Data saved locally in a JSON file
- Input validation and unit tests

## Tech Stack
- Python 3
- `json` module for storage
- `pytest` for testing

## How the Monthly Amount Is Calculated
**Monthly saving needed** = (Target − Already saved) ÷ Months left

Months left is the number of days until the deadline divided by 30.44, rounded up.

## Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/goalgrow.git
cd goalgrow
pip install -r requirements.txt
python main.py
```

## Run Tests
```bash
pytest
```

## Sample Output
```
Goal: Laptop
   [#####---------------] 25.0%
   Saved ₹15,000.00 of ₹60,000.00
   Deadline: 2027-06-20 (8 months left)
   Save ₹5,625.00 per month to reach it on time.
```

## Project Structure
```
goalgrow/
├── main.py          # menu and user interaction
├── goals.py         # goal logic and calculations
└── tests/           # unit tests
```

## Future Improvements
- Add charts for savings progress
- Build a web version with Flask
- Add reminders for monthly savings
- Support multiple currencies

## Author
Himani Shankar, CSE Student, DBIT Bengaluru
[GitHub](https://github.com/YOUR_USERNAME)

## License
MIT License