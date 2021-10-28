## Index
[**1. Functionality**](#1-functionality)  
[**2. Validators**](#2-validators)  
[**3. Compatibility**](#3-compatibility) 
[**4. Performance**](#4-performance) 
[**5. User stories**](#5-user-stories) 
[**6. Bugs**](#6-bugs) 

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








# 6. Bugs
-   When clicking on nav logo the user is redirected to *Walks* page
    - Bug has been fixed by changing the url.