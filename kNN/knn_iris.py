from kNN.kdTree import kdtree
import pandas as pd
import numpy as np
import kNN


train_data = pd.read_excel(
    "C:\\Users\\45530\\Desktop\\iris data\\iris_train.xlsx")
train_data = np.array(train_data)
x1 = train_data[:, :4]
y1 = train_data[:, 4:5].flatten()
T = kdtree(x1, y1)
T.kdtreeinit(T.root, 0)
    
test_data = pd.read_excel("C:\\Users\\45530\\Desktop\\iris data\\test.xlsx")
test_data = np.array(test_data)
x2 = test_data[:, :4]
y2 = test_data[:, 4:5].flatten()

sum = len(x2)
correct = 0
wrong = 0
k = 7

for i in range(len(x2)):
    res = T.knn_predict(k, x2[i])
    if res == y2[i]:
        correct += 1
    else:
        wrong += 1
    print("{}-th is predicted as {}, actually is {}.".format(i,res,y2[i]))
print("correct rate is {:.2f}%".format(correct/sum*100))
