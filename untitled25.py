# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 22:11:33 2021

@author: ASUS
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/ASUS/Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist', 100 , False, path, 15)    
df.to_csv('Glassdoor_jobs.csv', index = False)
