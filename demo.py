import cv2

# returns a 3D array for colored image ->second parameter 1
# 2D array for grayscale image -. second parameter 0
# Numpy_array imread( File_location , 0-1)
# img = cv2.imread("C://Users//lenovo//Desktop//OpenCV//image.png", 1)

# print(img)
# print(type(img))

# TO GET THE SIZE OF THE IMAGE
# print(img.shape)

# TO DISPLAY THE IMAGE
#   imshow( name_to_display , numpy_array_of_image)
#   waitKey()  ->  to wait for any keypress
#   waitKey(2000)  ->  to wait for specific time
#   destroyAllWindows() to distroy all Windows
# cv2.imshow("Material" , img)
# cv2.waitKey(2000)
# cv2.destroyAllWindows() #par farak nahi padta

# TO RESIZE IMAGE
# resize = cv2.resize(img , (int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imshow("Material Resized" , resize)
# cv2.waitKey(2000)
# cv2.destroyAllWindows() #par farak nahi padta
