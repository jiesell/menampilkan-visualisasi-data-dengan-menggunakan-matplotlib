# -*- coding: utf-8 -*-
"""plot histogram

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zhYFAXeVisWSuXvhqkrRFFC1Q0rvuEXp
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.random.randn(1000)
plt.hist(X, bins = 20)
plt.show()