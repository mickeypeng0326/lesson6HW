#變數初始化
scores_list=[]
全班人數=int(input('全班人數:'))
sum=0
max=0
min=100
最高分的學生=[]
最低分的學生=[]

for X in range(全班人數):
    #輸入名字、成績
    student=[]
    name=input('name:')
    student.append(name)
    score=int(input('score:'))
    student.append(score)
    
    #加總、判斷最高最低分
    sum=sum+score
    if min>score:
        min=score
        最低分的學生=student
    if max<score:
        max=score
        最高分的學生=student
    
    #整理成績單
    scores_list.append(student)

#輸出資訊
print('最高分的學生:',最高分的學生)
print('最低分的學生:',最低分的學生)
print('總分:',sum)
print('平均:',sum/ 全班人數)




    
