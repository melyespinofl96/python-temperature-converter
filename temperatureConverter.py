import PySimpleGUI as sg

layout = [
    [sg.Text('Tempeture Converter', font=('Arial', 15, 'bold'), pad = (0, 5))],
    
    [sg.Text('From: ', font=('Arial', 12, 'bold')), sg.Combo(['Celsius', 'Fahrenheit', 'Kelvin'], default_value = 'Celsius', key = 'from'),
     sg.Text('To: ', font=('Arial', 12, 'bold')), sg.Combo(['Celsius', 'Fahrenheit', 'Kelvin'], default_value = 'Fahrenheit', key = 'to')],
    
    [sg.Input([], size = 30, key = 'input'), sg.Button('Convert', key = 'convert')],
    
    [sg.Text(key = 'output')]
]

window = sg.Window('Tempeture Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'convert':
        inputValue = values['input']
        fromValue = values['from']
        toValue = values['to']
        
        if inputValue.isnumeric():
            if fromValue == toValue:
                    outputString = f'Enter a diffrent unit to convert to'
            
            #Celsius
            if fromValue == 'Celsius' and toValue == 'Fahrenheit':
                    output = round((float(inputValue) * 9/5) + 32, 2)
                    outputString = f'{inputValue} °C = {output} °F'
                    
            if fromValue == 'Celsius' and toValue == 'Kelvin':
                    output = round(float(inputValue) + 273.15, 2)
                    outputString = f'{inputValue} °C = {output} K'
            
            #Fahrenheit
            if fromValue == 'Fahrenheit' and toValue == 'Celsius':
                    output = round((float(inputValue) - 32) * 5/9, 2)
                    outputString = f'{inputValue} °F = {output} °C'
            
            if fromValue == 'Fahrenheit' and toValue == 'Kelvin':
                    output = round((float(inputValue) - 32) * 5/9 + 273.15, 2)
                    outputString = f'{inputValue} °F = {output} K'
            
            #Kelvin
            if fromValue == 'Kelvin' and toValue == 'Celsius':
                    output = round(float(inputValue) - 273.15, 2)
                    outputString = f'{inputValue} K = {output} °C'
                    
            if fromValue == 'Kelvin' and toValue == 'Fahrenheit':
                    output = round((float(inputValue) - 273.15) * 9/5 + 32, 2)
                    outputString = f'{inputValue} K = {output} °C'
    
    window['output'].update(outputString)
    
window.close()

#Formulas
#(0°C × 9/5) + 32 = 32°F
#0°C + 273.15 = 273.15K
#(0°F − 32) × 5/9 = -17.78°C
#(0°F − 32) × 5/9 + 273.15 = 255.372K
#0K − 273.15 = -273.1°C
#(0K − 273.15) × 9/5 + 32 = -459.7°F