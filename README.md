![alt text](https://فارسینو.com/wp-content/uploads/2021/01/%D9%81%D8%B1%D9%88%D8%B4%DA%AF%D8%A7%D9%87-%D8%A7%DB%8C%D9%86%D8%AA%D8%B1%D9%86%D8%AA%DB%8C-%D8%AF%DB%8C%D8%AC%DB%8C%DA%A9%D8%A7%D9%84%D8%A7.jpg)


### According to the task, this project has been developed in two main parts;
##### 1. Crawl the Torob website
   + Link extractor
   + Data extractor from each link

   <br>
    
##### 2. API service for manipulating the data which is powered by Django with below usage.
   + CRUD API for Product app.
   + CRUD API for Shop app.
   + An improved Django admin panel is developed which is powered by Django-jet package.
     + for sqlite;
       + username: admin
       + password: 1
       + django secret_key = 2ct5f19voo)t=+%w)h)d2l!1#f1brmncst=cv2qi3cr%$4y3&j
       
     + for using postgresql, please uncomment its config in setting.py

   <br>
    
##### 3. For an easy check I generated a PostMan export with examples for each API that is attached to root directory of project.

   <br>
    
##### 4. If you want to run the project in docker, the docker compose and docker file of each project is configured. 

   <br>
    
##### tips:
IS_DETAILED is a flag to run each crawler for work on list-view or detail-view mode.
IS_DETAILED = True means crawl on detail views one by one and IS_DETAILED=False means crawl on list view of the target.
