## Structure of the project
*yet to confirm*

*similar to google drive*

## *TODO*: 
*ADD USER UPLOADS*

*METADATA FILE TO STORE USERNAME AND IMAGE UPLOADED*

*USER AUTHNTICATION --?*

*BETTER HTML DESIGN*

## Main Pages

`/`

    Redirects to /login if not logged in
    else redirects to /user/list/5 - to display 5 recently uploaded images

`/login`

    Allows user to login if username and password is correct

`/signup`

    Allows users to create new user

--- 

## Uploading an image

`/<user>/upload/`

    a web page with upload button

--- 

## Viewing the images

`/<user>/list/n/`

    diplay last n images uploaded with thumbnails
        if no images are available display message to upload

    Upload button at the TOP
        redirects to /<user>/upload

`/<user>/view/<image-id>`
    display a single image with that id at default size - medium

`/<user>/view/<image-id>/[s-m-l-o]`
    display the image with image id at the specified size [small, medium, large, original]

---

[OPTIONAL]
## Deleting the image

`/<user>/delete/image-id`

    deletes the image if present 


<!-- ## Downloading an image

`/get/image-id/`
    
    to get the default size - medium

`/get/image-id/[s/m/l/o]/`
    
    Small, Medium, Large and Original -->



## Storing the images

## Locally 
[Uploading Files](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files)

`flask.save('/path/to/save')`
save files in the server directly

## METADATA

email, password, user_name = email id until @ symbol



## Cloud

Store the image in s3 bucket and fetch the image from there.

## Flow

*change*

/upload/ + image  --> store_db --> return OK Response

/get/image-id  -- fetch_image --> return image

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