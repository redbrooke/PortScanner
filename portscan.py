#!/bin/python3

def logo():
	print("""

######                                                                 
#     #  ####  #####  #####       ###### # #    # #####  ###### #####  
#     # #    # #    #   #         #      # ##   # #    # #      #    # 
######  #    # #    #   #   ##### #####  # # #  # #    # #####  #    # 
#       #    # #####    #         #      # #  # # #    # #      #####  
#       #    # #   #    #         #      # #   ## #    # #      #   #  
#        ####  #    #   #         #      # #    # #####  ###### #    # 
       __A__
        (")__
       /)_ \_L_
     _//  \_  _~~---\/~|
   ^~^^^^^^^^^ ~\ \^^^^^^^^^^^^^^^^^^^^
                ( ;
                {_\		
	
The slowest port-scanner in the west.....
""")


import sys #imports system functions.
import socket
from datetime import datetime as dt #importing something, giving it a new alias (name)

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid IP")
	sys.exit()


logo()
print("-" * 30)
print("scanning " + target)  						
print("Starting at: "+ (str(dt.now())))
#Scanning:----------------------------------------------------------------------------------------------------------------------------
try:	
	for port in range(1, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result=s.connect_ex((target,port))
		print("checking port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()
#error handleing:---------------------------------------------------------------------------------------------------------------------
except KeyboardInterrupt:
	print("Understandable. Have a nice day")
	sys.exit()
except socket.gaierror:
	print("can't resolve hoastname")
	sys.exit()
except socket.error:
	print("unable to establish connection")
	sys.exit()
print("Thanks and goodbye")
