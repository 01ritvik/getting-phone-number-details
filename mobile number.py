import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobile_number = input("Enter mobile number with country code: ")
mobile_number = phonenumbers.parse(mobile_number)

print(timezone.time_zones_for_number(mobile_number))

print(carrier.name_for_number(mobile_number, "en"))

print(geocoder.description_for_number(mobile_number, "en"))

print("valid Mobile number: ", phonenumbers.is_valid_number(mobile_number))

print("checking possibility of number: ", phonenumbers.is_possible_number(mobile_number))
