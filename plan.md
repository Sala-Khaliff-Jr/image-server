## Structure of the project
*yet to confirm*

*similar to google drive*

## Uploading an image

`/post/image`

    upload from command line with image_name as argument ?

return a response image has uploaded ?

*[optional]*

`/web/upload/`

    a web page with upload button

## Downloading an image

`/get/image-id/`
    
    to get the default size - medium

`/get/image-id/[s/m/l/o]/`
    
    Small, Medium, Large and Original

## Viewing the images
[optional]

`/web/list/n/`

    diplay last n images uploaded with thumbnails


## Storing the images

store image locally using sql lite


## Flow

/upload/ + image  --> store_db --> return OK Response

/get/image-id  -- fetch_image --> return image


