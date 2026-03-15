from src.data_loader import load_data
from src.split import split_data
import pandas as pd


df=load_data()

train_set,test_set=split_data(df,0.2)

print("Train set:",len(train_set))
print("Test set:",len(test_set))





