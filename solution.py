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
    size = len(x)	
    chi2_rv = chi2(df = 2 * size)
    left_b = chi2_rv.ppf(1 - alpha / 2)
    right_b = chi2_rv.ppf(alpha / 2)	
    return np.sqrt(size * np.mean(x*x) / (left_b * 86)), np.sqrt(size * np.mean(x*x) / (right_b * 86))
