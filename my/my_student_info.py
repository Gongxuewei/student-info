docs = []
def input_student():
    L = []
    d = set()
    while True :
        i_name  = input("请输入学生姓名,学生名为空退出:")
        if i_name == '':
            break
        else:
            i_age   = input("请输入学生年龄:")
            i_score = input("请输入学生成绩:")
            d = {'name':i_name,'age':i_age,'score':i_score}
            L.append(d)
    #print(L)
    global docs
    docs += L
    return L

def output_student(L):
	#边线+-----+-------+-------+
    def fmt_title_func(column_len):
        fmt_title = "+%%%ds+%%%ds+%%%ds+" % (column_len,column_len,column_len)
        s = '-'
        for  i in range(column_len -1 ):
            s += '-'
        return(fmt_title %(s,s,s))
    
    #|内容|内容|内容|
    def fmt_content_func(column_len,L):
        fmt_content = "|%%%ds|%%%ds|%%%ds|" % (column_len,column_len,column_len)
        return(fmt_content % (L[0],L[1],L[2]))
    
    #字典转list
    def dict_to_list(s):
        L = []
        for i in s :
            L.append(s[i])
        return L
    
    #计算输入最大长度
    L2 = []
    for i in L :
        each_line = dict_to_list(i)
        L2 += each_line
    lm = 7
    for j in L2:
        if  len(j) > lm :
            lm = len(j)
    max_length = lm
    #打印标题栏
    L_title = ['name','age','score']
    print(fmt_title_func(max_length))
    print(fmt_content_func(max_length,L_title))
    print(fmt_title_func(max_length))
    #循环调用dict_to_list(s)，调用一次打印一次输入
    for i in L :
        new_list = dict_to_list(i)
        print(fmt_content_func(max_length,new_list))
        print(fmt_title_func(max_length))

#docs = input_student()
#output_student(docs)
def modify_student(M_L):
    #stu_name = input("请输入要修改的学生名字:")
    #for i in M_L:
    #	if i['name'] == stu_name:
    pass


def del_student(D_L):
    stu_name = input("请输入要删除的学生名字:")
    for i in D_L:
        #print(i)
        if i['name'] == stu_name:
            #print(D_L.index(i))
            #del D_L[D_L.index(i)]
            global docs
            del docs[D_L.index(i)] 



def user_interface():
    print('+-------------------+')
    print('| 1)添加学生信息    |')
    print('| 2)显示学生信息    |')
    print('| 3)修改学生信息    |')
    print('| 4)删除学生信息    |')
    print('| q)退出信心系统    |')
    print('+-------------------+')
    while True:
        n = input("请输入选项:")
        if n == '1':
            input_student()
            #print(docs)
        elif n == '2':
            if docs == []:
                print("没有学生信息录入")
            else:
                output_student(docs)
        elif n == '3':
            modify_student()
        elif n  == '4':
            del_student(docs)
        elif n == 'q':
            print("退出信心系统！")
            break
        else:
            print("请输入正确选项！")
user_interface()