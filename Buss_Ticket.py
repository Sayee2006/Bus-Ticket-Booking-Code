print("=== Bus Ticket Booking App.! ===")

routes = {
    1: ("Mumbai -> Pune",300),
    2: ("Delhi -> Agra",450),
    3: ("Banglore -> Mysore",350)
}

print("\nAvailable Routes:")
for key , value in routes.items():
    print(f"{key}. {value[0]} - ₹{value[1]} ")    

choice = int(input("\nEnter The Route Number:"))

if choice in routes:
    route_name , price = routes[choice]
    print(f"\n You Selected route : {route_name}")

    tickets =   int(input("How Many tickets do you want to buy ? "))

    total = price * tickets 

    print(f"\n Total amount: ₹{total}")

    with open("ticket.txt","w") as file:
        file.write("=== Bus Tickets Details === \n")
        file.write(f"Route{route_name} \n")
        file.write(f"Price Per Ticket: {price} \n")
        file.write(f"Number of Tickets : {tickets} \n")
        file.write(f"Total Amount: {total} \n")
        file.write(f"Ticket Booked Successfully.! \n")


    print("\n Ticket Booked Successfully.!")
    print("\nYour Ticket Details are saved in 'ticket.txt'\n")

else:
    print("Invalid route Number.!")