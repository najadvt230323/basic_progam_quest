# import threading

# def dispay():
#     for i in range(5):
#         print("hello")

# def dispay1():
#     for i in range(5):
#         print("najad")

# t1 = threading.Thread(target = dispay)
# t2 = threading.Thread(target = dispay1)

# t1.start()
# t2.start()

# ----------------------------------------------------------------------------

# import threading
# import time

# def dispay():
#     for i in range(5):
#         print("hello")
#         time.sleep(1)

# def dispay1():
#     for i in range(5):
#         print("najad")
#         time.sleep(1)
# def dispay2():
#     for i in range(5):
#         print("")
#         time.sleep(1)

# t1 = threading.Thread(target = dispay)
# t2 = threading.Thread(target = dispay1)
# t3 = threading.Thread(target = dispay2)

# t1.start()
# t2.start()
# t3.start()

# ---------------------------------------------------------------------------

# import threading
# import time

# def dispay():
#     for i in range(5):
#         print("hello")
#         time.sleep(1)

# def dispay1():
#     for i in range(5):
#         print("najad")
#         time.sleep(1)

# start_time = time.time()

# t1 = threading.Thread(target = dispay)
# t2 = threading.Thread(target = dispay1)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end_time = time.time()

# print("Execution Time : ",end_time - start_time ," Seconds")

# -------------------------------------------------------------------------------

# import threading

# counter = 0

# def dispay():
#     global counter
#     for i in range(1000000):
#         counter +=1
    
# t1 = threading.Thread(target = dispay)
# t2 = threading.Thread(target = dispay)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter)

# -----------------------------------------------------------------------------------

import threading

counter = 0
lock =threading.Lock()

def dispay():
    global counter

    for i in range(1000000):
        lock.acquire()

        counter +=1

        lock.release()
    
t1 = threading.Thread(target = dispay)
t2 = threading.Thread(target = dispay)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter) 


# --------------------------------------------------------------------------
