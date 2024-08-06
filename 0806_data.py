import pandas as pd
data={
    '학번': (2000,2010),
    '성적':[85,95,75,70,100,100,85,85,80,95]
}
print('일반')
print(pd.DataFrame(data))
print('------------------------------------')
print('프레임 컬럼 순서 변경')
print(pd.DataFrame(data,columns=['성적','학번']))