class MyCalendarTwo:

    def __init__(self):
        self.booked=[]
        self.overlap_booked=[]
        
    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlap_booked:
            if min(e,end)-max(s,start)>0:
                return False
        for s,e in self.booked:
            if min(e,end)-max(s,start)>0:
                self.overlap_booked.append((max(s,start),min(e,end)))
        self.booked.append((start,end))
        return True

        
        
             
    
        


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
times=[(10, 20), (50, 60), (10, 40), (5, 15),(5,10), (25, 55)]
for time in times:
    print(obj.book(time[0], time[1]))

print(obj.booked, obj.overlap_booked)
# [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]