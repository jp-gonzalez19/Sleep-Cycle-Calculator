# SLEEP CYCLE CALCULATOR
#### Video Demo:  <https://youtu.be/Fvs7seb2gDU>
## Description:
Sleep Cycle Calculator is my final project for CS50's Introduction to Programming with Python, I have always liked the idea of optimizing our mind and body, a few years back I came across some documentation about sleep cycles and how they affect our general feeling and rest. That's why I decided to make my own sleep cycle calculator

---
## Folder Contents:
- **project.py**: here is where the ```main``` function is located and all the other functions for the program to be implemented.
- **test_project.py**: This file contains the test functions for project.py.
- **requirements.txt**: All ```pip```-installable libraries that where used for this project are listed here.
---
## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate`
```
$ pip install tabulate
```
---
## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
- The program will prompt you to enter a key if you want to choose your wake up hour or choose your sleep hour.
- Then, you will be prompted to input the desired time.
- The program is going to validate that the time you gave is valid. If it's invalid, the program will print a message containing the usage method and format for the hour; then you will be re-prompted to input the hour.
- Finally, a table will appear containing the optimal hours for you to get up (or go to sleep), as well as the number of sleep cycles and the total hours you would sleep.

Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```
