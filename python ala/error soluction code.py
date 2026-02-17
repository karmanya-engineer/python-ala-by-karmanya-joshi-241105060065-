print("Event Registration")
events = ["Seminar","Workshop","Hackathon"]
participants = []
name = input("Enter name: ")
event = input("Enter event: ")
if event in events:
    participants.append(name)
else:
    print("Event not available")
print("Name:", name)
print("Event:", event)
for i in range(3):
    print("Registered")
print("End")
