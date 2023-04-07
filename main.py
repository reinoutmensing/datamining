# Data Mining Techniques
# Reinout Mensing, Margot Boekema, Koen Smallegange 
# april 2023
# ---------------------------------------------------------------------------------------------------------

import csv
import matplotlib.pyplot as plt 

# Open the CSV file and create a CSV reader object
with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')

    # do not include the header in the list
    next(reader)

    # Create empty lists to store the data for each column
    tracker_l = []
    timestemp_l = []
    programme_l = []
    courses_ml_l = []
    courses_rtvl_l = []
    courses_stats_l = []
    courses_dbs_l = []
    gender_l = []
    chatGPT_l = []
    birthday_l = []
    estimate_no_students_l = []
    stood_up_l = []
    stress_level_l = []
    sports_pweek_l = []
    random_number_l = []
    bedtime_l = []
    goodday_1_l = []
    goodday_2_l = []


    # Loop through each row in the CSV file and add data to corresponding list 
    count = 0
    for row in reader:
        timestemp_l.append(row[0])
        programme_l.append(row[1])
        courses_ml_l.append(row[2])
        courses_rtvl_l.append(row[3])
        courses_stats_l.append(row[4])
        courses_dbs_l.append(row[5])
        gender_l.append(row[6])
        chatGPT_l.append(row[7])
        birthday_l.append(row[8])
        estimate_no_students_l.append(row[9])
        stood_up_l.append(row[10])
        stress_level_l.append(row[11])
        sports_pweek_l.append(row[12])
        random_number_l.append(row[13])
        bedtime_l.append(row[14])
        goodday_1_l.append(row[15])
        goodday_2_l.append(row[16])
       
        # give each entry in the data set a refrence index 
        tracker_l.append(count)
        count += 1


# do something with data 
plt.scatter(tracker_l, estimate_no_students_l, marker = 'o', s = 5, alpha = 0.75)
plt.yticks([]) 
plt.show()


