import numpy as np

x2=np.array(
    [
        [12, 1, 3, 7],
        [4,0,2,3],
        [0,0,6,9]
    ]
)
x2_sub=x2[:2,:2].view()
#Thay đổi trên con/ gốc thì cả con và gốc đều thay đổi
x2_sub2=x2[:2,:2].copy()
#Thay đổi dữ liệu thì bản gốc và con không liên quan đến nhau

x2[0,0]=99

print(x2,x2_sub,x2_sub2,sep="\n")