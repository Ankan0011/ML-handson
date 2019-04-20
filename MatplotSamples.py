#This program matplotling based on correlation amoung columns


import pandas as pd
import matplotlib.pyplot as plt

housing = pd.read_csv("C:\\Users\\ankan.ghosh\\Desktop\\ML\\kaggle_data\\housing.csv" , header='infer')
#train_set , test_set = split_train_test_by_id(housing_with_id, 0.2, "index")


housing.plot(kind = "scatter", x = "longitude", y = "latitude", alpha = 0.4
             , s=housing["population"]/100, label="population",
             c = "median_house_value", cmap= plt.get_cmap("jet"), colorbar=True )
#plt.legend()

corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending = False))
