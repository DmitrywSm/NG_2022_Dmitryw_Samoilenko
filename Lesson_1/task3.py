currentTime = int(input("Input required number of seconds: "))

days = currentTime / 86400
hours = (currentTime / 3600 ) % 24
minutes = (currentTime / 60) % 60
seconds = currentTime % 60

print(f"days:  {int(days)} \nhours: {int(hours)} \nminutes: {int(minutes)} \nseconds: {int(seconds)}")
input("Press Enter to close program")
exit()