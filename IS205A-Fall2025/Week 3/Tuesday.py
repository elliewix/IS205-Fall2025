# comparing apartments

# apartment 1

apt1_size = 1000
apt1_b1 = 12 * 14
apt1_b2 = 11 * 14

# print(apt1_b1, apt1_b2)
# apt size - (total bedroom size)
apt1_communal_space = apt1_size - (apt1_b1 + apt1_b2)
print(apt1_communal_space)

# apartment 2

apt2_size = 1190

apt2_b1 = 13 * 14
apt2_b2 = 15 * 9
apt2_b3 = 12 * 9
apt2_b4 = 9 * 15

apt2_bedroom_total = apt2_b1 + apt2_b2 + apt2_b3 + apt2_b4
apt2_communal_space = apt2_size - apt2_bedroom_total

print(apt2_communal_space)

# okay wait, what if the bedroom size changes

# I want add 100sqft to the total bedroom space
# updating variables
apt2_bedroom_total = apt2_bedroom_total + 100
print(apt2_size - apt2_bedroom_total)

# a different kind of calculation

# splitting an 80/20 bill

total_bill = 1250 + 300 + 175
my_share = total_bill * .2 # I pay 20%
insurance = total_bill * .8 # insurance pays 80%

print(my_share)

