import os
import io
import re
import mysql.connector
from google.cloud import vision
from google.oauth2 import service_account
credentials = service_account.Credentials. from_service_account_file('My First Project-94f40dc7e722.json')
client = vision.ImageAnnotatorClient(credentials=credentials)
#client=vision.ImageAnnotatorClient('My First Project-94f40dc7e722.json')
with io.open('LicPlateImages/test11.jpg','rb') as image_file:
    content = image_file.read()
image=vision.types.Image(content=content)
response=client.label_detection(image=image)

labels = response.label_annotations
#print('Labels:')
#for label in labels:
#    print(label.description)
response = client.text_detection(image=image)
texts=response.text_annotations
"""print('Texts:')
for text in texts:
    print('\n"{}"'.format(text.description))
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])
    print('bounds: {}'.format(','.join(vertices)))"""

"""objects = client.object_localization(image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
    print('\n{} (confidence: {})'.format(object_.name, object_.score))
    print('Normalized bounding polygon vertices: ')
    for vertex in object_.bounding_poly.normalized_vertices:
        print(' - ({}, {})'.format(vertex.x, vertex.y))"""

"""for page in response.full_text_annotation.pages:
    for block in page.blocks:
        print('\nBlock confidence: {}\n'.format(block.confidence))
        for paragraph in block.paragraphs:
            print('Paragraph confidence: {}'.format(paragraph.confidence))
            for word in paragraph.words:
                word_text = ''.join([
                        symbol.text for symbol in word.symbols])
                print('Word text: {} (confidence: {})'.format(word_text, word.confidence))
                for symbol in word.symbols:
                    print('\tSymbol: {} (confidence: {})'.format(symbol.text, symbol.confidence))"""
for text in texts:
    print('\n"{}"'.format(text.description))


print "Over"
print "\n"
def prints(nplate):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbtest"
    )

    mycursor = mydb.cursor()
    y=0
    z=(nplate, )
    sql = "SELECT * FROM vehicle inner join registration on vehicle.LoginID=registration.LoginID where Numplate = %s"
    mycursor.execute(sql, z)
    myresult = mycursor.fetchall()
    if len(myresult)!=0:
        for x in myresult:
            l5=x[1:2]
            l6=x[5:9]
            y=y+1
        if(y==1):
            print("Person Identified-Gate Open")
            print "\n"
        else:
            print("Unidentified object")
        print "The Details of the member: -   \n"
        l=l5+l6
        det=['Numplate: -','First Name: -','Last Name: -','Email ID: -','Phone Number: -']
        for j in range(len(l)):
            print det[j]+"   "+l[j]
    else:
        print "Numberplate is not registered in the data base"
def recheck(str):
    x = re.findall("\w\w\W\d\w\W\w\w\W\d\d\d\d",str)
    y = re.findall("\w\w\w\w\w\w\d\d\d\d",str)
    if len(x)==1|len(y)==1:
        return 5
c=0
for i in texts:
    numplate=i.description
    print numplate
    bool=recheck(numplate)
    if(bool==5):
        break
    c+=1
print "Final Result:-",numplate
prints(numplate)

    
