from Student import Student

continued = ""
student_list = []
student_info = 0

while(student_info != "1") :
    student_info = input("학생정보입력(그만두기:1) >")
    if(student_info == "1") : break
    student_list.append(Student(student_info[0],student_info[1],student_info[2],student_info[3]))

print("이름 총점 평균 석차")
for std in student_list:
    print (std.name, std.get_total_score(), std.get_average(),end=" ")