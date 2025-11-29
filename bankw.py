import sys
if len(sys.argv)==4:
    script_name=sys.argv[0]
    withdraw=float(sys.argv[1])
    balance=float(sys.argv[2])
    pin=float(sys.argv[3])
else:
    script_name=sys.argv[0]
    withdraw=100
    balance=1000
    pin=1234

if withdraw<balance:
    print("transaction is approved")
else:
    print("transaction is declined")