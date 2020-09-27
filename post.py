from instabot import Bot 
import os
  
  
bot = Bot() 
  
bot.login(username ='HereWeGo.SIK',password = 'kis@164264') 


path = "/Users/Apple/Desktop/HereWeGo/instagram"

def getPhotoAndCaption(path):
    photo=[]
    caption=[]
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     

    for imagePath in imagePaths:
        if imagePath.endswith("jpg") :
            photo.append(imagePath)
        elif imagePath.endswith("txt") :
            caption.append(imagePath)
    return photo,caption 

def PostRecent(photo,caption) :
    for i in range(len(photo)) :
        with open(caption[i]) as file : 
            data = file.read()  
            bot.upload_photo(photo[i], caption=data)
            
def clear_folder(path) :
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    for imagePath in imagePaths:
        os.remove(imagePath)
     
photo,caption=getPhotoAndCaption(path)
PostRecent(photo,caption)