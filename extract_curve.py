from skimage import io
from skimage.color import rgb2gray
from os.path import join
from os import getcwd

img_fdir=getcwd()
img_fname_base="Pascioni2016_Spectra"
img_fname=img_fname_base+".png"
img_fpath=join(img_fdir,img_fname)
plot=io.imread(img_fpath)
# Set the X axis and Y axis
y1=1E-2
idx_y1=96
y2=1E-6
idx_y2=405
x1=1E-1
idx_x1=272
x2=1E1
idx_x2=719
red=[255,0,0]
blue=[0,0,255]
ms=4
#  plot[idx_y1-ms:idx_y1+ms+1,idx_x1-ms:idx_x1+ms+1,:]=red
#  plot[idx_y2-ms:idx_y2+ms+1,idx_x1-ms:idx_x1+ms+1,:]=red
#  plot[idx_y1-ms:idx_y1+ms+1,idx_x2-ms:idx_x2+ms+1,:]=red
#  plot[idx_y2-ms:idx_y2+ms+1,idx_x2-ms:idx_x2+ms+1,:]=red
#  io.imsave(img_fname[:-4]+"_marker.png",plot)
#  exit()

# Crop to get the core part of the plot
height_offset=23
height=460
width_offset=156
width=670
plot=plot[height_offset:height_offset+height,width_offset:width_offset+width]
#  io.imsave(img_fname[:-4]+"_crop.png",plot)
#  exit()
# Convert RGB to grayscale
plot_rgb=plot
plot_gray=rgb2gray(plot)
#  io.imsave(img_fname[:-4]+"_gray.png",plot)
#  print(plot[0:40,1])
# The target curve I want is of grayscale 0.0. The other curve is about 0.5.
# Collect the index of the target curve
import numpy as np
idx_black_row,idx_black_col=np.where(plot_gray<0.1)
# Save a marker image to check if it is OK
for i in range(idx_black_row.size):
    idx_y,idx_x=(idx_black_row[i],idx_black_col[i])
    plot_rgb[idx_y,idx_x]=red
img_marker_fname=img_fname[:-4]+"_marker.png"
img_marker_fpath=join(getcwd(),img_marker_fname)
io.imsave(img_marker_fpath,plot_rgb)
print("%s is saved."%img_marker_fpath)
# Transform to the dataset we want
x_scale=(np.log10(x2)-np.log10(x1))/(idx_x2-idx_x1)
y_scale=(np.log10(y2)-np.log10(y1))/(idx_y2-idx_y1)
x_arr=np.zeros((idx_black_row.size,))
y_arr=np.zeros((idx_black_row.size,))
for i in range(idx_black_row.size):
    idx_y,idx_x=(idx_black_row[i],idx_black_col[i])
    idx_y,idx_x=idx_y+height_offset,idx_x+width_offset
    x=np.log10(x1)+x_scale*(idx_x-idx_x1)
    y=np.log10(y1)+y_scale*(idx_y-idx_y1)
    x_arr[i]=10**x
    y_arr[i]=10**y

savedata=np.zeros((x_arr.size,2))
savedata[:,0]=x_arr
savedata[:,1]=y_arr
savedata_fname=img_fname_base+".csv"
savedata_fpath=join(getcwd(),savedata_fname)
np.savetxt(savedata_fpath,savedata,delimiter=",",header="freq,psd")
print("%s is saved."%savedata_fpath)
