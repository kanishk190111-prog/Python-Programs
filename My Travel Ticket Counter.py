# 1. TEXT MANIPULATION
name = "kanishk Agarwal"
destination = "paris"

print("--- Travel Ticket Counter ---")
print("Passenger Name:", name.title())
print("Destination:", destination.upper())
print()


# 2. CALCULATING TICKET COST
tickets = 3
price = 150
total = tickets * price

print("--- Booking Details ---")
print("Number of Tickets:", tickets)
print("Price per Ticket:", price)
print("Total Cost:", total)
print()


# 3. CHECKING BUDGET
budget = 400

print("--- Budget Check ---")
print("Your Budget:", budget)
print("Is it within budget?", total <= budget)
print()


# 4. SWAPPING PRICES
ticket1 = 100
ticket2 = 250

print("--- Before Swapping ---")
print("Ticket 1 Price:", ticket1)
print("Ticket 2 Price:", ticket2)

ticket1, ticket2 = ticket2, ticket1

print("--- After Swapping ---")
print("Ticket 1 Price:", ticket1)
print("Ticket 2 Price:", ticket2)