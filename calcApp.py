import PySimpleGUI as sg

# Function to create a new window.
# Param: theme (passed by user)
def create_window(theme):
    ##### THEMES #####
    # In PySimpleGUI we can customize themes using sg.theme() -> Such as Dark Mode
    # Options can be set using sg.set_options() -> Such as button sizes, padding, etc.
    # Each element has customization options
    sg.theme(theme) # Gives us a dark theme -> Note: ANY elements before this line would NOT have the dark theme

    # Font is set to Franklin and size 14. Button_element_size insicates buttons are 6 CHARACTERS wide, 3 CHARACTERS high
    sg.set_options(font = 'Franklin 14', button_element_size = (6, 3)) # -> Font Size
    button_size = (6, 3) # Buttons are 6 characters wide, 3 characters high

    layout = [
        [sg.Text(
            '', # What is (initially) displayed in the calculator window (an empty string)
            font = 'Franklin, 26', #font: Character font is set to Franklin, size 14
            justification = 'right', #justification: how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
            expand_x = True, # expand_x : If True the element will automatically expand in the X direction to fill available space
            pad = (10, 20), # pad: Amount of padding to put around element in pixels (left/right, top/bottom) or ((left, right), (top, bottom)) or an int. If an int, then it's converted into a tuple (int, int)
            right_click_menu = theme_menu, # right_click_menu: A list of lists of Menu items to show when this element is right clicked
            key = '-TEXT-') # key: Used with window.find_element and with return values to uniquely identify this element to uniquely identify this element
            ],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
    ]

    return sg.Window("Calculator", layout)

# A menu of theme options for the user to select from. When user selects a (new) theme, the current window will close and a new one with selected theme will open
# Params: menu: name of the menu
# Param: ['LightGrey1', 'dark', 'DarkGray8', 'random']: a list of theme options
# Each element in the menu is effectively a button, so if we click any of them, an event with their name should be called
theme_menu = ['menu',['LightGrey1', 'dark', 'DarkGray8', 'random']]

# Call create_window function. Window will have the dark theme
WIN = create_window('dark')


currentNum = [] # A list containing the current numbers selected by the user
full_operation = [] # A list containing the current operator selected by the user

while True:
    event, values = WIN.read()

    if event == sg.WIN_CLOSED:
        break

    # If user selects a theme from the themes menu list the current window will close, and a new window with the selected theme opens
    if event in theme_menu[1]:
        # print(event)
        WIN.close() # Close current window
        WIN = create_window(event) # Create new window with our selected theme

    # If any numbers were pressed
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        # print(event)
        currentNum.append(event) # Append each selected number to the end of the current list of numbers
        num_string = ''.join(currentNum) # Create a string from the list of numbers
        WIN['-TEXT-'].update(num_string) # Update the window to display users current string of numbers (text)

    # If event is one of the operator keys
    if event in ['+', '-', '/', '*']:
        # print(event)
        # When the user presses an operator button, we want to get our full_operation list, and append the current number to it (as a string)
        full_operation.append(''.join(currentNum))
        currentNum = [] # Empty our currentNum list
        full_operation.append(event) # Append our event to the full_operation list
        WIN['-TEXT-'].update('') # After we click an operator, we want to empty the text field (by updating with an empty string)

    # If event is 'Enter' key
    if event in 'Enter':
        # print(event)
        # If event is 'Enter' key, we want to get the full_operation, and append the currentNum
        full_operation.append(''.join(currentNum))
        result = eval(' '.join(full_operation)) # eval() evaluates a string with math operations inside (ex: eval('2+2'))
        WIN['-TEXT-'].update(result) # Update our window to display current evaluated result
        full_operation = [] # Empty full_operation, so if we click anything else, it will not be appended to our current window
    
    # If event is 'Clear' key
    if event in 'Clear':
        # print(event)
        # If we click the 'Clear' button, all teh input disappears and we essentially start from scratch
        currentNum = [] # Set currNum to an empty list
        full_operation = [] # Set full_operation to an empty list
        WIN['-TEXT-'].update('') # Set window text to an empty string

WIN.close()