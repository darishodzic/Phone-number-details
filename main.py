import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo = input("Enter Mobile Number with Country code: ")
mobileNo = phonenumbers.parse(mobileNo)

# get timezone a phone number
timeZone = timezone.time_zones_for_number(mobileNo)
print("timezone: ", timeZone)
# Getting carrier of a phone number
Carrier = carrier.name_for_number(mobileNo, 'en')
# Getting region information
Region = geocoder.description_for_number(mobileNo, 'en')
# Printing the carrier and region of a phone number
print("Carrier: ", Carrier)
print("Region: ", Region)
# Validating a phone number
valid = phonenumbers.is_valid_number(mobileNo)
# Checking possibility of a number
possible = phonenumbers.is_possible_number(mobileNo)
# Printing the output
print("Valid: ", valid)
print("Possible: ", possible)
