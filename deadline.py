import datetime

user_input = input("Enter your goal with a deadline(dd.mm.yyyy) separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_left = deadline_date - today_date


print(f"Today's date is {today_date}")
print(f"Your deadline is {deadline_date}")
print(f"Your goal is {goal} and the time remaining are {time_left}")
