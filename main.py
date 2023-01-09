import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
path = dir + 'img/'

def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
            return 'file remove'
        else:
            return 'Notfound file'
    else:
        os.mkdir(filePath)
        return "mkdir"

def removeTextfile(textPath):
    if os.path.exists(textPath):
        os.remove(textPath)
        return "text file remove"

    else:
        return "Notfound text file"


print(removeAllFile('./newImg'))
print(removeTextfile('./pay.txt'))

# 파일 읽기 시작
if os.stat('./img').st_size != 0:
    f = open('./pay.txt', 'w')

for root, dirs,files in os.walk(path):
    for idx, file in enumerate(files):
        print(file)
        fname, ext = os.path.splitext(file)
        if ext in ['.jpg', '.png']:
            im = Image.open(path + file)
            width, height = im.size


            crop_image = im.crop((150, 693, 630, 730))
            crop_image.save('./newImg/' + str(idx + 1) + '.jpg')
            image = Image.open('./newImg/' + str(idx + 1) + '.jpg')
            newStr = pytesseract.image_to_string(image)
            result = newStr.replace(" ", "")
            f.write(result)
    """
      except:
            f.close()
            print("비정상 종료")
        
        else:
            print("정상 종료")
 """



