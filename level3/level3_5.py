class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t1, t2):
        total_minutes = (t1.hours + t2.hours) * 60 + t1.minutes + t2.minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

time1 = Time(2, 50)
time2 = Time(1, 20)

result = Time(0, 0)
result.addTime(time1, time2)

print("Time 1:", end=" ")
time1.displayTime()
print("Time 2:", end=" ")
time2.displayTime()
print("Result:", end=" ")
result.displayTime()
result.displayMinutes()
