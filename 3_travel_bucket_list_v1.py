import easygui

while True:
    favourite_places = easygui.enterbox("Enter the name of 5 places you would"
                                        "like to visit.\nSeparate each place"
                                        "name with a comma.", "Enter favourite"
                                                              "places")
    bucket_list = favourite_places.split(",")

    if len(bucket_list) == 5:
        for place in bucket_list:
            places = "\n".join(bucket_list)
        easygui.msgbox(f"My bucket list: \n{places}")
    else:
        easygui.msgbox("Sorry but you have to enter '5' places, but you "
                       f"entered {len(bucket_list)} places.")
