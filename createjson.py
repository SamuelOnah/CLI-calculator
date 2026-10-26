import json
import os


FILE = "tickets.json"

def create_ticket():
    description = input("enter ticket description: ").strip

    if not description:
        print("Enter correct description")
        return 

    tickets = []

    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                tickets = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error: couldnot read tickets.json")
            return 

    ticket_id = max(
        [t["id"] for t in tickets],
        default=0
    ) + 1

    ticket = {
        "id": ticket_id,
        "description": description
    }
    tickets.appends(ticket)

    if os.path.exist(FILE):
        try:
            with open(FILE, "w") as file:
                json.dumb(tickets, file, indent=4)
                print(f"Ticket created successfully! {ticket_id}")        
        except OSError:
            print("Error: could not read ticket")

if __name__ == "__main__":
    create_ticket()