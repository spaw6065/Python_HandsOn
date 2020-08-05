#1) WAP to create a Data Structure of students
# print the sum of scores in five subjects and get student percentage.

##get student marks as data structure
def get_student_marks(num_students):
    student_rollNo = 100
    last_student_rollNo = student_rollNo + num_students

    student_marks_list = list()
    student_dict = dict()
    marks_cntr = 0

    while student_rollNo < last_student_rollNo:
        cntr = 0
        ind_stud_marks = list()

        print("-----------------------------------------------")
        print(f"Enter the marks for student having rollno : {student_rollNo}")
        while cntr < 5:
            marks = float(input(f"   Enter the marks in subject {cntr} :  "))
            ind_stud_marks.append(marks)
            cntr += 1

        student_rollNo += 1
        student_marks_list.append(ind_stud_marks)
        student_dict[student_rollNo]=student_marks_list[marks_cntr]
        marks_cntr += 1


    #print(student_marks_list)
    #print(student_dict)
    return student_dict

## get student sum of marks and percentage
def get_student_progress_report(stud_detailed_report):
    cntr = 0
    student_report_card = list()
    for student_rollNo in stud_detailed_report:
        #print(student_rollNo)
        marks_Total = 0
        #print(student_detailed_report[student_rollNo])
        for marks in student_detailed_report[student_rollNo]:
             #print(f"marks {marks}")
             marks_Total += marks
        percentage = marks_Total/len(student_detailed_report[student_rollNo])
        student_report_card.append((student_rollNo,marks_Total,percentage))

    #print(student_report_card)
    return student_report_card

##print the details
def print_report_card(stud_report_card):
    print("--------------SCORE CARD--------------".center(50))
    print(f"Roll No | Grand Total | Percentage".center(50))
    for dtls in stud_report_card:
        rollNo = dtls[0]
        Grand_Total = dtls[1]
        Percentage = dtls[2]

        print(f"{rollNo}|{Grand_Total}| {Percentage}%".center(50))

noofstudents = int(input("Enter number of students... "))
student_detailed_report = get_student_marks(noofstudents)

stud_report_card = get_student_progress_report(student_detailed_report)

print_report_card(stud_report_card)



