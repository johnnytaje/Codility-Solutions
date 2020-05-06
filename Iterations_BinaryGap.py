# -*- coding: utf-8 -*-


def main():

    A = 1041
    
    S = solution(A)
    D = dec2bin(A)
    print(D)
    print(S)       

#%% Solution function 
def solution(N):
    L = dec2bin(N)
    count = 0;
    maxCount = 0;
    for n in range(len(L)):
        if L[n] == 0:
            count = count+1;
        else:
            if count > maxCount:
                maxCount = count
            count = 0;
    return maxCount

#%% Decimal to binary
def dec2bin(A):
    D = [];
    m = 2
    while A >= 1:
        D.append(A % m)
        A = A//2
    D.reverse()
    return D

#%% Call Main
if __name__ == '__main__':
    main()