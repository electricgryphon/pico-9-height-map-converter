#python image convert to pico-8
import matplotlib.image as mpimg
import numpy as np
import sys
from math import *

def tohex(val, nbits):
	return hex((val + (1 << nbits)) % (1 << nbits))

def main():
	input_filename = sys.argv[1]
	
	
	#input_file = open(input_filename,'r')
	
	#print(input_filename.strip(".obj"))
	output_filename=input_filename.strip(".obj")+"_converted.txt"
	
	output_file = open(output_filename,'w')
	
	image=mpimg.imread(input_filename)
	
	
	#write image file to output in hex from 0x00 to 0xff
	count=1
	line=0
	hex_string=tohex(int(floor(1*255)),16)
	hex_string=hex_string[2:]
	hex_string = hex_string.zfill(2)
	print("string: "+hex_string)
	
	output_file.write("00001011111151555555d5dddddd6d66666676777771090300010000000001010000000100010002080601010000000000000000000000000000000000000000\n01010111151515555d5d5dddd6d6d6666767677777782f1e05000000000002010a0e090100010215302403000000000000000000000000000000000000000000\n")
	
	for pix in np.nditer(image):
		#if(line>1):
		#pix=count*4
		hex_string=tohex(int(floor(pix)),16)
		hex_string=hex_string[2:]
		hex_string = hex_string.zfill(2)[::-1]

		if(line<126):output_file.write(hex_string)
		#output_file.write("xx")
		count+=1
		if(count==65):
			output_file.write("\n")
			count=1
			line+=1
		#high=flr( (pix*255)/16 )
		#low=flr( (pix*255))%16
		
	
	
	#read until the firt vector
	
	#with open(input_filename) as f:
	#	output_file.write('model_v="')
	#	for line in f:
	#		if(line[:1]=='v'):
	#			line=line.strip('v ')
	#			#print(line)
	#			#output_file.write('{')
	#			point_text=line.split(' ')
	#			for num_text in point_text:
	#				#print("p: "+num_text)
	#				val=float(num_text)
	#				val=int(floor(val*256))
	#				hex_string=tohex(val, 16)
	#				hex_string=hex_string[2:]
	#				hex_string = hex_string.zfill(4)
	#				output_file.write(hex_string)
	#			#output_file.write('},\n')
	output_file.write('\nsee data below')
	

	print("\nConversion complete!\nSee output: "+output_filename)


	output_file.close()
	
	
main()
	