def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm unavailable!")

    return wrapper


@check_working_hours
def sweep_floors(time):
    print("I am at work")


sweep_floors(2000)
