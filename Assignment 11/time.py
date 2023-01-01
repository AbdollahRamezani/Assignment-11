class Time:
    def __init__(self, h, m,s) :
        self.second=s
        self.minute=m
        self.hour=h
        self.fix()  # جهت فیکس کردن زمانهای اشتباه وارد شده
    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)    

    def sum(self, other):
        h=self.hour+other.hour    
        m=self.minute+other.minute    
        s=self.second+other.second 
        result=Time(h, m, s)
        return result
    
    def sub(self, other):
        h=self.hour-other.hour    
        m=self.minute-other.minute    
        s=self.second-other.second 
        result=Time(h, m, s)
        return result
    
    def gmt_to_tehran(self):
        t=Time(3, 30, 0)
        tehran_time=self.sum(t)
        return tehran_time
    
    def time_to_second(self):
        seconds=self.hour*3600 + self.minute * 60 + self.second
        return seconds
    
    @staticmethod   #توسط هیچ شیئی فراخوانی نشده و مال خود کلاس است 
    def seconds_to_time(seconds):  # نیاز به سلف ندارد چون مال شی خاصی نیست و مال کلاس است
       hour=seconds//3600
       seconds=seconds-(hour*3600)
       minute=seconds//60
       seconds=seconds-(minute*60)
       second=seconds
       time=Time(hour, minute, second)
       return time
    
    def fix(self):
        if self.second >= 60 :
            self.second -= 60
            self.hour += 1
        
        if self.minute >= 60 :
            self.minute -= 60    
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1        

  
t1=Time(3,65,14)
t1.show()        

t2=Time(4, 16, 25)
t2.show()

sum=t2.sum(t1)
sum.show()

sub=t2.sub(t1)
sub.show()

tehran_time=t1.gmt_to_tehran()
tehran_time.show()

seconds=tehran_time.time_to_second()
print("Seconds : ", seconds)

time=Time.seconds_to_time(4000)   #در اینجا استاتیک متد توسط خود کلاس فراخوانی می شود
time.show()