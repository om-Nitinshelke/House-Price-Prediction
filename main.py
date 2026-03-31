from src.data_loader import load_data
from src.split import split_data
from src.preprocessing import preprocess_the_data


df=load_data()

train_set,test_set=split_data(df,0.2)

X_train,X_test,Y_train,Y_test=preprocess_the_data(train_set,test_set)







