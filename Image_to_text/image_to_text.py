# import the following libraries
# will convert the image to text string
import pytesseract
import sys

# adds image processing capabilities
from PIL import Image

# to check file is written
from os.path import exists
from os import getcwd

# opening an image from the source path
#filename = "string_operations"
try:
    filename = input("Enter image filename to be converted to text file: ")
    
    print(f"Current working directory path is {getcwd()} and image file should be present in .\image folder")
    img = Image.open(r'./image/'+filename+'.jpg')

    # describes image format in the output
    #print(img)
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    with open(r'./text_file/'+filename+'.txt', mode='w') as file:
        file.write(result)
        #print(result)
    file_exists = exists(r'./text_file/'+filename+'.txt')
    #print("File writing done") if file_exists else print("Issue with file writing")
    print(f"Converted file is {getcwd()}\\text_file\{filename}.txt") if file_exists else print(f"Issue with file writing")
except Exception as e:
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
 

input('Press Enter to Continue...')