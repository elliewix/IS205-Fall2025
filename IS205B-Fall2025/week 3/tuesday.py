bill = 100

print(bill /2)

medical_bill = 1000 + 175 + 1200 + 34
my_share = medical_bill * .2 # I pay 20%
insurance_share = medical_bill * .8 # they pay 80%
print(my_share, insurance_share)

####

# let's look at these apartments

apt1_size = 1000 # sqft
apt1_b1 = 12 * 14
apt1_b2 = 11 * 14
print(apt1_b1, apt1_b2)

apt1_bedroom_size = apt1_b1 + apt1_b2
print(apt1_size - apt1_bedroom_size)

# now for apt 2

apt2_size = 1190
apt2_b1 = 15 * 14
apt2_b2 = 15 * 9
apt2_b3 = 12 * 9
apt2_b4 = 9 * 15

apt2_bedroom_size = apt2_b1 + apt2_b2 + apt2_b3 + apt2_b4

print(apt2_size - apt2_bedroom_size)

# updating variables
# updating the total bedroom size by 100sqft

apt2_bedroom_size = apt2_bedroom_size + 100

