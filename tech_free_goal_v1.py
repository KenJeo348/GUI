import easygui

tech_used = easygui.enterbox("Please enter each of the days on which you used"
                             " technology.\n Separate each day with a space",
                             "Days tech was used.")
tech_used_list = tech_used.split(" ")
tech_used_days = len(tech_used_list)
tech_free_days = 7 - tech_used_days
if tech_free_days >= 3:
    easygui.msgbox(f"Congratulations! You had {tech_used_days} tech"
                   f"You met your goal with {tech_free_days} tech free days.")

