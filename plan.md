## Structure of the project
*yet to confirm*

*similar to google drive*

## *TODO*: 
*ADD USER UPLOADS*

*METADATA FILE TO STORE USERNAME AND IMAGE UPLOADED*

*USER AUTHNTICATION --?*

*BETTER HTML DESIGN*

## Uploading an image

`/post/image`

    upload from command line with image_name as argument ?

return a response image has uploaded ?

`/web/upload/`

    a web page with upload button

## Downloading an image

`/get/image-id/`
    
    to get the default size - medium

`/get/image-id/[s/m/l/o]/`
    
    Small, Medium, Large and Original

## Viewing the images

`/web/list/n/`

    diplay last n images uploaded with thumbnails


## Storing the images

## Locally 
[Uploading Files](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files)

`flask.save('/path/to/save')`
save files in the server directly

store image locally using sql lite -- probably not needed ?

## Cloud

Store the image in s3 bucket and fetch the image from there.

## Flow

/upload/ + image  --> store_db --> return OK Response

/get/image-id  -- fetch_image --> return image


*not needed*
*click or argparse*
    
    probably stick with argparse
    flask uses click

Sample link

http://aaugh.com/imageabuse.html

Amazon Cover Image example  

http://images.amazon.com/images/P/0971633894.01._PT-90_PE10_PT-90_PE20_PT-90_PE30_PT-90_PE40_.jpg

raw image
    http://images.amazon.com/images/P/0971633894.01.jpg


Flask Uploads for file upload and progressbar ?

https://pythonhosted.org/Flask-Uploads/

[Handling file uploads with flask](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)


## NOTES

svinx package for documentation 

minio - s3 interface

environment variable for image path

store images in s3

metadata file to assign username to the image uploaded