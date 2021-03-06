import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' # your Tesseract-OCR installed location


result = pytesseract.image_to_string(r'C:\Users\shin\Pictures\Samsung\Scan04302020_195211.BMP', lang="kor") # your image file
# print(result)

f = open('file.txt', 'w', encoding='utf-8')
f.write(str(result))
f.close()

from gtts import gTTS
tts = gTTS(str(result), lang='ko')
tts.save('tts.mp3')
