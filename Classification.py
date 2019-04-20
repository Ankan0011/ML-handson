#This program is implementation of classification example

import pandas as pd
from Code.MatplotSamples import corr_matrix





tract_data = pd.read_csv("C:\\Users\\ankan.ghosh\\Desktop\\ML\\kaggle_data\\US_tract2014.csv", encoding='latin-1')
#train_set , test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

corr_matrix1 = tract_data.corr()
print(corr_matrix1["adapt_index"].sort_values(ascending=False))