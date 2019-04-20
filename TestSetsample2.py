#This program have 2 different type of test data split
#Firstly, based on random hash calculated split using train_test_split function with 20%
# Second, based non statum spliting on category using StratifiedShuffleSplit

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.preprocessing import Imputer, StandardScaler, FunctionTransformer, OneHotEncoder
from sklearn.pipeline import Pipeline
#from sklearn.pipeline import FeatureUnion ~~~~~~~~~# This method is depreciated in scikit 0.20 package, instead use the ColumnTransformer
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score



def add_extra_features(X, add_bedrooms_per_room=True):
    rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
    population_per_household = X[:, population_ix] / X[:, household_ix]
    if add_bedrooms_per_room:
        bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
        return np.c_[X, rooms_per_household, population_per_household,
                     bedrooms_per_room]
    else:
        return np.c_[X, rooms_per_household, population_per_household]

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())



housing_val = pd.read_csv("C:\\Users\\ankan.ghosh\\Desktop\\ML\\kaggle_data\\housing.csv" , header='infer')
#train_set , test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

train_set, test_set = train_test_split(housing_val, test_size = 0.2, random_state=42)
print(len(train_set), "train +", len(test_set), "test")

housing_val["income_cat"] = np.ceil(housing_val["median_income"] / 1.5)

#print(housing_val)
housing_val["income_cat"].where(housing_val["income_cat"] < 5, 5.0, inplace = True)

#Stratified split for the proporational test data split on the basis of "income_cat" category
df_split = StratifiedShuffleSplit(n_splits= 1 , test_size= 0.2, random_state= 42)
for train_index , test_index in df_split.split(housing_val, housing_val["income_cat"]):
    strat_train_set = housing_val.loc[train_index]
    strat_test_set = housing_val.loc[test_index]

for settle in (strat_train_set, strat_test_set):
    settle.drop(["income_cat"], axis=1, inplace = True)

#Preparing dataframe for machine leanrning algorithm training 
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

#print(housing_val["income_cat"].value_counts())
rooms_ix, bedrooms_ix, population_ix, household_ix = [
    list(housing.columns).index(col)
    for col in ("total_rooms", "total_bedrooms", "population", "households")]


#housing["rooms_per_household"] = housing["total_rooms"]/ housing["households"]
#housing["bedrooms_per_room"] = housing["total_bedrooms"]/ housing["total_rooms"]
#housing["population_per_household"] = housing["population"] / housing["households"]

#checking the correlation of column "median_house_value" with reset of the columns to figure out which columns are directly proportional 
#corr_matrix = housing.corr()
#corr_matrix["median_house_value"].sort_values(ascending =False)


housing_num = housing.drop("ocean_proximity", axis = 1)
housing_cat = housing[['ocean_proximity']]



num_attrib = list(housing_num)
cat_attrib = ["ocean_proximity"]

    
num_pipeline = Pipeline([
    ('imputer', Imputer(strategy="median")),
    ('attrib_adder', FunctionTransformer(add_extra_features, validate=False)),
    ('std_scaler', StandardScaler()),
    ])

cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)


full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attrib),
        ("cat", OneHotEncoder(), cat_attrib),
    ])

housing_prepared = full_pipeline.fit_transform(housing)

"""Training Decision Tree Regressor Model to Test on training data"""
tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(housing_prepared, housing_labels)

"""let's try the full preprocessing pipeline on a few training instances"""
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)

print("Predictions:", tree_reg.predict(some_data_prepared))
print("Labels:", list(some_labels))


"""To check the Mean Square Error to measure its accuracy"""
"""
housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
print(tree_rmse)
"""
""" Training the model with RandomForestRegressor"""
forest_reg = RandomForestRegressor(n_estimators=30, random_state=42)
forest_reg.fit(housing_prepared, housing_labels)

"""Cross Validation feature to evaluate the training model """
"""scores = cross_val_score(forest_reg, housing_prepared, housing_labels,
                         scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-scores)

display_scores(tree_rmse_scores)
"""


test_data_temp = strat_test_set.drop("median_house_value", axis=1)
test_data = full_pipeline.fit_transform(test_data_temp)
strat_test_set["predicted_values"] = forest_reg.predict(test_data)

strat_test_set.to_csv("C:\\Users\\ankan.ghosh\\Desktop\\ML\\kaggle_data\\predictionII.csv" ,index=False,  sep=',')

