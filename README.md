# Image Downloader
Most probably, many of you know big data concept in today's world. So, images, sounds and other all data types can be part of a big data. In that project we are dealing with images.
With that project we can download many images from different websites in any categories.

## Why I start that project?
When I was a member of autonomous vehicle project in Marmara University, I dealed with machine learning part. In that part, first of all we have to collect data and learn
them to vehicle to provide safety driving. In that time we faced really big problems especially to find data. So, I started to develop that image downloader.

In the future, I am going to add new websites, APIs, Gui and object labelling parts to that project.
Right now, just you can download many images in different categories.

## How it works?
That project hasn't a ui. So you should use terminal. 
<br/> 
python main.py 
<br/>
Then, you should write the data names which you want to download with commas. As an example;
<br/>
cat,dog,elephant,car,bicyle
<br/>
Then press enter and write amoutns of each category like
<br/>
25,30,10,100,40
<br/> 
Then the programs starts to get links from related websites and it downloads images which you want.

### Requirements
opencv-python <br/>
bs4 <br/>
requests <br/>
keyboard <br/>
lxml <br/>
pandas <br/>
matplotlib <br/>
cv2 <br/>
