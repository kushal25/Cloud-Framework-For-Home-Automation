import serial
import sys

def oper( data1, data2):
	print "data1", data1
	print "data2", data2
	#ser = serial.Serial('/dev/ttyUSB0', 9600 ,timeout = 2)
	if (data1 == '1') and (data2 == 'on'):
		ser.write('A')
	elif (data1 == '1') and (data2 == 'off'):
		ser.write('B')
	elif (data1 == '2') and (data2 == 'on'):
        	ser.write('C')
	elif (data1 == '2') and (data2 == 'off'):
        	ser.write('D')
	elif (data1 == '3') and (data2 == 'on'):
        	ser.write('E')
	elif (data1 == '3') and (data2 == 'off'):
        	ser.write('F')
	elif (data1 == '4') and (data2 == 'on'):
        	ser.write('G')
	elif (data1 == '4') and (data2 == 'off'):
        	ser.write('H')
	elif (data1 == '5') and (data2 == 'on'):
        	ser.write('I')
	elif (data1 == '5') and (data2 == 'off'):
        	ser.write('J')
	elif (data1 == '6') and (data2 == 'on'):
        	ser.write('K')
	elif (data1 == '6') and (data2 == 'off'):
        	ser.write('L')
	elif (data1 == '7') and (data2 == 'on'):
        	ser.write('M')
	elif (data1 == '7') and (data2 == 'off'):
        	ser.write('N')
	elif (data1 == '8') and (data2 == 'on'):
        	ser.write('O')
	elif (data1 == '8') and (data2 == 'off'):
        	ser.write('P')
	elif (data1 == '9') and (data2 == 'on'):
        	ser.write('Q')
	elif (data1 == '9') and (data2 == 'off'):
      	 	 ser.write('R')
	else :
		print 'ERROR'

if __name__ == "__main__":
	oper( sys.argv[1], sys.argv[2] )	
