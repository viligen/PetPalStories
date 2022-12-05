# PetPalStories
Live at: www.petpalstories.de

My Django Project - Nov - Dec 2022

Python Web Framework @ SoftUni

Documentation:

INITIATION: This application was created as a final project to 'Python Web Framework' course at SoftUni. It has been developed in the sake of pets.

IDEA: Creating an operational Web Application, which allows users to register, login, create, edit and delete profiles, content, interact with each other in various ways, etc. The application's name is 'PetPalStories', where the main focus is on pets - publishing Stories with pictures, creating and signing Petitions, posting and commenting in Forum, sending messages to story authors, etc.

CONTENT: PetPalStories project consists of several apps, static files folder, templates, tests and others. 
Post comments have been developed, using Django Rest Framework and JS to prevent page reloading and gain better UX performance.

DB & MEDIA: The project uses PostgreSQL as a DBMS. Media files are hosted on Cloudinary

HOSTING: AWS

EMAILS: The app sends automatically emails via MailJet upon given events like user registration, new comment to a post, petition's goal reach.

SECURITY: The project uses environment variables to hide sensitive information. Custom, extra security features are implemented to prevent unauthorized access to other users' data, others publications editing and deleting.

FRONTEND: The project uses HTML5, CSS3, Bootstrap5, Popper, JS

MAIN THIRD PARTIES:

    'bootstrap5',
    'django_bootstrap5',
    'cloudinary',
    'rest_framework',


DISCLAIMER: This Application has no commercial purposes, it's not intended for commercial use and has features, which had not been fully tested.

*EMOTIONAL VALUES: This Project has been developed in Memoriam of my beloved pet Riva. Her pictures appear on the main landing page.