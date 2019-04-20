import pandas as pd
import matplotlib.pyplot as plt


housing_val = pd.read_csv("C:\\Users\\ankan.ghosh\\Desktop\\ML\\kaggle_data\\housing.csv" , header='infer')
print(housing_val.head(10));
#print(housing_val.info())
print(housing_val.describe())
#print(housing_val["ocean_proximity"].value_counts())

housing_val.hist(bins = 50, figsize =(20,15))
plt.show()