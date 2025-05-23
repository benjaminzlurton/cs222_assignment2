import math

print("How many people will be attending the cookout?: ")
num_attendants = int(input())

print("How many hotdogs will each person be given?: ")
hotdogs_per_person = int(input())

hotdogs_per_package = 10
buns_per_package = 8

total_hotdogs = num_attendants * hotdogs_per_person
hotdog_packages_needed = math.ceil(total_hotdogs / hotdogs_per_package)
bun_packages_needed = math.ceil(total_hotdogs / buns_per_package)

print(f"You need {hotdog_packages_needed} packages of hotdogs!")
print(f"There will be {(hotdog_packages_needed*hotdogs_per_package) - total_hotdogs} hotdogs left over.")

print(f"You need {bun_packages_needed} packages of buns!")
print(f"There will be {(bun_packages_needed*buns_per_package) - total_hotdogs} buns left over.")

