# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:57:39 2024

@author: nhopk
"""
import colored

print(f'{colored.Fore.cyan} Hello world')

import tqdm, time

counter = 0

for i in tqdm.tqdm(range(100)):
    counter += i
    time.sleep(0.1)
    
print(counter)
