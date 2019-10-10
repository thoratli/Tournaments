import PySimpleGUI as sg
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to Tournaments!')],
            [sg.Button('New Tournament')],
            [sg.Button('Find existing Tournament')]
            ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break

    if event == 'New Tournament':
        window.close()

        while True:
            event, values = window.read()
            layout = [[sg.Text('Tournament name: '), sg.InputText()],
                      [sg.Text('How many players: '), sg.InputText()],
                      [sg.Text('How many rounds'), sg.InputText()],
                      [sg.Button('Confirm')]
                      ]


            window = sg.Window('Window Title', layout)

            if event in (None, 'Confirm'):  # if user closes window or clicks cancel
                window.close()
                exit()
            # if event == 'Confirm':
            #     window.close()

    # print('You entered ', values)

# window.close()