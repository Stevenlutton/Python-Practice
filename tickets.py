TICKET_PRICE = 10

tickets_remaining = 100

print("There are {} tickets remaining".format(tickets_remaining))

name = input("Hi there, what is your name?   ")

tickets_wanted = input("Hi {}, how many tickets would you like to purchase?  ".format(name))
tickets_wanted = int(tickets_wanted)

amt_due = tickets_wanted * TICKET_PRICE

print("The total due is ${}".format(amt_due))

should_proceed = input("Would you like to purchase?   Y/N  ")

if should_proceed.lower() == "y":
    print("SOLD!")
    tickets_remaining -= tickets_wanted

else:
    print("Thank you anyways, {}".format(name))

