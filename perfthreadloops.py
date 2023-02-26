from threading import Thread
from time import perf_counter

test_loops = 1000

def do_loop(n):
  for loop in range(n):
    vals = [n*n for n in range(10000)]    
    vals = [v/50 for v in vals]
    vals = [v**(1/3) for v in vals]
    return vals
# normal loop
norm_start = perf_counter()

for loops in range(test_loops):
  do_loop(loops)

norm_end = perf_counter()
print(norm_end-norm_start)

# threaded loops
thread_start = perf_counter()
threads = []
for loops in range(test_loops):
  Thread(target=do_loop, args=({loops})).start()

#[t.start() for t in threads]

thread_end = perf_counter()
print(thread_end-thread_start)
