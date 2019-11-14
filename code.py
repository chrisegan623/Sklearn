from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import pandas as pd

if __name__ == '__main__':
    boston = load_boston()
    data = pd.DataFrame(boston.data)            #convert to pandas dataframe
    data.columns = boston.feature_names         #set column names to feature names
    data['Price'] = boston.target               #add price column


    X = data.drop(['Price'], axis = 1)          #set X and Y data for linear regression
    Y = data['Price']

    model = LinearRegression().fit(X,Y)
    influence = pd.DataFrame(model.coef_)
    influence.columns = ['Coef']
    influence['Feature'] = boston.feature_names
    #This dataframe shows each factors influence


    find_max = pd.DataFrame(abs(model.coef_))
    # create dataframe with all positive values to find the maximum

    find_max.columns = ['Coef']
    find_max['Feature'] = boston.feature_names

    find_max['Influence'] = 'Positive'

    for row in influence['Coef']:
        if row < 0:
            find_max['Influence'] = 'Negative'

    MaxInfluence = (find_max[find_max.Coef == find_max.Coef.max()])

    with open('Boston.txt', 'w') as b:
            b.write(str(MaxInfluence))
