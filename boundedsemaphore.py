#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:49:22 2022

@author: alumno
"""
from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import BoundedSemaphore

N = 8
maxProcesos=1

def task(common, tid, critical, s):    
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')        
        a += 1
        print(f'{tid}−{i}: End of non−critical Section') 
        s.acquire()
        try:    
            print(f'{tid}−{i}: Critical section')        
            v = common.value + 1
            print(f'{tid}−{i}: Inside critical section')        
            common.value = v
            print(f'{tid}−{i}: End of critical section')        
            critical[tid] = 0   
        finally:
            s.release()
def main():    
    lp = []    
    common = Value('i', 0)    
    critical = Array('i', [0]*N)    
    s = BoundedSemaphore(maxProcesos)
    for tid in range(N):        
        lp.append(Process(target=task, args=(common, tid, critical, s)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:        
        p.start()
    for p in lp:        
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")


if __name__ == "__main__":    
    main()