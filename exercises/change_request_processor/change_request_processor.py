# This program/component will verify the strucute of the change(dictionary) with the given schema.

import csv

# Schema for validating the change structure.

schema = {
    "Change ID": str,
    "Application": str,
    "Priority": str,
    "Approved": bool,
    "Risk Score": int
}


# Reading the input CSV file.

with open("exercises\\change_csv.csv", "r") as requests:
    change_reader =  csv.DictReader(requests)

    valid_change_for_processing = []
    invalid_changes = []
    priority_values =["High","Medium","Low"]
    for change in change_reader:
        invalid_record = False
        
        if change.keys() == schema.keys():
            for key,value in change.items():
                if change[key] == None:
                    invalid_record = True
                
            if not invalid_record:
        
                for key,value in change.items():
                    try:
                        if schema[key] == int:                    
                            change[key] = int(value)
                        if int(change["Risk Score"]) < 1 or int(change["Risk Score"]) > 10:
                            invalid_record = True
                            print("Risk Score validation failed for the change " +  change["Change ID"])
                            break
                    except ValueError:
                        invalid_record = True
                        print("Conversion error for int type for the change " +  change["Change ID"] + "\n")
                        break    
                    if schema[key] == bool:
                        if change[key].lower() == "true":
                            change[key] = True
                        elif change[key].lower() == "false":
                            change[key] = False
                        else:
                            invalid_record = True
                            print("Conversion error for bool type for the change " + change["Change ID"])
                            break
        if change["Priority"] not in priority_values:
                print("Change Validation failed for Priority key for the change, " + change["Change ID"])
                invalid_record = True        
        if not invalid_record:
            valid_change_for_processing.append(change)
        elif invalid_record:
            invalid_changes.append(change)

print("Valid changes for further processing are ")
for change in valid_change_for_processing:
    print(change)

print("invalid changes are " )
for change in invalid_changes:
    print(change)