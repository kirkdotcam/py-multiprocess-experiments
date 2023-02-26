from threading import Thread
from time import sleep

def do_loop(n):
  for loop in range(n):
    sleep(2)
    print(f"item {loop} in this thread")

t = Thread(target=do_loop, args=({6}))
p = Thread(target=do_loop, args=({2}))
t.start()
p.start()
