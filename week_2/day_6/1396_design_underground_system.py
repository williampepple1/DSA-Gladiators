# An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

# Implement the UndergroundSystem class:

# void checkIn(int id, string stationName, int t)
# A customer with a card ID equal to id, checks in at the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card ID equal to id, checks out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time it takes to travel from startStation to endStation.
# The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
# The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
# There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
# You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.


class UndergroundSystem:

    #Check In : 45, Leyton, 3.        Check Out: 45, Waterloo, 15 (12)
    #           32, Paradise, 8                  32, Cambridge, 22 (14)
    #           27, Leyton, 10                   27, Waterloo, 20 (10)  

    def __init__(self):
        self.checkInMap = {}
        self.journeyMap = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInMap[id]
        time = t - startTime
        journey = (startStation, stationName)

        if journey in self.journeyMap:
            self.journeyMap[journey][0] += time
            self.journeyMap[journey][1] += 1
        else:
            self.journeyMap[journey] = [time, 1] 
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = (startStation, endStation)
        totalTime, count = self.journeyMap[journey]
        return totalTime/count
  


        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)