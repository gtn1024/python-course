"""
编写input_stu()函数完成学生数据记录的输入，
要求记录条数不小于5，
每个学生的信息包括学号，姓名和三门课程的成绩，
完善函数output_stu()实现输出每位学生的学号、姓名、和三门课程分数及总分。
要求使用list来模拟学生记录结构。
"""
N = 5
student = []
for i in range(N):
  student.append(['', '', [0, 0, 0]])


def input_stu(stu):
  for i in range(N):
    print(f"正在录入第{i+1}位同学信息")
    id = input("请输入学号：")
    stu[i][0] = id
    name = input("请输入姓名：")
    stu[i][1] = name
    for j in range(0, 3):
      stu[i][2][j] = int(input(f"请输入{j+1}的成绩："))


def output_stu(stu):
  for i in range(N):
    print(
        f"学号：{stu[i][0]}，姓名：{stu[i][1]}，成绩：{stu[i][2][0]}, {stu[i][2][0]}, {stu[i][2][0]}"
    )


if __name__ == '__main__':
  input_stu(student)
  print(student)
  output_stu(student)
