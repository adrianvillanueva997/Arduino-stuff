import pyfirmata

LED_PIN = 13

board = pyfirmata.Arduino("COM3")
print('connected to: ' + str(board))
while True:
    board.digital[LED_PIN].write(0)
    print('ON')
    board.pass_time(1)
    board.digital[LED_PIN].write(1)
    print('OFF')
    board.pass_time(1)
