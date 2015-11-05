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
 

def dec():
 image=raw_input("enter url of image :")
 im=Image.open(image)
 data=stepic.decode(im)
 print data
 
  print('Thaank you')

s=raw_input('enter \n1-encryption\n2-decryption\n\n')
if(int(s) is 1):
 enc()
elif(int(s) is 2):
 dec()
else :
 print('Invalid')

