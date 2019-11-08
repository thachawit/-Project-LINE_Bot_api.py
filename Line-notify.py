import requests
import datetime
url = 'https://notify-api.line.me/api/notify'
token = '4T9p8MqZfJZO15j9OaNNzE4fDOk4pNe3RjeVI4oiY1h'	#EDIT (depends on group or person)
headers = {'Authorization':'Bearer '+token}

def _lineNotify(payload,file=None):
    return requests.post(url, headers=headers , data = payload, files=file)

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)
    
# notifySticker(40,2) #(sticker position,sticker package(from left side))
# notifyPicture("https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQgloeY3pgm5As2PsZ0LL4IYdFzyft53yjgXH6WNQ8Z4sGYHRRc")


# thetime="2019-11-08 14:57"
# def notifyMessage(thetime):
# while True:
#     recently = datetime.datetime.now()
#     string= str(recently)[0:16]
#     if thetime == string:
#         url = 'https://notify-api.line.me/api/notify'
#         token = '4T9p8MqZfJZO15j9OaNNzE4fDOk4pNe3RjeVI4oiY1h'
#         headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
#         msg = 'Notify at' thetime[11:]
#         r = requests.post(url, headers=headers , data = {'message':msg})
#         print(r.text)
#         break
        
#     else:
#         print(recently)
    







