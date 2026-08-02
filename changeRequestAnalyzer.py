import pprint

#########################
  #  Functions #
#########################

#displays all the changes in a change list.
def display_all_changes(changes_list):
    for change in changes_list:
        print(change)


def display_application_names(change_list):
    for change in change_list:
        print(change["application"])

def display_changes_by_owner(change_list,owner):
    for change in change_list:
        if change["owner"] == owner:
            print(change)

#Display change by Risk.
def display_changes_by_risk(change_list,risk):
    for change in change_list:
        if change["risk"] == risk:
            print(change)


#Display count of changes by Status.

def count_status(change_list):
    pending = 0
    completed = 0
    for change in change_list:
      if change["status"] == "Pending":
        pending+= 1
      elif change["status"] == "Completed":
        completed+= 1
    print("Pending changes " + str(pending) +"\n" + "Completed changes " + str(completed)) 


#############

# Change List #

change_request =[]

change1 = {"change_id": "CHG0012","application": "whatsapp", "risk": "Medium",
           "owner": "Kashif", "status":"Completed"}
change2 = {"change_id": "CHG0021","application": "google", "risk": "High",
           "owner": "Arbia","status": "Pending"}

change3 = {"change_id": "CHG0041","application": "windows", "risk": "Low",
           "owner": "Kashif","status":"Pending"}

change_request = [change1,change2,change3]


#####################

#     Main Program  #

####################


#updating risk of a change. Lets say change number 2

change_request[1]["risk"]="None"

print(change_request[1])

#adding a new key to all the changes.
for items in change_request:
    items["priority"] ="High"


print(change_request)



#displays all change requests.
display_all_changes(change_request)

#displays the applications for the changes
display_application_names(change_request)

#print(change)
#print(type(change))
#display changes by owner name
display_changes_by_owner(change_request,"Kashif")

#display changes by risk
display_changes_by_risk(change_request,"Low")   

#display changes count by status
count_status(change_request)