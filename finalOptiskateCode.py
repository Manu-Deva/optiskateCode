import time
import board
import busio
import digitalio
# import matplotlib.pyplot as plt


# Set up UART communication with Lidar sensor
uart = busio.UART(board.GP0, board.GP1, baudrate=115200)
# 14400 bytes a second,
# 14.4 bytes every millisecond
dist_array = []
time_array = []


while True:
  # Send command to Lidar sensor to request distance measurement
  uart.write(bytes([0x42, 0x57, 0x02, 0x00, 0x00, 0x00, 0x01, 0x06]))


  # Read response from Lidar sensor
  response = bytearray(9)


  # Parse distance measurement from response
  uart.readinto(response)
  while (response[0] == 0x59 and response[1] == 0x59 and response[7] != 0x59):
    uart.readinto(response)


    distance = response[2] + response[3] * 256  # distance in next 2 bytes


    if distance<300:
      led2.value = 1
      count = 0
    print((distance,))
    # Delay for a short time before taking the next measurement
    count+=1
    time.sleep(0.01)
    if count>100:
      led2.value = 0
  print (f"loop ran {x} times: ",count)
  #print(len(dist_array))
  break