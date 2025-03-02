'''
In this example I use single image, multiple images, and with different lanaguage
'''
from PIL import Image
from pathlib import Path
import pytesseract, os

def single_img(img_name):
    print(pytesseract.image_to_string(Image.open(img_name)))

def single_img_method2(img_name):
    img = Image.open(img_name)
    text = pytesseract.image_to_string(img)
    print(text)
    
def single_lang_chi(img_name):
    #print(pytesseract.image_to_string(Image.open(img_name),lang='eng+chi_tra'))
    print(pytesseract.image_to_string(Image.open(img_name),lang='eng+chi_tra+chi_sim'))
def multiple_file(directory):
    files = Path(directory).glob('*.png')
    for file in files:
        print(file)
        #print(pytesseract.image_to_string(Image.open(file)))
        print(pytesseract.image_to_string(Image.open(file),lang='eng+chi_tra+chi_sim'))
        #print('\n----------\n')


#single image
img_name = 'ex1_eng.png'
img_name1 = 'ex2_chi_trad.png'
img_name2 = 'ex3_chi_simple.png'

print(f'====Extract img with english method1====')
single_img(img_name)
print(f'====Extract img with english method2====')
single_img_method2(img_name)
print(f'====Extract img with chinese traditional====')
single_lang_chi(img_name1)
print(f'====Extract img with chinese simple====')
single_lang_chi(img_name2)

directory= Path().resolve()
multiple_file(directory)
