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
            return 'not file path'
        return "remove"
    else:
        os.mkdir(filePath)
        return "mkdir"

def removeTextfile(textPath):
    if os.path.exists(textPath):
        os.remove(textPath)
        return "text file remove"
    else:
        return "Notfound text file"

    print(3)


print(removeAllFile('./newImg'))
print(removeTextfile('./pay.txt'))
# 파일 읽기 시작
f = open('./pay.txt','w')
#for root, dirs, files in os.walk(path):
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
f.close()

"""
현재작업
1. 이미지 지정 영역 자른 후 새로운 파일로 저장
2. 새로 저장된 이미지 텍스트 추출
3. 텍스트 추출된 이미지 txt 파일에 작성
4. 재실행 시 과거 파일 삭제

추가작업
1. 이미지 지정 영역 드래그로 지정하기
2. 네이버 로그인 네이버 페이 쿠폰 등록 페이지 이동
3. 텍스트 한줄씩 읽고 붙여넣기
4. 텍스트에 기호 삭제
"""
