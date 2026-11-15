import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('housing.csv').iloc[:,:-1].dropna()

print("read the dataset")
X=df.drop(columns='median_house_value')
y=df.median_house_value.copy()
print("split thedataset")
model=LinearRegression().fit(X,y)
print("Trained the model")
joblib.dump(model,'model.joblib')
print("saved the model")
