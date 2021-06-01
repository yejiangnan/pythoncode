from kNN.kdTree import kdtree
import kNN
import numpy as np

x1=[]
y1=[]
nums=[189, 198, 195, 199, 186, 187, 195, 201, 180, 204]
file="C:\\Users\\45530\\Desktop\\ml code\\MLiA_SourceCode\\machinelearninginaction\\Ch02\\digits\\trainingDigits\\"

for i in range(10):
    for j in range(nums[i]):
        num_arr=[]
        filename=file+"{}_{}.txt".format(i,j)
        with open(filename, 'r') as file_to_read:
            while True:
                line=file_to_read.readline()
                if not line:
                    break
                line=line[:len(line)-1]
                t=[float(i) for i in line]
                num_arr.append(t)
        num_arr=np.array(num_arr)
        num_arr=num_arr.flatten()
        x1.append(list(num_arr))
        y1.append(i)
         
x1=np.array(x1)
y1=np.array(y1)

x2=[]
y2=[]
nums=[87, 97, 92, 85, 114, 108, 87, 96, 91, 89]
file="C:\\Users\\45530\\Desktop\\ml code\\MLiA_SourceCode\\machinelearninginaction\\Ch02\\digits\\testDigits\\"

for i in range(10):
    for j in range(nums[i]):
        num_arr=[]
        filename=file+"{}_{}.txt".format(i,j)
        with open(filename, 'r') as file_to_read:
            while True:
                line=file_to_read.readline()
                if not line:
                    break
                line=line[:len(line)-1]
                t=[float(i) for i in line]
                num_arr.append(t)
        num_arr=np.array(num_arr)
        num_arr=num_arr.flatten()
        x2.append(list(num_arr))
        y2.append(i)      
x2=np.array(x2)
y2=np.array(y2)

sum=len(x2)
correct=0
wrong=0
k=5

T=kdtree(x1,y1)
T.kdtreeinit(T.root,0)

for i in range(len(x2)):
    res=T.knn_predict(k,x2[i])
    if res==y2[i]:
        correct+=1
    else:
        wrong+=1
    print("{}-th is predicted as {}, actually is {}".format(i,res,y2[i]))
print("correct rate is {:.2f}%".format(correct/sum*100))
    



