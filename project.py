import re
from tabulate import tabulate
from datetime import datetime, timedelta

#Constant for sleep cycle, time of 90 minutes
SLEEP_CYCLE = 90

def main():
    print("\nSleep Cycle Calculator")
    action = get_input()
    #prompt for desire time
    while True:
        try:
            desire_time = validate_time(input("enter desired time: "))
            break
        except:
            print("\nInvalid time, Usage: HH:MM AM|PM")

    #initial list and cycle
    hours = []
    cycle = 6

    while cycle > 2:
        h = optimal_time(desire_time, cycle, action)
        hsleep = hours_of_sleep(desire_time, h, action)
        hour = {"Hour": h, " Number of Cycles": f"{cycle} cycles for {hsleep} hours of sleep "}
        hours.append(hour)
        cycle -= 1
    if action == "W":
        print("\nYou should try to fall asleep at one of the following times: ")
    if action == "S":
        print("\nYou should try to wake up at one of the following times: ")

    print(tabulate(hours, headers="keys", tablefmt="rounded_outline"))
    print("Try to aim for 7-9 hours of sleep")
    print("keep in mind that The average human takes fourteen minutes to fall asleep, so plan accordingly!\n")


def get_input():
    instructions = [{"Key": "W", "Action": "Choose wake up time"},
                    {"Key": "S", "Action": "Choose sleep time"}]

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        action = input("What do you want to do?: ").upper()

        if action in ["W", "S"]:
            return action
        else:
            print("Invalid key, try again.")


#Validates input time
def validate_time(time):
    wake_time = re.search(r"^(1[0-2]|0?[1-9]):?([0-5]?[0-9])? (AM|PM)$", time, re.IGNORECASE)
    if wake_time:
        hour, minutes, meridiem = int(wake_time.group(1)), wake_time.group(2), wake_time.group(3)
        ##chage to 24H format:
        if meridiem.upper() == "PM":
            hour += 12
        ##change 12 AM to 00:00
        if hour == 12 and meridiem == "AM":
            hour = 00
        ##if no input for minutes format to 00
        if minutes == None:
            minutes = 0
        return f"{hour:02}:{minutes:02}"
    else:
        raise ValueError

# calculates optimal time to go to sleep or wake up
def optimal_time(input_time, cycle, action):
    i = cycle
    meridiem = "AM"
    time = datetime.strptime(input_time, '%H:%M')
    #calculates sleep hour
    if action == "W":
        final_time = time - timedelta(minutes=(SLEEP_CYCLE*i))
    #calculates wakeup hour
    if action == "S":
        final_time = time + timedelta(minutes=(SLEEP_CYCLE*i))
    hour, minutes, seconds = str(final_time.time()).split(":")
    #change 24H format to 12H
    if int(hour) > 12:
        hour = int(hour) - 12
        meridiem = "PM"

    return f"{hour:02}:{minutes:02} {meridiem}"


# calculates total hours of sleep
def hours_of_sleep(input_time, final_time, action):
    time1 = datetime.strptime(input_time, '%H:%M')
    time2 = datetime.strptime(final_time, '%H:%M %p')

    if action == "W":
        diff = timedelta(hours=(time1.hour - time2.hour), minutes=(time1.minute - time2.minute))
    if action == "S":
        diff = timedelta(hours=(time2.hour - time1.hour), minutes=(time2.minute - time1.minute))

    #transform the timedelta object to a str and use a re to catch the hour
    if time_diff := re.search(r"([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$", str(diff)):
        hour, minutes, = int(time_diff.group(1)), time_diff.group(2)
        if hour > 12:
            hour -= 12

    return f"{hour}:{minutes}"


if __name__ == "__main__":
    main()