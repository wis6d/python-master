#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:45:41 2020

@author: hideyuki.suzuki
"""

import numpy as np

arr = np.random.randint(0, 100, 100)

print(arr)
print('min:' + str(np.min(arr)))
print('max:' + str(np.max(arr)))
print('ave:' + str(np.mean(arr)))
print('med:' + str(np.median(arr)))
print('var:' + str(np.var(arr)))
print('std:' + str(np.std(arr)))