import numpy as np
#1
def longest_substring(string1,string2):
    mat=np.zeros(shape=(len(string1),len(string2)))
    for x in range(len(string1)):
        for y in range(len(string2)):
            if x==0 or y==0:
                if string1[x]==string2[y]:
                    mat[x,y]=1
            else:
                if string1[x]==string2[y]:
                    mat[x,y]=mat[x-1,y-1]+1
    agmx=np.argmax(mat)
    iofagmx=np.unravel_index(agmx,mat.shape)
    numbofstr=int(np.max(mat))
    endstring=string1[iofagmx[0]-numbofstr+1:iofagmx[0]+1]
    return endstring
    
if __name__ == '__main__':
    assert longest_substring("jsanad","anasc") == "ana"
    assert longest_substring("ilovebioinformatics","icantwaitformax") == "forma"
    assert longest_substring("ironmansaregreat","triathlonforever") == "on"
    assert longest_substring("ihatewalking","nobikenolife") == "i"
    assert longest_substring("gofaster","govegan") == "go"    
   
