
import numpy as np
import matplotlib.pyplot as plt

#1
def reverse_array(input_array):
    rev = input_array[::-1]
    return rev

#2
def sort_array(input_array):
    sorted_array=np.sort(input_array)
    return sorted_array,input_array

#3
def plot_matrix(seq_0, seq_1):
    mat=np.zeros(shape=(len(seq_0),len(seq_1)))
    for x in range(0,len(seq_0)):
        for y in range(0,len(seq_1)):
            if seq_0[x]==seq_1[y]:
                mat[x,y]=1    
    plt.matshow(mat)
    plt.show()

if __name__ == '__main__':
#    print(reverse_array(([1,2,3,4,5,6,7,8])))
#    print(sort_array((["A","V","G"])))
    print(plot_matrix("HELLOMUM","HELLOMUMFAFNVM"))

