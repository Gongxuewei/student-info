def input_student():
  L = []
  while True:
    n = input("请输入学生姓名: ")
    if not n:
      break
    a = int(input("请输入学生年龄: "))
    s = int(input("请输入学生成绩: "))
    d = {"name": n,"age": a , "score" : s}
    L.append(d)
  return L


def output_student(L):
  line = "+------------+------------+------------+"
  (title) = "| name       |    age     | score      |"
  print(line)
  print(title)
  print(line)
  for d  in L :
    s = '|%s|%s|%s|' %(d['name'].center(12),
                       str(d['age']).center(12),
                       str(d['score']).center(12)
                       )
    print(s)
    #print(line)
  print(line)
docs = input_student()
print(docs)
output_student(docs)


def show_menu():
    print('+---------------------------+')
    print('| 1)添加学生信息            |')
    print('| 2)显示学生信息            |')
    print('| 3)修改学生信息            |')
    print('| 4)删除学生信息            |')
    print('| 5)按成绩高低输出学生信息学|')
    print('| 5)按成绩高低输出学生信息学|')
    print('| 5)按成绩高低输出学生信息学|')
    print('| 5)按成绩高低输出学生信息学|')
    print('| q)退出信心系统            |')
    print('+---------------------------+')

def man ():
  while  True:
    show_menu()
    s = input("请输入: " )
    if s =  '1':
      lst = input_student()
      docs.extend(lst)
      
      #添加学生信息
    if s = 'q' :
      break
    if s = '5':
      def k(d):
        return d['score']
      lst = sorted(docs, key = k ,reverse = True)
      output_student(lst)
      