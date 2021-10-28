# Kids Love Walking


**[Live demo](https://kids-love-walking.herokuapp.com/get_walks)**

---
## Index
[**1. Overview**](#1-overview)  
[**2. UX**](#2-ux)  
- [2.1 User Stories](#21-user-stories)  
- [2.2 Wireframes](#22-design) 
- [2.3 Design](#23-design) 

[**3. Features**](#3-features) 
- [3.1 Existing features](#31-existing-features)  
- [3.2 Features to add](#32-features-to-add)  

[**4. Technologies used**](#4-technologies-used)  
[**5. Testing**](#5-testing)  
[**6. Deployment**](#6-deployment)  
[**7. Credits**](#7-credits)  


# 1. Overview   
The aim of this application is to offer parents a source of inspiration and help them choose an appropriate walk for the whole family, considering the little feet especially. Furthermore, the app is encouraging parents to share their own favourite walks so that others could enjoy them too.
# 2. UX  
From a user's point of view the application should be intuitive and easy to use whilst presenting the information in a manner that would make the visitor come back in the future.  
## 2.1 User Stories  
**First time visitor**  
&rarr; User is able to find relevant information about walks  
&rarr; User can filter information using a search field  
&rarr; User can register easily    
**Returning visitor**  
&rarr; User can see last added walks  
&rarr; User can log in/log-out  
&rarr; User can add their favourite walks  
&rarr; User can see their contribution in Profile section  
&rarr; User can edit/delete their contribution  
**Site owner**  
&rarr; Admin can add/remove categories  

## 2.2 Wireframes
Wireframes were created for every page, considering mobile, tablet and desktop views. Full size wireframes can be checked **[here](wireframes)**.
## 2.3 Design
The project uses Materialize framework and it's grid system that allows the project to be responsive across different devices.  
### Colour scheme
For simplicity the project uses Materialize's colour scheme, the following being chosen:
- ![#388e3c](https://via.placeholder.com/15/388e3c/000000?text=+) #388e3c (green darken-2)
- ![#e8f5e9](https://via.placeholder.com/15/e8f5e9/000000?text=+) #e8f5e9 (green lighten-5)
- ![#ff8f00](https://via.placeholder.com/15/ff8f00/000000?text=+) #ff8f00 (amber darken-3)  


 For Header, Footer and call to action buttons the colour being used is green darken-2, to represent the green found on walks most of the year. Also green lighten-5, a pale shade of green, is used as background for flashed messages and cards.   
For Cancel/Delete buttons the colour chosen was amber darken-3, the colour of leaves in autumn, to represent a warning about the action to be made.

### Font
The font used is trying to suggest that the walks have a personal touch, being hand-written by the user, hence the cursive Google font *Architects Daughter* was chosen.
## 3. Features
### 3.1 Existing features  
The app makes use of the following features:
### **Material design and its features:**
- Cards
- Forms
- Modal
- Sidenav
### **Register and Login**
- Werkzeug security was used to store user's hashed password.
### **CRUD functionality**
New visitors have access to the *walks* collection whilst registered users can:
- Add new walk
- Edit their own additions
- Delete their own additions.
The admin can also add/edit/delete categories in the collection.  
### **User profile**
Registered users get access to their own walks in the *Profile* page, making editing/deleting process easier.
### **Defensing Programming**
To prevent accidental deletion of walks, users are asked to confirm again before deleting, through a modal pop-up.
### 3.2 Features to add
- Comments for individual walks
- Option to add user profile picture
- Option to save favourite walks
## 4. Technologies used
### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
### Frameworks
- [Flask](https://palletsprojects.com/p/flask/)
- [jQuery](https://jquery.com/)
- [Materialize](https://materializecss.com/)
### Project management
- [Lucid](https://lucid.co/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/about)
- [MongoDB](https://www.mongodb.com/)

