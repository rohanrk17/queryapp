1. project Name
mentorApplication
This application provides api's for interaction between users and mentor.

2.Description:
This application provides certain api to register user,login,post queries to mentos or viceversa.
All the endpoints use jwt authentication.Once the user posts queries he automatically receives notification via email.

Here Django drf framework is used to build api's and authentication is done using email instead of username and even is captured ie(User/Mentor).
Even while posting queries the user can provide document as attachment.


3. How to Install and Run the Project
Creating virtual env by running below commandsI
a.virtualenv -p python3.7 venv
b.source venv/bin/activate (To activate env)
c.deactivate (To deactivate env)

Once above steps are done run pip install -r requirements.txt (to install required modules)
I
python manage.py makemigrations
python manage.py migrate (To migrate db config)

python manage.py runserver (to run the application)

Here 3 applications are created
1.  Authentication :To handle authentiction like register user,login user 
2.  Query:To handle api's related posting queries ,fetching queries etc
3.  User:To handle api's related user role

Swagger implementation of  all API's.