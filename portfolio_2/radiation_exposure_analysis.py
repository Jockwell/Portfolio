'''Radiation Exposure Analysis'''

import statistics

# Assign the existing data to variables.
locations = ["City Center", 
            "Industrial Zone", 
            "Residential District", 
            "Rural Outskirts", 
            "Downtown" 
            ]
radiations = [[22, 19, 20, 31, 28],
             [35, 32, 30, 37, 40],
             [15, 12, 18, 20, 14],
             [9, 13, 16, 14, 7],
             [25, 18, 22, 21, 26]
             ]

# Ask the user to input any new data to be addded.
new_location = input('''Please enter the new location you took radiation
readings from (enter 'none' if you have no new readings): ''')

if new_location.lower() != "none":
    locations.append(new_location)

new_radiation_list = []
while True:
    user_measurements = input("Enter radiation level or 'done' to finish: ")
    if user_measurements.lower() == "done":
        print("Exiting loop.")
        break
    try:
        new_radiation_list.append(int(user_measurements))
        print(f"Added radiation reading: {user_measurements}")
        print(new_radiation_list)
    except ValueError:
        print("Invalid input, please enter a number")

radiations.append(new_radiation_list)

for i, locations in enumerate(locations):
    print(f"Processing {locations}")
    average = sum(radiations[i]) / len(radiations[i])
    standard_deviation = statistics.stdev(radiations[i])
    print(f'''
Radiation Levels: {radiations[i]},
Average: {average},
Standard Deviation: {standard_deviation}
''')
