import pandas as pd
import numpy as np

from scipy.stats import expon
from scipy.stats import chi2
from scipy.stats import norm

chat_id = 305011093 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s = np.sum(x)
    x_mean = s / n
    left = (-np.log(alpha/2 + 1/2) - x_mean)/(86**2)
    right = (-np.log(3/2 - alpha/2) - x_mean)/(86**2)
    return left, \
           right
