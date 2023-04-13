import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


chat_id = 653318045 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=0.09
    
    p_value=proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')[1]
    print(p_value)
    if (p_value < alpha) and (x_success/x_cnt <= y_success/y_cnt):
      return True
    else: 
      return False
