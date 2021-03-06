# ImageProcessor

### Shortcut Links
- [Objective](#objective)<br>
- [Software Developement Lifecycle Model](#software-development-lifecycle-model)<br>
- [Project Status](#project-status)<br>
- [Planning, Requirement Gathering and Setup](#phase-0---planning)<br>
- [Design and Development](#phase-3-and-4---design-and-development)<br>
- [Testing and Deployment](#phase-5-and-6---testing-and-deployment)<br>
- [Demo](#demo)<br>

[Go to Bottom](#conclusion)

## Objective:
The aim of this task is to build a system that takes an image as an input from a user as a form of request and allows the user to edit/transform the image via url-parameters.

## Software Development Lifecycle Model
- [x] Phase 0: Planning
- [x] Phase 1: Requirement Gathering and Analysis
- [x] Phase 2: Setup of Project and versioning system
- [x] Phase 3: Design
- [x] Phase 4: Development
- [x] Phase 5: Testing
- [x] Phase 6: Deployment
- [x] Phase 7: Deliverables

- - - -
## Project Status
| # |        Status                                                                 | Date 
|---|-------------------------------------------------------------------------------|------
| 1 |Bird-eye planning completed.                                                   | 11/02
| 2 |Requirement Gathering completed.                                               | 11/02
| 3 |Basic setup completed.                                                         | 11/02
| 4 |Created folder structure and configuration file for the application.           | 11/02
| 5 |Read articles related to this project. Saw few examples.                       | 11/03
| 6 |Created HTML form that accepts image media and stores in Local.                | 11/03
| 7 |Working on storing the image with a unique uuid.                               | 11/03
| 8 |Finished storing the image with a unique uuid.                                 | 11/04
| 9 |Added a few image config.					                                            | 11/04
|10 |Return uploaded image feature completed.		                                    | 11/04
|11 |Created a new template for returning the uploaded.                             | 11/05
|12 |Fixed some file path issues.                                                   | 11/05
|13 |Created image url for 'edit' route.                                            | 11/05
|14 |Created route to display submitted image.                                      | 11/06
|15 |Enabled resizing the image.                                                    | 11/06
|16 |Converting image to webp format. Having issues with conversion.                | 11/09
|17 |Converting image to webp successfull, however, image not getting saved in webp.| 11/10
|18 |Understanding caching and researching library fit for the project.				      | 11/10
|19 |Finished implementing caching.													                        | 11/11
|20 |Testing and providing necessary comments.										                  | 11/12
|21 |Added features to the processor. Image can be rotated and cropped (ellipse).	  | 11/12
|22 |Presentation and feedback.														                          | 11/13
|23 |Incorporated new changes as suggested and checked-in code.						          | 11/16
|24 |Completed documentation and code cleaning.									                    | 12/07

- - - -
### Phase 0 - Planning
*	Prepare a plan for the application.
*	Start documenting plan, progress and approach.
*	Decide application tech-stack, architecture, approach, code-structure.
*	Prepare Gantt-chart.
*	Research and read about unknown components involved in the project.

- - - -
### Phase 1 - Requirement Gathering
**1. What is the problem that is being solved via this task?**<br>
Images require optimization specific to context to display quickly and with high quality. Both are key metrics for engagement and conversion.
Allowing a user to change image size or dimensions on a browser provides flexibility to the user to manipulate the image on-the-fly. This feature can be then used to improve website performance as delivery speed can be enhanced by delivering the optimal version of an image for a given context.<br>

**2. Who will use this application?**<br>
This application can be used by someone who is wanting to quickly change an image and have responsive images.<br>

**3. What is the objective of this task?**<br>
The aim of this task is to build a system that takes an image as an input from a user as a form of request and allows the user to edit/transform the image via url-parameters. This task solves the underlying problem mentioned in point(1).<br>

**4. What is the expected output?**<br>
At the end of this task, there should a deployable code that takes in an input image and returns a url using which a user can alter and manipulate the image. This project will allow basic operations to be applicable on the image. Namely changing width, height, and crop.<br>

**5. Specific Requirements**<br>
  - URLs are immutable.<br>
  - Source file should be processed based on URL parameters.<br>
  - Processed image should be cached to server. 1 or 1 million requests to the same image with same URL parameters.<br>
  - A 5 second cut-off should be aimed for total processing for each image.<br>
  - This project should be completed in two weeks. Project Start Date: November 2, 2020 | Project End Date: November 16, 2020.<br>

**6. Additional Requirements given on 11/13**<br>
  - Original image should not be lost. Store images in their original format. Provide an option to convert the image to .webp format (superior lossless and lossy compressed images for web applications).<br>
  - Multiple requests should be possible.<br>
  - Create a test script to test performance of 10 requests per second.
  
 - - - -
 ### Phase 2 - Setup of Project and versioning system
 - Using Python 3 as coding language.
 - Using basic HTML for forms.
 - Using PIL for image processing.
 - Using Flask as Web Application Framework.
 - Using PyCharm as IDE.
 - Using Jinja2 as template engine.
 - Using cachetools for caching/ API Caching and CDN technologies.
 
 - - - -
 ### Phase 3 and 4 - Design and Development
- Create a file structure suitable for the project.
- Create a simple architecture of wireframes, routes, and APIs.
- Develop the APIs - Upload and Edit.
- Develop code for cache
- Enable image processing features

The following are the features the APIs provide:<br>
**1. /image route (Upload route)**<br>
  * This allows you to upload an image in any format. Stores the original image in its original format.<br>
  
**2. /edit route (Edit route)**<br>
  * This allows you to edit the width and height of the image. 
  * Convert image to .webp format for superior lossless and lossy compression
  * Rotate the image to desired degree
  * Crop the image into an ellipse (For profile pictures as rounded images)
  * Maintains the aspect-ratio of the image.<br>
  
**3. Cache**<br>
  * The API has a cache enabled. Currently for 5 mins. Any request that has been previously requested will be retrieved from the cache. After 5 mins, the cache is updated with Least Recently Used images removed.<br>
  
**4. Performance**<br>
  * Multithreaded requests or simultaneous requests can be made and the performance of 10 requests/sec is 0.17 secs. <br>
  
**5. Clickable Link**<br>
  * The edited image can be accessed as a link to be used by any API.<br>

- - - -
 ### Phase 5 and 6 - Testing and Deployment
 - A test script `test.py` was created to compute the performance of the API when simultaneous requests are hit. 
 - The performance score was 0.1705 seconds when 10 requests were hit simultaneously (locally).<br>
 ![performance](images/performance.jpeg)
 - The application is deployed on Heroku
 
 - - - -
 ## Demo
 To upload image
 ![upload_image](images/upload_image.gif)
 
 To edit the image
 ![edit_image](images/edit_image.gif)
 
 Other features
 ![ellipse_crop](images/ellipse_image.jpeg)![rotate_image](images/rotate_image.jpeg)
 
 - - - -
 ## Conclusion
 This code was created to provide an API service to the team for responsive, light-weight images. This project was also created to assess coding style of the candidate within a short period of time of 2 weeks.<br>
 
[Go to Top](#imageprocessor)
