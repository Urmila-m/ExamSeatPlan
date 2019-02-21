import pandas as pd
import numpy as np
import math

def partition(size,num_partion):
    step = size/num_partion
    result = list()
    ans = 0
    for i in range(num_partion):
        ans += step
        result.append(int(ans-1))

    return result

def equalise(dataframes, totalseat):
    # Merges dataframes so that all student occupy all the seats
    num_exam = len(dataframes)
    sizes = list(map(len, dataframes))
    total_size = sum(sizes)
    assert(total_size <= totalseat)

    max_size = max(sizes)

    if totalseat/num_exam >= max_size:
        group_size = max_size
    
    else:
        group_size = math.ceil(totalseat/num_exam) #up ceil

    total_dataframes = pd.DataFrame(np.array(['empty']* (group_size *num_exam)), columns = ['Key']) # initializing

    # make it more readable
    a = 0
    for i, df in enumerate(dataframes):
        b = a + sizes[i]
        total_dataframes.Key[a:b] = df.Key[0:sizes[i]]
        a = b
    
    ans_dataframe = list()
    a = 0
    for i in range(num_exam):
        b = (i+1) * group_size
        ans_dataframe.append(total_dataframes[a:b])
        a = b
    
    return ans_dataframe

def arrange_seat(equalised_dataframes):
    group_num = len(equalised_dataframes)
    group_size = len(equalised_dataframes[0])
    
    total_list = list()
    for df in equalised_dataframes:
        total_list.append(df.values)
    
    total_list = np.array(total_list)
    dataframe = pd.DataFrame(total_list.T.reshape(group_size, group_num))
    dataframe = dataframe.values.reshape(-1,1)
    dataframe = pd.DataFrame(dataframe,columns = ['Key'])
    dataframe['Key'] = dataframe['Key'].astype(str)
    return dataframe

def plan_examhall(dataframe, row, column):    
    dataframe['Row'] = dataframe.index/(len(dataframe)/(row)) + 1
    dataframe['Row'] = dataframe['Row'].apply(lambda x: int(x))
     
    dataframe['Column'] = dataframe.index % column + 1
    dataframe = dataframe.set_index(['Column','Row'])
    return pd.pivot_table(dataframe, values='Key', index=['Row'],
                    columns=['Column'], aggfunc=lambda x: ' '.join(x))
    

if __name__ == '__main__':
    filenames = ['bctA.xlsx', 'bctB.xlsx']
    dataframes = list()
    for fname in filenames:
        df = pd.read_excel(fname)[['Mobile Phone']]
        df.columns = ['Key']
        dataframes.append(df)
    

    dataframes = equalise(dataframes, 52)
    ans_dataframes = arrange_seat(dataframes)
    print(ans_dataframes)
    print(plan_examhall(ans_dataframes, 13, 4).reset_index().drop('Column',1))

