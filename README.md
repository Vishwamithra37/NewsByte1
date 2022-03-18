# newsbytes_task
# UTM primary function:
 The code only serves one purpose: to help your analytics tool track the source of your visitor.

# Problem: 
At NewsBytes, the marketing department often finds themselves using long URLs with UTM tracking. These URLs often travel in emails, getting copied over sheets and docs, thereby are at risk of getting ruined by formatters. Objective is to design and implement a URL hashing system which would allow us to overcome these problems primarily. Things to keep in mind: URL length can't be restricted. Query parameters can’t be ignored. Click tracking should be there but hashed URLs can be made privacy aware. May be used in a secure manner as the generated URL might be single (limited) use only. You can choose to make the application with UI or only API.

# Solution:
The solution is to use a hash function to generate a unique URL, by using MD5. The new URL is stored in mongodb and is retrieved when the original URL is requested.
The Database is optimized using Time to Live index and unique hash index thereby making sure no memory over run.
The Swagger/api documentation can be obtained at /swagger-ui.

# Note:
The code is written in Python 3.9.
Gunicorn has not been used for deployment. But can be added. The dbconfig.py file is used to manage the database while config.py is used to manage the application(This includes the ports and host it is running upon).
Run the Mains.py file to start the application. Assuming the requirements are installed. Certificates for production can be installed when gunicorn is used and this code is deployed.

# Run command:
python3.9 Mains.py
