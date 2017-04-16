# Why Rerun does not use Multiprocessing?
Some might argue that Multiprocessing is better due to process isolation. 
But fact is, the perfomance degradation is horrible. Refer to the file 
called 'pycallgraph-multiprocess.png'. This experiment with multiprocess 
was done in a 'feature' branch called better-threading. On the whole, the 
experiment was a failure and I found no ways to improve threading.  

# Speed
Rerun is still undergoing optimizations to reduce startup time and such. 
Do not judge Rerun by the speed of running it the first time on boot. The 
speed greatly improves after initial launch per boot. This cannot be changed 
by me as it is Python that causes this tiny lag.  
Also, for performance, I recommend Python 2 over 3. The lag is not nearly 
noticeable but Python 3 is slower than Python 2. For more info, refer benches
in the same folder.