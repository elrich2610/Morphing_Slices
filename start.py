import os

topology=input("Insert the selected topology: ")
if topology in ["star","star2","tree","linear","ring"]:
    os.system("gnome-terminal -e 'bash -c \"./start.sh " + topology + "; exec bash\"'")
    os.system("gnome-terminal -e 'bash -c \"sudo python3 baseTopology.py; exec bash\"'")
