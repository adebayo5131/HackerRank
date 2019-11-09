def gradingStudents(grades):
    # Write your code here
    new_Grades = 0
    for i in range(len(grades)):
        if grades[i] > 37:
            decision = (5*round(grades[i]/5)- (grades[i]))
            if decision < 3:
                new_Grades = (5*round(grades[i]/5))
                print(new_Grades)
        else:
                new_Grade = grades[i]
                print(new_Grades)

                          

grades = [73,67,38,33]

gradingStudents(grades)

  

