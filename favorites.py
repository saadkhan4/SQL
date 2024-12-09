import csv

with open("Devices.csv" , "r") as file:      # dictreader automatically analize the first line form you  
    reader = csv.DictReader(file)            # figures out what are the column called. 
    next(reader)                             # it means give me the next line.
    for row in reader:
        print(row["Language"])


# ANOTHER WAY USING LOOP IN PYTHON.

with open("Devices.csv" , "r") as file:
    reader = csv.DictReader(file)
    scratch, c ,python  = 0,0,0
  
for row in reader:
    Devices = row["Language"]
    if Devices == 'scratch':
        scratch += 1
    elif Devices == 'c':
        c += 1
    elif Devices == 'python':
        python += 1
                
print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")


