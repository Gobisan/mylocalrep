import Image
import stepic

def enc():
 iurl=raw_input("enter url of image :")
 im=Image.open(iurl)
 text=raw_input("Enter your text :")
 im2=stepic.encode(im,text)
 curl=raw_input("Enter destination of the crypted image :")
 im2.save(curl,"PNG")
 print('Image has been saved\n\nDo you want to encrypt in another image')
 ei=input('Press \n1-Yes\n0-No\n')
 if(int(ei) is 1):
  enc()
 elif(int(ei) is 0):
  print('Thaank you')

def dec():
 image=raw_input("enter url of image :")
 im=Image.open(image)
 data=stepic.decode(im)
 print data
 di=input('Do you want to decrypt any othr image?\nPress \n1-Yes\nAny key to exit-No\n')
 if(int(di) is 1):
  dec()
 else :
  print('Thaank you')

s=raw_input('enter \n1-encryption\n2-decryption\n\n')
if(int(s) is 1):
 enc()
elif(int(s) is 2):
 dec()
else :
 print('Invalid')

