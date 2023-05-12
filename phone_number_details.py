import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("enter your phonenumber with +___ ")
phone=phonenumbers.parse(number)    # it is converting phone number entered by user into phone number format

if phonenumbers.is_valid_number(phone)==True: #checks whether the given phone number is valid or not
     time=timezone.time_zones_for_number(phone)   # gives the timezone of our phone number
     car=carrier.name_for_number(phone,"en")    #provides the carrier of our phone number
     region=geocoder.description_for_number(phone,"en")   #gives the geographical location of our phone number
     print("Time Zone of your phone number is ",time )
     print("Carrier of your phone number is ",car)
     print("Your phone number is from ",region)
else:
     print("Your phone number isn't valid ")  

