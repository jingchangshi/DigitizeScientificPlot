#  xml_fname="Pascioni2016_Cp_slat.xml"
xml_fname="Pascioni2016_Cp_main.xml"
#  xml_fname="Pascioni2016_Cp_flap.xml"
#  xml_fname="Murayama2014_Cp_slat.xml"
#  xml_fname="Murayama2014_Cp_main.xml"
#  xml_fname="Murayama2014_Cp_flap.xml"
xml_f=open(xml_fname,"r")
content=xml_f.readlines()
xml_f.close()
idx_pts_list=[i for i,s in enumerate(content) if "<point n=" in s]
pts_list=[content[i] for i in idx_pts_list]
x_list=[]
y_list=[]
for i in range(len(pts_list)):
    pts_str=pts_list[i].strip()
    pts_str_list=pts_str.split(' ')
    x_str=pts_str_list[4]
    y_str=pts_str_list[5]
    idx1_quote=x_str.index("'")
    idx2_quote=x_str.rindex("'")
    x_list.append(float(x_str[idx1_quote+1:idx2_quote]))
    idx1_quote=y_str.index("'")
    idx2_quote=y_str.rindex("'")
    y_list.append(float(y_str[idx1_quote+1:idx2_quote]))
import numpy as np
x_arr=np.array(x_list)
Cp_arr=np.array(y_list)
savedata=np.zeros((x_arr.size,2))
savedata[:,0]=x_arr
savedata[:,1]=-Cp_arr # Flip Y axis
csv_fname=xml_fname[:-3]+"csv"
np.savetxt(csv_fname,savedata,delimiter=',',header="X/C,Cp")
