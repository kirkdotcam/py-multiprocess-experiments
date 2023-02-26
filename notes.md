# threading vs multiprocessing in python
- threading in python is slower due to the GIL
- threading is better for IO-bound (waiting for input, such as a database or network call) applications
- multiprocessing is better for CPU-bound applications (single-core is slow)
- thradeoff for multiprocessing is that you need MUCH more ram to hold multiple copies of your data
- consider turning off swapiness if disk IO becomes a limitation
