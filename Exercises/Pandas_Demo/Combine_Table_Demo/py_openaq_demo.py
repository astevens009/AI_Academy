# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 21:37:59 2020

@author: A. Stevens
@description: Testing py-openaq
"""
import pandas as pd
import openaq as oaq

api = oaq.OpenAQ()

aq_source = api.sources(df=True)
print(aq_source.head())




