import csv
import os

firstLine = True
newList=[]
name = []
fName = []
lName = []
date = []
ssn = []
newRow = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empFile = os.path.join("employee_data1.csv")

with open(empFile, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ",")

    newFile = os.path.join("EmployeeInfo.csv")
    with open(newFile, 'w', newline="") as csvfile:
        fieldnames = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'States']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:

            #Split the names such that the new list 'name' has name[0] = first name and name[1] = last name
            name = str(row['Name']).split(" ")
            fName = name[0]
            lName = name[1]

            #Split the SSN and extract the last 4 digits(ssn[2])
            ssn = str(row['SSN']).split("-")
            newSSN = "***-**-"+ssn[2]

            #Abbreviate the state names like: us_state_abbrev[row['State']]

            writer.writerow({"Emp ID":row["Emp ID"], "First Name":fName, "Last Name": lName, "DOB": row["DOB"], "SSN": newSSN,
                         "States": us_state_abbrev[row['State']]})


