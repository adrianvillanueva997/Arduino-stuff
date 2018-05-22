import pyfirmata

board = pyfirmata.Arduino("COM3")

print('connected to: ' + str(board))
pin = board.get_pin('d:3:p')  # Digital : pin:3 : p:PWM
print('connected to: ' + str(pin))
while True:
    pin.write(0)
    print('ON')
    board.pass_time(1)
    pin.write(1)
    print('OFF')
    board.pass_time(1)
