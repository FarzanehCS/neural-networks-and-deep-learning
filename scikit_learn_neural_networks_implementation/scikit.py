from sklearn.neural_network import MLPClassifier
import data_skikit
import numpy as np

file_hourly = "/Users/amir/Desktop/fxtime/cur_hours.csv"
file_daily = "/Users/amir/Desktop/fxtime/cur_daily.csv"
data_file = "/Users/amir/Desktop/fxtime/input.csv"
out_file = "/Users/amir/Desktop/fxtime/out.csv"

lst_of_new_data = [1.31784, 1.31592, 1.31459, 1.31497, 1.31187, 1.31298, 1.31257, 1.31099, 1.31064,
                   1.31069, 1.31049, 1.31069, 1.31083, 1.31026, 1.31037, 1.31107, 1.31077, 1.31070, 1.31088, 1.30947,
                   1.31136, 1.30919, 1.30849, 1.30970]
num_features = 24
num_samples = 50

new_lst = np.array(lst_of_new_data).reshape(1, num_features)

lst_input = data_skikit.provide_data(file_hourly, data_file)

matrix_input = np.array(lst_input).reshape(num_samples, num_features)

lst_labels = data_skikit.provide_output(file_daily, out_file)

matrix_output = np.array(lst_labels).reshape(num_samples, )

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10, 10, 10), random_state=1)

clf.fit(matrix_input, matrix_output)

result = clf.predict(new_lst)



# test if next day candle will be a buy candle or a sell one
if result == [1]:
    print("sell")
else:
    print("buy")
