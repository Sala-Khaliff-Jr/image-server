## Structure of the project
*yet to confirm*

*similar to google drive*

## *TODO*: 
*ADD USER UPLOADS*

*METADATA FILE TO STORE USERNAME AND IMAGE UPLOADED*

*USER AUTHNTICATION*

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

## Storing the images

Local Storage

    store file in dedicated directory for each user
        /images/user/

Cloud Storage

    ## TODO: Plan how to store and retrieve in cloud

## METADATA

email, password, user_name = email id until @ symbol



---

[OPTIONAL]
## Deleting the image

`/<user>/delete/image-id`

    deletes the image if present 

## Log out option

`/logout`

    to log the user out of the session

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