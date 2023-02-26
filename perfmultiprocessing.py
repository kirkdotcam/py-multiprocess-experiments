from multiprocessing.pool import Pool
from time import perf_counter

test_loops = 10000

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

# multiprocess loops
multiprocess_start = perf_counter()
    
with Pool(8) as p:
  p.map(do_loop, range(test_loops))


multiprocess_end = perf_counter()
print(multiprocess_end-multiprocess_start)
