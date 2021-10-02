from PIL import Image
import pytesseract

im = Image.open("../../test_images/text.png")
text = pytesseract.image_to_string(im,lang="tur")
print(text)
