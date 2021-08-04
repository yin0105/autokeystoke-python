import time, sys, random, keyboard
from pynput.keyboard import Key, Controller
from datetime import datetime

ctrlr = Controller()  # Create the controller


def waiting():
    print("starting ...")
    for i in range(20, 0, -1):
        print(i)
        time.sleep(1)
    

def type_string_with_delay(string):
    global transition

    count_window = (int)(input("Please enter count of windows : ")) - 1
    print("count window = ", count_window)   
    tab_index = (int)(input("Please enter tab index : "))    
    waiting()
    prev_time = datetime.now()
    while True:
        for character in string:        
            if transition and (datetime.now() - prev_time).seconds >= 115:                        
                if random.random() < 0.6:
                    alt_tab_count = tab_index
                else:
                    alt_tab_count = random.randint(2, count_window)
                print("alt_tab_count = ", alt_tab_count)
                
                ctrlr.press(Key.alt)
                for i in range(alt_tab_count):
                    ctrlr.press(Key.tab)
                    ctrlr.release(Key.tab)
                    time.sleep(0.1)
                ctrlr.release(Key.alt)
                time.sleep(0.5)

                if alt_tab_count == tab_index:
                    ctrlr.press(Key.ctrl)                
                    ctrl_tab_count = random.randint(1, 10)
                    print("ctrl_tab_count = ", ctrl_tab_count)
                    for i in range(ctrl_tab_count):
                        print("ctrl tab : ", i)
                        ctrlr.press(Key.tab)
                        ctrlr.release(Key.tab)
                        time.sleep(0.1)
                    ctrlr.release(Key.ctrl)
                    time.sleep(0.5)

                print("== restore tab position ==")
                ctrlr.press(Key.alt)
                ctrlr.press(Key.tab)
                ctrlr.release(Key.tab)
                ctrlr.release(Key.alt)
                time.sleep(0.5)

                if alt_tab_count > tab_index:
                    tab_index += 1
                elif alt_tab_count == tab_index:
                    tab_index = 1

                prev_time = datetime.now()
            else:
                ctrlr.type(character)

            delay = random.randint(5, 20)  # Generate a random number between 0 and 10
            
            count = 0
            while count < delay:
                try: #used try so that if user pressed other than the given key error will not be shown
                    if keyboard.is_pressed(' '): #if key 'a' is pressed 
                        print('You Pressed "Break" Key!')
                        waiting()
                        break #finishing the loop
                    else:
                        pass
                except Exception as e:
                    print("=== error ", e)
                    time.sleep(4)
                    break 
                time.sleep(0.1)
                count += 1

transition = True
if len(sys.argv) > 1 and sys.argv[1] == "-n":
    print("== No Transition ==")
    transition = False

type_string_with_delay("""
New report in yogo-admin -> Reports.

Name: "Classes". Placed in Reports sub menu above "Salary" report.

Content: All classes in specified time period. See attached sample.

Formats: 
Screen (show report for default date selection automatically)
pdf
xlsx
csv. This format should be identical to the others, except for that the bottom line with totals should be omitted.

UI: 
Two datepickers, "Start date" and "End date". Default selected date interval is the last whole month (just like the Salary report), so if today is May 15, default selected date interval is April 1 - April 30. Max time period is one year. If a longer period is selected, show the message "Max time period is one year" under the date pickers, don't show report on screen and disable download buttons.
Treeselect with label: "Teacher". Default selection: All teachers. If "All teachers" are selected, also include archived teachers, ie don't filter records by teacher.
Treeselect with label "Class type". Default selection: All class types. If "All Class Types" is selected, also include archived class types, ie don't filter records by class type.
Checkbox: "Only classes with physical attendance" = Only include classes with physical_attendance_enabled : 1 
Checkbox: "Only classes with livestream"Only include classes with livestream_enabled : 1  (Note that these two checkboxes do not exclude each other, as a class can be physical, livestream, or both.)
Checkbox, only visible if ClassPass integration is enabled: "Only classes with ClassPass.com booking enabled"

Table:
"Branch" field is only included if client has more than one branch
Fields "Physical attendance", "Livestream" and "Livestream sign-ups" are only included if client setting iivestream_enabled is true.
Fields "ClassPass.com enabled" and "ClassPass.com sign-ups" are only included if client_setting classpass_com_enabled is true
Values "Yes" and "No", should be localized
""")