import pytest
from project import validate_time, optimal_time, hours_of_sleep

def main():
   validate_time()
   optimal_time()
   hours_of_sleep()


def test_valid_time_valueError():
   with pytest.raises(ValueError):
      validate_time("cat")


def test_valid_time():
   assert validate_time("5:45 am") == "05:45"
   assert validate_time("3:00 pm") == "15:00"


def test_optimal_time():
   assert optimal_time("5:45", 6, "W") == "08:45 PM"
   assert optimal_time("6:30", 5, "W") == "11:00 PM"
   assert optimal_time("22:30", 6, "S") == "07:30 AM"
   assert optimal_time("22:30", 4, "S") == "04:30 AM"



def test_hours_of_sleep():
   assert hours_of_sleep("5:45", "8:45 PM", "W") == "9:00"
   assert hours_of_sleep("5:45", "1:15 AM", "W") == "4:30"
   assert hours_of_sleep("22:30", "7:30 AM", "S") == "9:00"
   assert hours_of_sleep("22:30", "6:00 AM", "S") == "7:30"


if __name__ == "__main__":
    main()