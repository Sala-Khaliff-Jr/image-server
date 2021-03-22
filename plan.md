## Structure of the project
*yet to confirm*

*similar to google drive*

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

store image locally using sql lite


## Flow

/upload/ + image  --> store_db --> return OK Response

/get/image-id  -- fetch_image --> return image


*click or argparse*
    
    probably stick with argparse
    flask uses click

Sample link

http://aaugh.com/imageabuse.html

Amazon Cover Image example  

http://images.amazon.com/images/P/0971633894.01._PT-90_PE10_PT-90_PE20_PT-90_PE30_PT-90_PE40_.jpg

raw image
    http://images.amazon.com/images/P/0971633894.01.jpg
