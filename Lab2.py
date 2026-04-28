# print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()

    str_list = user_input.split(",")

    num_list = []
    for item in str_list:
        num_list.append(float(item))

    return num_list

def calc_average_temperature(num_list):
    average = sum(num_list) / len(num_list)
    return average

def calc_min_max_temperature(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    return [min_temp, max_temp]

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print("ET0735 Lab 2")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)

    average = calc_average_temperature(num_list)
    print("Average temperature = " + str(average))

    min_max = calc_min_max_temperature(num_list)
    print("Minimum temperature = " + str(min_max[0]))
    print("Maximum temperature = " + str(min_max[1]))


if __name__ == "__main__":
    main()