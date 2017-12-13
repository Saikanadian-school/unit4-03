
#gets the address
def getaddress():
    global address
    address = raw_input("enter your address: ")
    global city 
    city = raw_input("enter your city: ")
    global province 
    province = raw_input("enter your province: ")
    global postalcode 
    postalcode = raw_input("enter your postal code: ")
    global aptnum 
    aptnum = raw_input("enter your apartment number ")
#prints address
def printaddress(address, city, province, postalcode, aptnum = ''):
    if aptnum == '':
        print address 
    else:
        print aptnum + ' - ' + address 
    print city + ', ' + province
    print postalcode
	
#the code
getaddress()
printaddress(address, city, province, postalcode, aptnum)

