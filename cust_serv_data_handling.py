'''
2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.

Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

'''
# moved all comments here for clearer visual

# create a sample to start with
# create functions for each action. Use pass for now.
# create a function for assigning a ticket
# displays all the tickets key created
# now we slice and just take the integers and increment that
# print the ticket with the next number available
# now that I can generate the next ticket number, I have to take inputs for name, issue and append to the dictionary

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def generate_ticket(service_tickets):
     
    new_ticket = [int(ticket[6:]) for ticket in service_tickets.keys()]  
    next_ticket = max(new_ticket) + 1
    return (f"Ticket{next_ticket:03d}")  


def open_ticket():
    new_ticket = generate_ticket(service_tickets)
    name = input("Please enter customer's name: ")
    issue = input("Please enter issue: ")
    status = "open"

    service_tickets[new_ticket] = {"Customer": name, "Issue" : issue, "Status" : status}
    print(f"New ticket created: {new_ticket}")
  

def update_ticket():
    ticket_id = input("Please enter the ticket ID you want to update: ")

    if ticket_id in service_tickets:
        current_status = service_tickets[ticket_id]["Status"]
        new_status = "closed" if current_status == "open" else "open"
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}")
    else:
        print("Ticket not found.")

def display_tickets(filter_by = None):  # or filter by status
    if filter_by:
        filtered_tickets = {ticket: details for ticket, details in service_tickets.items() if details["Status"] == filter_by}
        if filtered_tickets:
            for ticket, details in filtered_tickets.items():
                print(f"{ticket}: {details}")
        else:
            print(f"No tickets with status '{filter_by}'")
    else:
        for ticket, details in service_tickets.items():
            print(f"{ticket}: {details}")

# call functions
#def main():
    # Display sample data
print("Initial Service Tickets:")
display_tickets()
    
    # Add a new ticket
open_ticket()
    
    # Update an existing ticket
update_ticket()
    
    # Display all tickets after update
print("Updated Service Tickets:")
display_tickets()

    # Display only open tickets
print("Open Tickets:")
display_tickets(filter_by="open")
    
    # Display only closed tickets
print("Closed Tickets:")
display_tickets(filter_by="closed")


#main()