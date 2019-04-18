import datetime

food_time = (16, 39)
current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
while (food_time != current_time):
    current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
print("Time for food!")