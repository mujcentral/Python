import jsonlines
import cv2
num=0
with jsonlines.open('Address of .jsonl file') as data:
 for line in data:
    coordinates=line['prediction']['bboxes']
    address=line['instance']['content'].replace('_','\\')
    temp_img = cv2.imread(address, cv2.IMREAD_COLOR)
    img=cv2.resize(temp_img,(720,500))
    x_min=line['prediction']['bboxes'][0][0]
    y_min=line['prediction']['bboxes'][0][1]
    x_max=line['prediction']['bboxes'][0][2]
    y_max=line['prediction']['bboxes'][0][3]
    image = cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (255,0,0), 2)
    cv2.imwrite('Address where the images are to be stored'+str(num)+'.jpg',image)
    num+=1