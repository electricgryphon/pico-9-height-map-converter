# pico-9-height-map-converter
Converts single channel 8-bit grayscale bitmaps (.bmp) to pico-8 sprite format. 2-pixels on sprite sheet for each pixel in image map.

Input format:<br>
Image dimensions: 64*128<br>
Note that image is asymetrically scaled.<br>
Mode: grayscale 8-bit bmp. No transparency allowed.<br>
<p>
Operation:<br>
python depth_convert-01.py image_name.bmp<br>
Output is saved to image_name_converted.txt

