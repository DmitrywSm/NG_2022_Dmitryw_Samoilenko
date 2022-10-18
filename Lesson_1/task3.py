import datetime

currentTime = float(input("Enter required number of seconds: "))

currentUnixTime = datetime.datetime.fromtimestamp(currentTime, tz=datetime.timezone.utc)
currentTimeFormatDay = currentUnixTime.strftime("day: %d\nhour: %H\nminute: %M\nsecond: %S")
print(currentTimeFormatDay)
input("Press Enter to close the program")
exit()
