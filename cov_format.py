import numpy as np
import SimpleITK as sitk
import os
import h5py

def read_image(path):
    img = sitk.ReadImage(path)
    array = sitk.GetArrayFromImage(img)
    return img, array
    
def write_image(array, path, origin = (0,0,0), spacing = [1,1,1]):
    image = sitk.GetImageFromArray(array)
    image.SetOrigin(origin)
    image.SetSpacing(spacing)
    sitk.WriteImage(image, path)

input_folder_path = r'' # modify
output_folder_path = r'' # modify
size_output = 64 # output size

for root, dirs, files in os.walk(path_in):
    for name in files:
        image, array = read_image(os.path.join(root, name))
        Train_data = array.reshape((1,1,size_output,size_output,size_output))
        path_out = output_path + '\\' + name.split('.')[0] + '.h5'
        fw = h5py.File(path_out, 'w')
        fw['data'] = Train_data
        fw.close()
