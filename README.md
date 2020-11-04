# ImageProcessor

## Objective:
The aim of this task is to build a system that takes an image as an input from a user as a form of request and allows the user to edit/transform the image via url-parameters.

## Software Development Lifecycle Model
- [ ] Phase 0: Planning
- [ ] Phase 1: Requirement Gathering and Analysis
- [ ] Phase 2: Setup of Project and versioning system
- [ ] Phase 3: Designing
- [ ] Phase 4: Development
- [ ] Phase 5: Testing
- [ ] Phase 6: Deployment
- [ ] Phase 7: Deliverables
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
  - URLs are immutable<br>
  - Source file should be processed based on URL parameters<br>
  - Processed image should be cached to server 1 or 1 million requests to the same image with same URL parameters<br>
  - A 5 second cut-off should be aimed for total processing for each image<br>
  - This project should be completed in two weeks. Project Start Date: November 2, 2020 | Project End Date: November 16, 2020<br>
 - - - -
 ### Phase 2 - Setup of Project and versioning system
 - Using Python 3 as coding language
 - Using basic HTML for forms
 - Using OpenCV or equivalent for image processing
 - Using Flask as Web Application Framework
 - Using PyCharm as IDE
 - Yet to decide on caching/ API Caching and CDN technologies
 

