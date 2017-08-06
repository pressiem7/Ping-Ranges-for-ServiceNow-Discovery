#Ping Range 1.2
#Pings a /16 one /24 at at time, stops when it hits a host and logs that there are pingable hosts in that /24 and moves to the next. 
#Output is in the format required to import into ServiceNow for Discovery
import os
import csv
print ("This script will ping through a /16 network and output the /24 networks that contain pingable hosts in a csv file on the desktop")
filename = raw_input("Enter the filename you would like to save the CSV as without the extension: ")
network = raw_input("Enter the /16 network with only one period. EX 192.168: ")
third_octet = int(raw_input("Set the third octet value from 0 to 255. If you would like to ping the entire range, enter 0: "))
username = os.getenv('username')
file = open("C:/Users/" + username + "/Desktop/" + filename + ".csv", "wb")
writer = csv.writer(file, delimiter=',')
writer.writerow(["RangeName", "IP", "mask", "type"])
file.close()
while third_octet < 256:
    for host in range (0, 255): 
        y = os.system("ping -n 1 -w 300 " + network + "." + str(third_octet) + "." + str(host))
        if y == 0:
            file = open("C:/Users/" + username + "/Desktop/" + filename + ".csv", "ab")
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["", network + "." + str(third_octet) + ".0", "24", "IP Network"])
            file.close()
            break
    third_octet = third_octet + 1

#Improvements: 
#Input error handling
#Fork of this script that records pings for each host and does not break upon first success
