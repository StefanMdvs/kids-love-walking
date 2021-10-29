## Index
[**1. Functionality**](#1-functionality)  
[**2. Validators**](#2-validators)    
[**3. Performance**](#3-performance)  
[**4. User stories**](#4-user-stories)  
[**5. Bugs**](#5-bugs)  

# 1. Functionality
- ### Navigation  
    - when logo "Kids Love Walking" is clicked the user is redirected to Home Page.
    - links in the navbar have been tested and are working
    - The hamburger menu expands when clicked   When clicked/tapped, it expands to reveal page links. These have been tested and are working as expected
    - Navigation links display according to user being logged in or not or being an admin
- ### Footer 
    - Footer is sticky so at the bottom of the page on all devices
    - Social links open in a new page and redirect user to their respective location
- ### Home Page
    - links on home page send user to Register or Log In, depending if user is in session or not
    - User can see the last 3 added walks or be redirected to *Walks* page to see more
- ### Walks Page
    - Users can search for a walk by walk name and/or description
    - When pressing *Reset*, page displays all walks again
    - If no walks matching searching criteria were found, a message displays letting the user know
- ### Register Page
    - User needs to fill in the Username and Password, both requiring a minimum/maximum amount of characters
- ### Log In Page
    - If no user matching the input was found in db or password doesn't match, the user get's a message displayed
- ### Log Out
    - When logging out the user is removed from the session cookie and user is being notified via a flash message
- ### Add walk/Edit walk
    - All fields are required except the image field. If image field is empty, a default image will be provided
    - *Category*, *Facilities* and *Age* field have dropdowns that are validated accordingly
    - When *Cancel* is clicked, the user is redirected to *Walks* page

- ### Redirect user
    - After user logs in/register, the page redirects to *Profile* page that displays user's walks
    - After logging out, user is redirected to *Log In* page
    - when adding a walk, if user wants to cancel, user is redirected to *Walks* page
    - After adding a walk user is being redirected to the same *Walks* page
    - When user wants to delete a picture and cancels the action, they are being redirected to the same walk
    - If user deletes the walk, they are being redirected to *Walks* page
- ### Summary cards
    - when clicked open up and give details about the walk
    - the Back button sends user to *Walks* page
- ### Detailed cards
    - when clicked show information about the walk, and if user is in session then the *Delete* and *Edit* buttons are displayed

# 2. Validators
The code was validated using [W3C](https://validator.w3.org/) services, [JSHint](https://jshint.com/) for JavaScript file and [PEP8](http://pep8online.com/) online for Python code.
- HTML validator returned several semantic errors that have been fixed
- CSS validator returned two errors, one related to Font Awesome stylesheet and the other related to Materialize
- JS returns no error
- Python code returns no error.

# 3. Performance
Automated testing was performed using Chrome Dev Tools - Lighthouse:  
**Mobile page**  
    - Performance: 88%  
    - Accessibility: 94%  
    - Best Practices: 80%  
    - SEO: 92%  

**Dektop Page**
    - Performance: 93%  
    - Accessibility: 94%  
    - Best Practices: 80%  
    - SEO: 90%  

**Browsers**
The app was tested on:
    - Google Chrome
    - Samsung Internet
    - Amazon Silk  
**Screen sizes**
Using Chrome Dev Tools the app had been tested for all profiles displayed, from Moto G4 to Nest Hub Max.  
The app had also been tested on:
- Samsung S6
- iPhone 6
- Amazon Fire 10
- Dell Laptop

# 4. User stories
**First time visitor**
>&rarr;User is able to find relevant information about walks
>
User is presented with a short selection of walks starting with the Home Page, furthermore clicking on a specific walk opens up a card with details about it, a picture, facilities and age suitability. Information is tructured in a way that it is relevant separating the fields and   being visual appealing due to the image being present.  

>&rarr; User can filter information using a search field
>
On entering a query in the search field, relevant walks containing the string are displayed.
>&rarr; User can register easily
>
User is guided to Register starting with home page and Register navigation link is visibly displayed and the register process requires only two fields, username and password.

**Returning visitor**
>&rarr; User can see last added walks
>
When landing on *Home* Page user can see the latest added walks as the last three are displayed here.

>&rarr; User can log in/log-out
>
Navigation tabs are visible and have been tested for functionality.

>&rarr; User can add their favourite walks
>
*New Walk* page allows user to share their favourite walk. User need to be registered and logged in to be able to do so. 

>&rarr; User can see their contribution in Profile section
>
If user had any walks added, these will be displayed also in *Profile* page.

>&rarr; User can edit/delete their contribution
>
User can see details about their own walks in *Profile* page and edit/delete if they wish to.

Site owner
>&rarr; Admin can add/remove categories
>
Admin can add/edit or remove Categories.

# 5. Bugs
-   When clicking on nav logo the user is redirected to *Walks* page
    - Bug has been fixed by changing the url.
- When editind a walk and clicking on *Submit* the walk will not update
    - Bug was fixed by replacing the anchor tag on "*edit_walk.html*" with a submit button.
