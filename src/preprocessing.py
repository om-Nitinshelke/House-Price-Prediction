import pandas as pd

def preprocess_the_data(train_set,test_set):

    train_set=train_set.drop(["Locality","Amenities"],axis=1)
    test_set=test_set.drop(["Locality","Amenities"],axis=1)

    x_train=train_set.drop("Price_in_Lakhs",axis=1)
    y_train=train_set["Price_in_Lakhs"]

    x_test= test_set.drop("Price_in_Lakhs", axis=1)
    y_test = test_set["Price_in_Lakhs"]

    x_train=pd.get_dummies(x_train,drop_first=True)
    x_test=pd.get_dummies(x_test,drop_first=True)

    x_train,x_test=x_train.align(x_test,join='left',axis=1,fill_value=0)

    return  x_train,x_test,y_train,y_test

