from datetime import datetime
import time

class Call(object):
    def __init__(self, id, name, phone_number, time, reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time = datetime.strptime(time, '%x %X')
        self.reason = reason
        self.queue = []
    def display_info(self):
        print "Id: " + str(self.id)
        print "Name: " + self.name
        print "Phone Number: " + self.phone_number
        print "Time: " + str(self.time)
        print "Reason: " + self.reason
        return self

class CallCenter(object):
    def __init__(self, calls=None):
        if calls == None:
            self.calls = []
            self.queue_size = 0
        else:
            self.calls = calls
            self.queue_size = len(self.calls)
    def add(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size = len(self.calls)  
        return self
    """    
    Ninja Level: add a method to call center class that can find and remove 
    a call from the queue according to the phone number of the caller.
    """
    def remove_by_phone(self, phone_number):
        index = 0
        for i in range(0, self.queue_size):
            if self.calls[i].phone_number == phone_number:
                index = i
                break
        self.calls.pop(index)
        self.queue_size = len(self.calls)
        return self
    def info(self):
        print " "
        print "Queue: " + str(self.queue_size) + " calls"
        print "============================="
        for i in range(0,self.queue_size):
            print "Name: " + self.calls[i].name
            print "Phone Number: " + self.calls[i].phone_number
            print "Time: " + str(self.calls[i].time)
            print "Reason: " + self.calls[i].reason
            print "-----------------------------"
    """    
    Hacker Level: If everything is working properly, your queue should be sorted by time, 
    but what if your calls get out of order? Add a method to the call center class that 
    sorts the calls in the queue according to time of call in ascending order.
    """
    def sort_queue(self):
        for i in range(0,self.queue_size-1):
            for j in range(i + 1,0,-1):
                if self.calls[j - 1].time > self.calls[j].time:
                    temp = self.calls[j-1]
                    self.calls[j-1] = self.calls[j]
                    self.calls[j] = temp
        return self

"""Test calls, times are out of order"""
call1 = Call(1, "Jonathan Ayala Colon", "604-655-2507", "02/17/18 16:07:16", "Whatever)
call2 = Call(2,"Vania Ayala Colon", "778-707-0753", "02/17/18 16:02:45", "Diarrhea")
call3 = Call(3,"Yolanda Colón Gonzalez", "555-252-5315", "02/17/18 16:15:23", "Broken arm")
call4 = Call(4,"José Antonio Ayala Méndez", "555-252-5415", "02/17/18 16:09:02", "Surgery")
call5 = Call(5,"Elizabeth Wallace", "604-312-5853", "02/17/18 16:07:32", "Confused")
call6 = Call(6,"Michelle Godoy", "604-771-7261", "02/17/18 11:06:11", "Waking up")

"""Add calls"""
center = CallCenter()
center.add(call1)
center.add(call2)
center.add(call3)
center.add(call4)
center.add(call5)
center.add(call6)

"""Removes call from queue using phone number"""
center.remove_by_phone(call2.phone_number)
center.info()

"""Sort call queue by time ascending"""
center.sort_queue()
center.info()