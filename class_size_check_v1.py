import easygui

while True:
    school_name = easygui.enterbox("Enter the name of your School",
                                   "School Name")
    maximum_class_size = easygui.integerbox("What is the maximum number of "
                                            "students allowed per class.\n"
                                            "Must be between 10 and 30",
                                            "Maximum class size.",
                                            lowerbound=10, upperbound=30)

    student_number = easygui.integerbox("What is the total number of children"
                                        f"at {school_name}:\n"
                                        f"The number must be between 10 and 1400"
                                        , "Total number of students",
                                        lowerbound=10, upperbound=1400)

    required_teachers = student_number//maximum_class_size + 1

    teacher_number = easygui.integerbox("How many teachers do you have at your"
                                        " school?\n"
                                        "There must be between 1 and 120",
                                        "Total amount of current teachers.",
                                        lowerbound=1, upperbound=120)

    teacher_difference = teacher_number - required_teachers
    if teacher_difference == 0:
        easygui.msgbox("Congratulations you have the right amount of teachers.")
    elif teacher_difference >= 0:
        easygui.msgbox("You have too many teachers at your school.\n"
                       f"You could fire {teacher_difference} teachers")
    else:
        easygui.msgbox("You don't have enough teachers at your school.\n"
                       f"You would have to hire {abs(teacher_difference)} teachers")

    play_again = easygui.buttonbox("Would you like to perform another calculation."
                                   , "Play again", choices=["Yes", "No"])

    if play_again == "No":
        easygui.msgbox("Goodbye", "Farewell")
        break
