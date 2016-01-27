import sched, time



def print_time():
    print("From print_time", time.time())

def print_some_times():
    print(time.time())
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    s.enter(11, 1, print_time, ())
    s.run()
    print(time.time())
    
def sel_time():
    return time.time()+1

if __name__ == "__main__":

    s = sched.scheduler(sel_time, time.sleep)
    print_some_times()
