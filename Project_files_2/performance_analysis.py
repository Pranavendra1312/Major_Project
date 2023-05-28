import PSNR as psnr
import ssim as ssim
import histogram as histogram



print("Image 1 Analysis :")
psnr.PSNR('images/in1.png','images/out1.png')
ssim.SSIM('images/in1.png','images/out1.png')
histogram.Histogram('images/in1.png','images/out1.png',1)

print("Image 2 Analysis :")
psnr.PSNR('images/in2.png','images/out2.png')
ssim.SSIM('images/in2.png','images/out2.png')
histogram.Histogram('images/in2.png','images/out2.png',2)

print("Image 3 Analysis :")
psnr.PSNR('images/in3.png','images/out3.png')
ssim.SSIM('images/in3.png','images/out3.png')
histogram.Histogram('images/in3.png','images/out3.png',3)

print("Image 4 Analysis :")
psnr.PSNR('images/in4.png','images/out4.png')
ssim.SSIM('images/in4.png','images/out4.png')
histogram.Histogram('images/in4.png','images/out4.png',4)

print("Image 5 Analysis :")
psnr.PSNR('images/in5.png','images/out5.png')
ssim.SSIM('images/in5.png','images/out5.png')
histogram.Histogram('images/in5.png','images/out5.png',5)