# create a program which takes input csv files, reads it, outputs a csv file
# adds a new column to the output csv file,"attention_reason" and based on the change
# writes High Risk, Database change, High Risk; Database change


#create a function process_changes(input_csv , output_csv)

def process_changes(change_requests, output_file):

    with open(output_file, "w", newline ="") as change_analysis:
        


        with open(change_requests, "r") as requests:
            change_reader = csv.DictReader(requests)

            fieldnames = change_reader.fieldnames
            fieldnames.append("attention_reason")
            fieldnames.append("priority")

            change_writer =  csv.DictWriter(change_analysis, fieldnames = fieldnames)
            change_writer.writeheader()
            priority = ""
            for change in change_reader:
                priority = determine_priority(change)
                #print(priority)

                if change["risk"] == "High" and change["change_type"] =="Database":
                    change["attention_reason"] = "High Risk; Database Change"
                    change["priority"] = priority
                elif change["risk"] == "High":
                    change["attention_reason"] = "High Risk"
                    change["priority"] = priority
                elif change["change_type"] == "Database":
                    change["attention_reason"] = "Database Change"
                    change["priority"] = priority
                else:
                    continue
                change_writer.writerow(change)

# create a function to determine the priority of the change(dictionary)
def determine_priority(change):
    priority = ""
    if change["risk"] == "High" and change["change_type"] == "Database":
        priority = "Critical"
    elif change["risk"] == "High" or change["change_type"] == "Database":
        priority = "High"

    return priority

import csv
process_changes("exercises\\change_requests.csv", "exercises\\change_attention_reason.csv")