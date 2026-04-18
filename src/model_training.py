from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def train_models(X_train,y_train,X_test,y_test):

    results={}

    lr_model=LinearRegression()
    lr_model.fit(X_train,y_train)

    train_of_lr=lr_model.predict(X_train)
    test_of_lr=lr_model.predict(X_test)

    results["Linear Regression"]={"Train MSE":mean_squared_error(y_train,train_of_lr),
                                  "Test MSE":mean_squared_error(y_test,test_of_lr)}


    dt_model=DecisionTreeRegressor()
    dt_model.fit(X_train,y_train)
    train_of_dt = dt_model.predict(X_train)
    test_of_dt = dt_model.predict(X_test)

    results["Decision Tree"] = {"Train MSE": mean_squared_error(y_train, train_of_dt),
                                    "Test MSE": mean_squared_error(y_test,test_of_dt)}

    rt_model=RandomForestRegressor(n_estimators=20,n_jobs=-1,random_state=42)
    rt_model.fit(X_train, y_train)
    train_of_rt = rt_model.predict(X_train)
    test_of_rt = rt_model.predict(X_test)

    results["Random Forest"] = {"Train MSE": mean_squared_error(y_train, train_of_rt),
                                    "Test MSE": mean_squared_error(y_test,test_of_rt)}

    return results