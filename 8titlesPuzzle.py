import copy


'''Functions body Start'''

def Print_board(boardArray):
    a=boardArray
    print(' %s | %s | %s \n--- --- ---\n %s | %s | %s  \n--- --- ---\n %s | %s | %s ' % (a[0][0],a[0][1],a[0][2],a[1][0],a[1][1],a[1][2],a[2][0],a[2][1],a[2][2],))

def get_Heuristic(array1,array2):
    count=0
    for i in range(0,len(array1)):
        for j in range(0,len(array1)):
            if array1[i][j]!=array2[i][j] and array1[i][j]!='0':
                count=count+1
    return count

def get_BlankPosition(array):
    abc =[0,0]
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if array[i][j]=='0':
                abc=[i,j]
    return abc

def Swap(array,pos1,pos2):
    arr=copy.deepcopy(array)
    temp=arr[pos1[0]][pos1[1]]
    arr[pos1[0]][pos1[1]]=arr[pos2[0]][pos2[1]]
    arr[pos2[0]][pos2[1]]=temp
    return arr

def get_toMove(ZeroPos):
    if ZeroPos==[0,0]:
        return [[0,1],[1,0]]
    elif ZeroPos==[0,1]:
        return [[0,0],[0,2],[1,1]]
    elif ZeroPos == [0,2]:
        return [[0,1],[1,2]]
    elif ZeroPos == [1,0]:
        return [[0,0],[2,0],[1,1]]
    elif ZeroPos == [1,1]:
        return [[1,0],[0,1],[1,2],[2,1]]
    elif ZeroPos == [1,2]:
        return [[0,2],[1,1],[2,2]]
    elif ZeroPos == [2,0]:
        return [[1,0],[2,1]]
    elif ZeroPos == [2,1]:
        return [[2,0],[1,1],[2,2]]
    elif ZeroPos == [2,2]:
        return [[2,1],[1,2]]




'''Function body end'''



'''Main Function Start'''
Start = [['1','2','3'],['0','4','6'],['7','5','8']]
Goal = [['1','2','3'],['4','5','6'],['7','8','0']]


Copy_Start = copy.deepcopy(Start)
Copy_Goal = copy.deepcopy(Goal)
Zero_Position=get_BlankPosition(Copy_Start)
To_Move=get_toMove(Zero_Position)
heuristicVal=[0,0,0,0]
for i in range(0,len(To_Move)):
    abc= Swap(Copy_Start,Zero_Position,To_Move[i][:])
    heuristicVal[i]=get_Heuristic(abc,Copy_Goal)
    Print_board(abc)
    print('\n')
print()





'''Main Function End'''
