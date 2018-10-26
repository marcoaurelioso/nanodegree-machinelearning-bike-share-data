
# coding: utf-8

# import all necessary packages and modules
import math # access to the mathematical functions
import csv # read and write csv files
import matplotlib.pyplot as plt # collection of command style functions that make matplotlib work like MATLAB

# Script functions
def load_csv_file(file_path): 
    """
    Function to load a CSV file.
    Args:
        (str) file_path: A csv file path
    Return:
        (list) A list with all rows from csv file
    """
    with open(file_path, "r") as file_read:
        return list(csv.reader(file_read))

# Let's read the data as a list
print("Reading the document...")
data_list = load_csv_file("chicago.csv")
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")

# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(1,21):
    print("{}. {}".format(i, data_list[i]))

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows
# columns: Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
print("\nTASK 2: Printing the genders of the first 20 samples")
for i in range(0,20):
    print("{}. {}".format(i, data_list[i][-2]))

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Function that gets a list and returns a particular column(list) specified by the index
    Args:
        (list) data: The list
        (int) index: The index that wich indicates the position of the column
    Return:
        A list with the items of the specified column
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for row in data:
        column_list.append(row[index])    
    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
# columns: Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
male = 0
female = 0
for elem in data_list:
    if elem[-2] == "Male":
        male += 1
    elif elem[-2] == "Female":
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Function to count the genders of a list
    Args:
        (list) data_list: The list
    Returns:
        (list) A list with 2 columns, the first is males count, and the second is females count.
    """    
    male = 0
    female = 0
    for elem in data_list:
        if elem[-2] == "Male":
            male += 1
        elif elem[-2] == "Female":
            female += 1
    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Function to get the most popular gender and return the gender as string
    Args:
        (list) data_list: The list
    Returns:
        (str) The answer as "Male", "Female" or "Equal"
    """    
    answer = ""
    # Male (index 0); Female (index 1)
    genders = count_gender(data_list)
    if genders[0] > genders[1]: 
        answer = "Male"
    elif genders[0] < genders[1]: 
        answer = "Female"
    else:
        answer = "Equal"
    return answer

print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
print("Check the chart!")
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
# columns: Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
def count_user_types(data_list):
    """
    Function to count the User Type of a list
    Args:
        (list) data_list: The list
    Returns:
        (list) A list with 2 columns, Customer count and Subscriber count
    """    
    customer = 0
    subscriber = 0
    for row in data_list:
        if row[-3] == "Customer":
            customer += 1
        elif row[-3] == "Subscriber":
            subscriber += 1
    return [customer, subscriber]

print("\nTASK 7: Check the chart!")
user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Types')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because some users did not provide their gender. So the sum without missing data will not work."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
# columns: Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def calc_median(data_list):
    """
    Function to find the median of a list 
    Args:
        (list) data_list: The list
    Returns:
        (int) return the average of the middle two.
    """       
    half = len(data_list) // 2
    data_list.sort()
    if not len(data_list) % 2:
        return (data_list[half - 1] + data_list[half]) / 2.0
    return data_list[half]

trip_duration_list_int = [int(x) for x in trip_duration_list]
trip_duration_list_int_sorted = sorted(list(trip_duration_list_int))
min_trip = trip_duration_list_int_sorted[0]
max_trip = trip_duration_list_int_sorted[-1]
mean_trip = sum(trip_duration_list_int_sorted) / len(trip_duration_list_int_sorted)
median_trip = calc_median(trip_duration_list_int)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
# columns: Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
user_types = set(column_to_list(data_list,3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
#    """
#   Example function with annotations.
#    Args:
#        param1: The first parameter.
#        param2: The second parameter.
#    Returns:
#        List of X values
#    """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """
    Function to count types of a specific column
    Args:
        (list) column_list: A list of columns
    Return:
        A tuple with types and amount of occurrences
    """    
    item_types = []
    count_items = []
    item_types = list(set(column_list))
    count_items = [column_list.count(t) for t in item_types]
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------

print("\nFinish")