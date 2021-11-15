# script for local processing of random tiles from the original dataset with awesome GDAL (https://gdal.org)
# only applicable for projected coordinate reference systems

from random import seed
from random import randint
# seed random number generator
seed(1)

# adapt your paths to your local system
path_original_img = "H:/opendemeurope/3035/data_countries/austria/all.tif"
out_high_res =  "G:/subset/hr/"
out_low_res = "G:/subset/lr/"
out_upsampled_nn = "G:/subset/lr_us_nn/"
out_upsampled_cubic = "G:/subset/lr_us_cc/" 

# adapt bbox of coordinates
xmin = 130000
xmax = 145000
ymin = 360000
ymax = 375000

# adapt size of image in meters
imagesize = 3000

# adapt size of pixel (resolution) in meters 
pixel_size_high_res = 10
pixel_size_low_res = 30

ts_high_res = imagesize / pixel_size_high_res
ts_low_res = imagesize / pixel_size_low_res

# adapt number of images
num_images = 5

for i in range(num_images):
   x_coord = randint(xmin, xmax - imagesize)
   y_coord = randint(ymin, ymax - imagesize)
   # high resolution images
   print("gdalwarp -ts ", ts_high_res ," ", ts_high_res, " -te ",x_coord," ",y_coord," ", x_coord +imagesize, " ", y_coord + imagesize , " ", path_original_img ," ", out_high_res , x_coord,"_",y_coord,".tif",sep="")
   # low resolution images
   print("gdalwarp -ts ", ts_low_res ," ", ts_low_res, " -te ",x_coord," ",y_coord," ", x_coord +imagesize, " ", y_coord + imagesize , " ", path_original_img ," ", out_low_res , x_coord,"_",y_coord,".tif",sep="")
   # upsampled images with next neighbor upsampling, default
   print("gdalwarp -ts ", ts_high_res ," ", ts_high_res, " -te ",x_coord," ",y_coord," ", x_coord +imagesize, " ", y_coord + imagesize , " ", out_low_res , x_coord,"_",y_coord,".tif ", out_upsampled_nn , x_coord,"_",y_coord,".tif",sep="")
   # upsampled images with cubic upsampling
   print("gdalwarp -ts ", ts_high_res ," ", ts_high_res, " -te ",x_coord," ",y_coord," ", x_coord +imagesize, " ", y_coord + imagesize , " -r cubic ", out_low_res , x_coord,"_",y_coord,".tif ", out_upsampled_cubic , x_coord,"_",y_coord,".tif",sep="")
  
