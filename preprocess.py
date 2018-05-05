from skimage import io
from os.path import join
from os import getcwd

img_fdir=getcwd()
img_fname_base="Pascioni2016_Spectra"
img_fname=img_fname_base+"_raw.png"
img_fpath=join(img_fdir,img_fname)
plot=io.imread(img_fpath)

white=[255,255,255]
red=[255,0,0]
ms=16
y1=68
x1=397
plot[y1-ms:y1+ms+1,x1-ms:x1+ms+1,:]=white
y1=150
x1=426
plot[y1-ms:y1+ms+1,x1-ms:x1+ms+1,:]=white
y1=196
x1=454
plot[y1-ms:y1+ms+1,x1-ms:x1+ms+1,:]=white
y1=202
x1=470
plot[y1-ms:y1+ms+1,x1-ms:x1+ms+1,:]=white
y1=310
x1=487
plot[y1-ms:y1+ms+1,x1-ms:x1+ms+1,:]=white
io.imsave(img_fname_base+".png",plot)

