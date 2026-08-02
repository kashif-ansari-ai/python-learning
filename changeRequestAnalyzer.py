import pprint
#list of changes

change_request =[]

change1 = {"change_id": "CHG0012","application": "whatsapp", "risk": "Medium",
           "owner": "Kashif", "status":"Completed"}
change2 = {"change_id": "CHG0021","application": "google", "risk": "High",
           "owner": "Arbia","status": "Pending"}

change3 = {"change_id": "CHG0041","application": "windows", "risk": "Low",
           "owner": "Kashif","status":"Pending"}

change_request.append(change1)
change_request.append(change2)
change_request.append(change3)

#printing all the change requests.
print("all changes")
pprint.pprint(change_request)

##printing the applications names for all the changes.
for items in change_request:
    print(items["application"])


#updating risk of a change. Lets say change number 2

change_request[1]["risk"]="None"

print(change_request[1])

#adding a new key to all the changes.
for items in change_request:
    items["priority"] ="High"


print(change_request)



#printing only Low risk changes.
print("SHows only Low risk changes")

for items  in change_request:
    if items["risk"] == "Low":
        print(items)

#count the number of pending and complete changes.

pending = 0
completed = 0
for items in change_request:
    if items["status"] == "Pending":
        pending+= 1
    elif items["status"] == "Completed":
        completed+= 1

print("Pending changes " + str(pending) +"\n" + "Completed changes " + str(completed))  

#CHanges where owner is Kashif
for change in change_request:
    if change["owner"] == "Kashif":
     print(change)
