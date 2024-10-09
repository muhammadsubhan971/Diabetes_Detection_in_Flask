import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
import joblib 

def predication(input):
    df=pd.read_csv(r'D:\machine learning contents\datasets\diabetes_prediction_dataset.csv')
    df.head()

    X=df.drop(df['diabetes']).to_numpy
    Y=df['diabetes'].to_numpy
    x_train,x_test,y_train,y_test=train_test_split(df.iloc[:,0:-1],df.iloc[:,-1],test_size=0.2,random_state=42)


    cu = ColumnTransformer(transformers=[
        ('tnf1', OrdinalEncoder(categories=[
            ['Female', 'Male', 'Other'],
            ['never', 'No Info', 'current', 'former', 'ever', 'not current']
        ]), ['gender', 'smoking_history'])
    ], remainder='passthrough')

    cu.fit(x_train)

    x_train1=cu.transform(x_train)
    x_test1=cu.transform(x_test)


    sr=StandardScaler()
    sr.fit(x_train1)

    x_train=sr.transform(x_train1)
    x_test=sr.transform(x_test1)

    # print(x_train)

    lr=LogisticRegression(max_iter=1000)

    lr.fit(x_train1,y_train)

    
    joblib.dump(lr,'model.joblib')
    
    lr=joblib.load('model.joblib')
    
    pred=lr.predict(input)
    
    return pred
    
    
input_data = [[1, 45, 0, 1, 0, 24.5, 5.8, 120]]
print(predication(input_data))