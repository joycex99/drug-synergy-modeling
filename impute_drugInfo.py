import numpy as np
import scipy as sp
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import time
from sklearn.svm import SVR
start = time.time()



model = RandomForestRegressor(n_estimators=1000, max_features='sqrt') #select model for imputation
#model = SVR(kernel='rbf', degree = 3, C=10000, epsilon=0.48)
input_training_set_path = "Combined_data/drugInfo_toImpute.csv"  #<-training table input
ouput_training_set_path = "Combined_data/drugInfo_imputed.csv"  #<-imputed training table output
imp_val= -9999 #<-placeholder


df = pd.read_csv(input_training_set_path)
data = np.array(df.get_values())
headers = df.columns.get_values()


def impute():

	for col in range(0,len(headers)):
		print("Working on column: "+str(col))
		##for the current column, remove rows where the current (row,column) value is not equal to zero
		##this way we are only training on data with non-zero target values
		reduced_data = data[np.logical_not(data[:,col] == imp_val)] #remove row if row,col_num value is zero
		target_set = reduced_data[:,col]
		training_set = np.delete(reduced_data,col,1)
		model.fit(training_set,target_set)
		row_num=0
		for row in data:
			remaining = np.delete(row,col,0)
			if data[row_num,col] == imp_val:
				data[row_num,col] = model.predict(remaining)
			row_num+=1
		print("done.. "+str(time.time() - start))
	df = pd.DataFrame(data,columns=headers)
	df.to_csv(ouput_training_set_path,index=False)
	return df


def main():
	return impute()
if __name__ == "__main__":
	main()






