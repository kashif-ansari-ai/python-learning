#first attempt to create change_processor. 

# import csv

# with open("exercises\\change_requests.csv") as change_requests:
#     change_reader = csv.DictReader(change_requests)

#     for change in change_reader:
#         print(change["id"], " - ", change["application"])
#         if change["risk"] == "High":
#             print((change["risk"]).upper(), " RISK: ", change["id"], " - ", change["application"])



# Creating the above solution using functions to make it more reusable and professional.

#Creating the function process_changes()
def process_changes(change_requests, risk_type):
    with open(change_requests, "r") as requests:
        change_reader = csv.DictReader(requests)

        for change in change_reader:
            print(change["id"], " - ", change["application"])

            if change["risk"] == risk_type:
             print(change["risk"].upper(), " RISK: ", change["id"], " - ", change["application"])


import csv

process_changes("exercises\\change_requests.csv", "Low")



#Created below code as the previous just above this
# failed due to incorrect scope. I put the for loop outside with block, so the file was closed
# and could not be processed. I understood while getting my code reviewed and solved it on my own.

#Below code works fine but the file is now hardcoded and it is not much reusable.

# def process_changes(change_requests, risk_type):     
#     change_reader = csv.DictReader(change_requests)

#     for change in change_reader:
#         print(change["id"], " - ", change["application"])
#         if change["risk"] == risk_type:
#             print((change["risk"]).upper(), " RISK: ", change["id"], " - ", change["application"])
# import csv

# with open("exercises\\change_requests.csv","r") as change_requests:
#     process_changes(change_requests, "Low")