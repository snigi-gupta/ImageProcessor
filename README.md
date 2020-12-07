# ImageProcessor

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
| # |        Status                                                                 | Date 
|---|-------------------------------------------------------------------------------|------
| 1 |Bird-eye planning completed                                                    | 11/02
| 2 |Requirement Gathering completed                                                | 11/02
| 3 |Basic setup completed                                                          | 11/02
| 4 |Created folder structure and configuration file for the application            | 11/02
| 5 |Read articles related to this project. Saw few examples.                       | 11/03
| 6 |Created HTML form that accepts image media and stores in Local                 | 11/03
| 7 |Working on storing the image with a unique uuid.                               | 11/03
| 8 |Finished storing the image with a unique uuid.                                 | 11/04
| 9 |Added a few image config						                                | 11/04
|10 |Return uploaded image feature completed		                                | 11/04
|11 |Created a new template for returning the uploaded                              | 11/05
|12 |Fixed some file path issues                                                    | 11/05
|13 |Created image url for 'edit' route                                             | 11/05
|14 |Created route to display submitted image                                       | 11/06
|15 |Enabled resizing the image                                                     | 11/06
|16 |Converting image to webp format. Having issues with conversion                 | 11/07
|17 |converting image to webp successfull, however, image not getting saved in webp | 11/08
|18 |Understanding caching and researching library fit for the project				| 11/08







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
**3.	What is the objective of this task?**<br>
The aim of this task is to build a system that takes an image as an input from a user as a form of request and allows the user to edit/transform the image via url-parameters. This task solves the underlying problem mentioned in point (1).<br>
**4.	What is the expected output?**<br>
At the end of this task, there should a deployable code that takes in an input image and returns a url using which a user can alter and manipulate the image. This project will allow basic operations to be applicable on the image. Namely changing width, height, and crop.<br>
**5. Specific Requirements**<br>
  - URLs are immutable.<br>
  - Source file should be processed based on URL parameters.<br>
  - Processed image should be cached to server 1 or 1 million requests to the same image with same URL parameters.<br>
  - A 5 second cut-off should be aimed for total processing for each image.<br>
  - This project should be completed in two weeks. Project Start Date: November 2, 2020 | Project End Date: November 16, 2020.<br>
 - - - -
 ### Phase 2 - Setup of Project and versioning system
 - Using Python 3 as coding language.
 - Using basic HTML for forms.
 - Using OpenCV or equivalent for image processing.
 - Using Flask as Web Application Framework.
 - Using PyCharm as IDE.
 - Using Jinja2 as template engine.
 - Yet to decide on caching/ API Caching and CDN technologies.
 - - - -
 ### Phase 2 and 3 - Design and Development
- Create a file structure suitable for the project.
- Create a simple architecture of wireframes, routes, and APIs.
