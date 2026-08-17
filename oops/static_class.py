
import datetime


class calander:
    def __init__(self)->None:
        self.event=[]

    def add_event(self,event:str)->None:
        self.event.append(event)

    def show_event(self)->None:
        print(f"Events: {self.event}")

    @staticmethod
    def is_weakend(date: datetime):
        if date.weekday()>4:
            print(f"{date} is a weekend")
        else:
            print(f"{date} is a weekday")




    

obj=calander()
obj.add_event("Birthday Party")
obj.add_event("Meeting with team")
obj.show_event()

calander.is_weakend(datetime.datetime.now())