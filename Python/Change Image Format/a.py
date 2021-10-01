import glob
import cv2

print("1:  jpg to png")
print("2:  jpg to tif")
print("3:  jpg to bmp")
print("4:  png to jpg")
print("5:  png to tif")
print("6:  png to bmp")
print("7:  tif to jpg")
print("8:  tif to png")
print("9:  tif to bmp")
print("10: bmp to jpg")
print("11: bmp to png")
print("12: bmp to tif")

x = (int)(input("\nEnter your choice : "))
image_format = ["jpg", "png", "tif", "bmp"]

temp = int((x-1)/3)
y = (x - 1) % 3

if y >= temp:
    y += 1

if x > 12 or x < 1:
    print("\nInvalid Choice\n")
    print("Try with valide choice\n")
    exit()

input_image_format = image_format[(int(temp))]
output_image_format = image_format[(int(y))]

images = glob.glob("Input Images/*.{}".format(input_image_format))

if len(images) == 0:
    print("\n\nThere is no {} images in 'Input Images' Folder/Directory.\n\n".format(input_image_format))

else:
    for image in images:
        new_image = image[13:-3]
        new_image += output_image_format
        img = cv2.imread(image)

        cv2.imwrite("Output Images/{}".format(new_image), img)

    print("\n\nAll the images with {} is succesfully converted to {}.".format(
        input_image_format, output_image_format))
    print("\n\nThank you for using this tool.\n\n")
