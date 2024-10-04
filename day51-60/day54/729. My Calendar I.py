import bisect
class MyCalendar:

    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_left(self.events, (start, end))
        if i<len(self.events) and self.events[i][0]<end:
            return False
        if i>0 and self.events[i-1][1]>start:
            return False
        self.events.insert(i, (start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(8,9)
print(param_1)