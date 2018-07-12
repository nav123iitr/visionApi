import io
import os
import google.cloud.vision
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'G:\\LifCare\\visionapi.json'


# Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

# TODO (Developer): Replace this with the name of the local image
# file to analyze.
image_file_name = 'G:\\LifCare\\vision\\images\\invoice jit.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

# Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
response = vision_client.text_detection(image=image)
text_file = open("text.txt", "w")
#compe = ""
for text in response.text_annotations:
    text_file.write(text.description.encode('utf-8') + " ")
#    compe += text.description.encode('utf-8') + " "
#always use .encode('utf-8') function and not .str('filename.txt')...    

#print (compe)
#text_file.write(compe)    
text_file.close()

    
   
