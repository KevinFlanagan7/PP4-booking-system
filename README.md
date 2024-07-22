![Logo](/documentation/readme-logo.jpg)

# Golf Academy

## Project Goals

The goal of this project is to enable registered users to book golf lessons with a PGA qualified professional at a Golf Academy. Once the user has registered an account they will be able to create, read, update and delete their booking at a state of the art driving range. The administrator of the booking site with also have full CRUD capibilities of the booking site.

## Table of Contents

- [Golf Academy](#golf-academy)
- [Project Goals](#project-goals)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Stories](#user-stories)
- [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
        - [User Model](#user-model)
        - [Booking Model](#booking-model)
    - [Agile Methodology](#agile-methodology)
        - [Overview](#overview)
        - [Epics & Milestones](#epics--milestones)
        - [Github Project](#github-project)  
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Home](#home)
        - [Sign Up](#sign-up)
        - [Sign In](#sign-in)
        - [My Bookings](#my-bookings)
        - [Create](#sign-in)
        - [Delete Modal](#delete-modal)
        - [Update](#update)
        - [Sign Out](#sign-out)
        - [Messages](#messages)
        - [Email Confirmation](#email-confirmation)
    - [Features to be implemented](#features-to-be-implemented)
- [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Fameworks](#frameworks)
    - [Database](#database)
    - [Tools](#tools)
- [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Lighthouse](#lighthouse)
    - [Features Testing](#features-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Responsiveness](#responsiveness)
    - [Browser Compatibility](#browser-compatibility)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Run Locally](#run-locally)
- [Credits](#credits)
- [Comments](#comments)

## UX

## User Stories

-  As a user, I want to be able to easily navigate through the website on all devices.

- As a user, I want to easily access information to learn about the golf academy and its offerings.

- As a user, I want to find the location on a map so I can easily plan my visit.

- As a user, I want to easily register an account with the golf academy.

- As a user, I want to sign into my account to create, read, update and delete bookings.

- As a user, I want clear notification messages when I complete an action successfully.

- As a user, I want to clearly know when I'm signed into and out of my account.

- As a user, I want to receive email confirmation when I make or update a booking.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Design

### Colours 

![Coolors](/documentation/coolors.png)

I used the colours above provided by the bootstrap classes listed below:

- Black: bg-dark, used in navigation bar and footer for good text contrast.
- Green: bg-success, used for messages to indicate successful actions like updating a booking etc.
- Red: btn-danger, used for delete and sign out to highlight a warning.
- Orange: btn.warning, used for update button which indicates a warning to the user that data can be changed. 
- White: bg-light, used for background for body of website for good text contrast.
- Blue: btn-primary, highlights primary actions like sign in, create and submit.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Fonts

I have used the default font families provided by Bootstrap for different devices and browsers. This ensures optimal readability and a consistent look. Below is a list of the default fonts depending on the device and browser used: 

font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";

### Icons

I have used the [Font Awesome library](https://fontawesome.com/ "Font Awesome") for the social media icons in the footer and a [Favicon generator](https://favicon.io/favicon-converter/ "Favicon") for the browser tab icon.


### Structure

I have built the website with a mobile first mindset using the Galaxy S5 (360px) as the smallest screen size for styling to look good on. The screen size breakpoints that I will be using are from [Bootstrap breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/).

| Screen Size | Breakpoint |
| ----------- | ---------- |
| x-small     | <576px     |
| small       | => 576px   |
| medium      | => 768px   |
| large       | => 992px   |
| x-large     | => 1200px  |

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Wireframes

- I used [Balsamic](https://balsamiq.com/wireframes/) to develop my wireframes. The pages include the home page, Sign up, Sign in, Create and the My Bookings pages.
The wireframes are below:

    - **Mobile Wireframes**

        <details><summary>Mobile Screenshots</summary>

        **Home Page**

        ![Home](/documentation/mobile-home.png)

        **Sign up page**


        ![Sign up](/documentation/mobile-signup.png)

        **Sign in page**

        ![Sign in](/documentation/mobile-signin.png)

        **Create booking page**

        ![Create](/documentation/mobile-create.png)

        **Bookings page**

        ![Bookings](/documentation/mobile-bookings.png)

    - **Tablet Wireframes**

        <details><summary>Tablet Screenshots</summary>

        **Home Page**

        ![Home](/documentation/tablet-home.png)

        **Sign up page**

        ![Sign up](/documentation/tablet-signup.png)

        **Sign in page**

        ![Sign in](/documentation/tablet-signin.png)

        **Create booking page**

        ![Create](/documentation/tablet-create.png)

        **Bookings page**

        ![Bookings](/documentation/tablet-bookings.png)

    - **Desktop Wireframes**

        <details><summary>Desktop Screenshots</summary>

        **Home Page**

        ![Home](/documentation/desktop-home.png)

        **Sign up page**

        ![Sign up](/documentation/desktop-signup.png)

        **Sign in page**

        ![Sign in](/documentation/desktop-signin.png)

        **Create booking page**

        ![Create](/documentation/desktop-create.png)

        **Bookings page**

        ![Bookings](/documentation/desktop-bookings.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Database Schema

![Database schema](/documentation/database.png)

#### User Model

- The built in Django user model above includes the below key fields:
    - id: Integer, primary key. A unique identifier for each user.
    - username: Varchar. The username chosen by the user (optional, configurable).
    - email: Varchar, unique. The user's email address, which must be unique.
    - password: Varchar. The user's password, stored in a hashed format. 
    - Django Allauth extends this model to handle user registration and authentication.

#### Booking Model

- The booking model stores the details of the booking and includes the fields below:
    - id: Integer, primary key. A unique identifier for each booking.
    - user_id: Integer, foreign key references the ID of the user who made the booking.
    - date: The date of the booking.
    - time: The time of the booking.
    - created_on: The timestamp when the booking was created.

The relationship between the user and bookings is one-to-many. Each user can have multiple bookings, with the user_id in the booking table referencing the id in the user table.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
    
### Agile Methodology

#### Overview

I used Agile methodology to plan my project. It allowed me to break down the project into smaller manageable clear tasks. It made it easier to prioritize tasks, to track progress and to maintain momentum during development. 

#### Epics & Milestones

My project is made up of several Epics which are large bodies of work that can be broken down into smaller, more manageable tasks. They provide an overview of the main functionalities to deliver, there are six milestones associated to the projects Epics. For my project, the Milestones with associated Epics, stories and tasks can be viewed at the links below:

- [Milestone 1 - Initial Set Up](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/1)

- [Milestone 2 - Home page creation](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/2)

- [Milestone 3 - Registered user CRUD functionality for Bookings](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/3)

- [Milestone 4 - Implement and Enhance Website Styling](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/4)

- [Milestone 5 - Email confirmation](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/5)

- [Milestone 6 - README Documentation](https://github.com/KevinFlanagan7/PP4-booking-system/milestone/6)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

#### Github Project

The Github projects tool was used to implement Agile development practices efficiently. By using Kanban boards, tasks were visually managed and tracked through various stages of completion. The MoSCoW (Must have, Should have, Could have & Won't have) method was used to prioritize features and tasks, view below links to the project's Kanban board and MoSCoW prioritization method:

- [Kanban board](https://github.com/users/KevinFlanagan7/projects/5/views/1)

- [MoSCoW Prioritization](https://github.com/KevinFlanagan7/PP4-booking-system/issues?q=is%3Aissue+is%3Aclosed)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features

## Existing Features

### Home

For the home page I used [Bootstrap's carousel](https://getbootstrap.com/docs/4.6/examples/carousel/) example template and added some customized html and css code. It includes three sectioms, the navigation bar, the main landing page and the footer section, details below:

<details><summary>Navigation Bar</summary>

<br>

The navigation bar is part of the base.html template and is displayed on all pages. It consists of the GolfAcademy name and logo which both link back to the home page. The option for unregistered users are Home, Sign up and Sign in. When registered and signed in the options are Home, My Bookings, a message to say who is signed in and the sign out option:

- Navagation bar for screensize > 768px.

    ![Nav](/documentation/nav-bar.png)

- Navagation bar for screensize > 768px when signed in.

    ![Nav](/documentation/nav-bar-signed-in.png)

- Navagation bar for screensize < 768px.

    For smaller screen sizes the nav menu collapses:

    ![Nav-mobile](/documentation/nav-bar-mobile.png)

- Navagation bar for screensize < 768px when signed in.

    ![Nav-mobile-signed-in](/documentation/nav-bar-mobile-signed-in.png)

</details>

<br>

<details><summary>Landing Page</summary>

<br>

The landing page consists of three carousel images each with a call to action button, the first is the link to the sign in page, the second links to the section of home page with information regarding the lessons and the third links the user to the location information of the GolfAcademy:

- First Carousel image

    ![First](/documentation/landing.png)

- Second Carousel image

    ![Second](/documentation/landing-2.png)

- Third Carousel image

    ![Third](/documentation/landing-3.png)

- Golf Lesson link

    ![Lesson](/documentation/lesson-info.png)

- Location link

    ![Location](/documentation/location-link.png)

</details>

<br>

<details><summary>Footer</summary>

<br>

The footer contains two logos which also double as a link back to the home page, one either side of the social media icon links. Like the nav bar the footer is part of the base.html template and is displayed across all pages. The social media links are only to the home pages of the platforms for educational purposes:

- Footer

    ![Footer](/documentation/footer.png)

</details>

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Sign Up 

The Sign up page includes a form for entering the users email address, username, password and a sign up button once details have been entered. At the top of the page it gives the option to be redirected to the sign in page if the user has already signed up.

<details><summary>Sign Up</summary>

<br>

- Sign Up

    ![Sign up](/documentation/sign-up.png)

</details>

### Sign In 

The Sign in page includes a form for entering the users username, password and a sign in button once details have been entered. At the top of the page it gives the option to be redirected to the sign up page if the user has not already signed up.

<details><summary>Sign In</summary>

<br>

- Sign In

    ![Sign in](/documentation/sign-in.png)

</details>

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### My Bookings 

When you sign up or sign in you are directed to the My Booking page, the nav bar menu changes to Home, My Bookings, logged in user message and the option to sign out. In this page the user can view the list of future bookings and has the ability to create, delete and update bookings.

<details><summary>My Bookings</summary>

<br>

- My Bookings

    ![My Bookings](/documentation/my-bookings.png)

</details>

### Create Booking 

When the signed in user clicks on create new booking button they are directed to a form to select a date, time slot and a button to submit booking. The lessons are only available Monday to Friday between 9am and 5pm, if Saturday or Sunday is selected a message is displayed that you can only book from Monday to Friday.

If a date in the past is select a message will be displayed that you can not book a date in the past. If the user selects a date and time that is not available a message will be displayed to say date and time slot has already been booked:

<details><summary>Create new booking</summary>

<br>

- Create new booking

    ![Create new booking](/documentation/create-new.png)

- Weekend day selected

    ![Weekend](/documentation/weekend-booking.png)

- Date in the past selected

    ![Past](/documentation/past-booking.png)

- Date and time slot already booked

    ![Booked](/documentation/booking-gone.png)

</details>

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Delete Modal 

When the user selects the delete button for a booking the delete modal is displayed warning the user that the booking will be permanently deleted with the option to continue with deletion or to close the modal.

<details><summary>Delete Modal</summary>

<br>

- Delete modal

    ![Delete modal](/documentation/delete-modal.png)

</details>

### Update 

When the signed in user clicks on the update booking button they are directed to a form to select a date, time slot and a button to update booking. Like with the create booking page the lessons are only available Monday to Friday between 9am and 5pm, the user can not select date in the past and will also get a message if updated date and time slot has already been booked:

<details><summary>Update booking</summary>

<br>

- Update booking

    ![Update booking](/documentation/update-booking.png)

- Update with Weekend day selected

    ![Update Weekend](/documentation/weekend-update.png)

- Update with Date in the past selected

    ![Update Past](/documentation/past-update.png)

- Update with Date and time slot already booked

    ![Update Booked](/documentation/update-gone.png)

</details>

### Sign Out 

When the red sign out button is selected the user is directed to the sign out page with a message asking user if they are sure they want to sign out. Once sign out is selected the user is directed back to the home page, the sign out button and signed in message is no longer displayed:

<details><summary>Sign Out</summary>

<br>

- Sign out

    ![Sign out](/documentation/sign-out.png)

</details>

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Messages

When a user has successfully signed up and signed in a message is displayed with the users username to say that they have signed in. There are also messages displyed to inform the user when they have succesfully created, deleted and updated a booking and when they have signed out:

<details><summary>Messages</summary>

<br>

- Sign up and Sign in

    ![Sign out/in](/documentation/sign-in-message.png)

- Create message

    ![Create](/documentation/booking-message.png)

- Delete message

    ![Delete](/documentation/delete-message.png)

- Update message

    ![Update](/documentation/update-message.png)

- Sign out message

    ![Sign out](/documentation/sign-out-message.png)

</details>


### Email Confirmation

When a user creates or updates a booking, along with the successful message an email confirmation is also sent to the email address that the user provided when signing up, an email account of golflessons2024@gmail.com was set up to send the confirmation emails:

<details><summary>Email confirmation</summary>

<br>

- Booking email confirmation

    ![Email booking](/documentation/email-confirmation.png)

- Update booking email confirmation

    ![Email update](/documentation/email-update.png)

</details>

## Features to be Implemented

Below are a list of features to be implemented in the future:

- Email verification on sign up
- Option to sign in with social media or google credentials
- Password reset functionality 
- A comments feedback section about the golf lessons.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML "HTML") 
- [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Frameworks

- [Django](https://en.wikipedia.org/wiki/Django_(web_framework) "Django")
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework) "Bootstrap")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Database

- [PostgreSQL](https://www.postgresql.org/) from [ElephantSQL](https://www.elephantsql.com/).

### Tools

- [Python Validator](https://pep8ci.herokuapp.com/)
- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")
- [JShint Validation Service](https://jshint.com/ "JSHint")
- [Heroku](https://dashboard.heroku.com/apps)
- [Balsamic](https://balsamiq.com/wireframes/ "Balsamic")
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview "Lighthouse")
- [Coolers](https://coolors.co/ "Coolers")
- [Am I Responsive](https://ui.dev/amiresponsive "Am I Responsive")
- [Favicon Converter](https://favicon.io/favicon-converter/ "Favicon Converter")
- [Font Awesome library](https://fontawesome.com/ "Font Awesome")
- [dbdiagram](https://dbdiagram.io/home/ "dbdiagram")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Testing

### Code Validation

<details><summary>HTML files</summary>

- Home page

    ![Home](/documentation/code-home.png)

- Sign up page

    ![Sign Up](/documentation/code-signup.png)

- Sign in page

    ![Sign In](/documentation/code-signin.png)

- My Bookings page

    ![My Bookings](/documentation/code-mybookings.png)

- Create Bookings page

    ![Create](/documentation/code-create.png)

- Update Booking page

    ![Update](/documentation/code-update.png)

- Sign Out page

    ![Sign Out](/documentation/code-signout.png)

</details>

<br>

<details><summary>CSS file</summary>

- style.css file

    ![CSS](/documentation/code-css.png)

</details>

<br>

<details><summary>JavaScript file</summary>

- script.js

    ![JS](/documentation/code-js.png)

</details>

<br>

<details><summary>Python files</summary>

- model.py

    ![Model](/documentation/code-model.png)

- views.py

    ![Views](/documentation/code-views.png)

- forms.py

    ![Forms](/documentation/code-forms.png)

- urls.py

    ![Urls](/documentation/code-urls.png)

- admin.py

    ![Admin](/documentation/code-admin.png)

- settings.py

    ![Settings](/documentation/code-settings.png)

</details>
   
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Lighthouse

Lighthouse tests were run on all pages for mobile and desktop, see results below:

<details><summary>Home page</summary>

<br>

- Home page desktop

    ![Home Desktop](/documentation/lighthouse-home-desktop.png)

- Home page mobile

    ![Home mobile](/documentation/lighthouse-home-mobile.png)

</details>

<br>

<details><summary>Sign up page</summary>

<br>

- Sign up page desktop

    ![Sign up Desktop](/documentation/lighthouse-signup-desktop.png)

- Sign up page mobile

    ![Sign up mobile](/documentation/lighthouse-signup-mobile.png)

</details>

<br>

<details><summary>Sign in page</summary>

<br>

- Sign in page desktop

    ![Sign in Desktop](/documentation/lighthouse-signin-desktop.png)

- Sign in page mobile

    ![Sign in mobile](/documentation/lighthouse-signin-mobile.png)

</details>

<br>

<details><summary>My Bookings page</summary>

<br>

- My Bookings page desktop

    ![Bookings Desktop](/documentation/lighthouse-mybookings-desktop.png)

- My Bookings page mobile

    ![Bookings mobile](/documentation/lighthouse-mybookings-mobile.png)

</details>

<br>

<details><summary>Create Bookings page</summary>

<br>

- Create Bookings page desktop

    ![Create Desktop](/documentation/lighthouse-create-desktop.png)

- Create Bookings page mobile

    ![Create mobile](/documentation/lighthouse-create-mobile.png)

</details>

<br>

<details><summary>Update Bookings page</summary>

<br>

- Update Bookings page desktop

    ![Update Desktop](/documentation/lighthouse-update-desktop.png)

- Update Bookings page mobile

    ![Update mobile](/documentation/lighthouse-update-mobile.png)

</details>

<br>

<details><summary>Sign out page</summary>

<br>

- Sign out page desktop

    ![Sign out Desktop](/documentation/lighthouse-signout-desktop.png)

- Sign out page mobile

    ![Sign out mobile](/documentation/lighthouse-signout-mobile.png)

</details>

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Features Testing

- Home Page 

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Nav bar GolfAcademy name|Click on name|Returns user to home page if not already there|:white_check_mark:|
    |Nav bar Logo|Click on Logo|Returns user to home page if not already there|:white_check_mark:|
    |Nav bar Home|Click on Home link|Returns user to home page if not already there|:white_check_mark:|
    |Nav bar Sign up|Click on Sign up link|Directs user to Sign up page|:white_check_mark:|
    |Nav bar Sign in|Click on Sign in button|Directs user to Sign in page|:white_check_mark:|
    |Carousel Sign in|Click on carousel sign in button|Directs user to Sign in page|:white_check_mark:|
    |Carousel Golf Lessons|Click on carousel Golf Lessons button|Directs user to golf lessons info section on home page|:white_check_mark:|
    |Carousel Location button|Click on carousel Location buttom|Directs user to Location info section on home page|:white_check_mark:|
    |Footer logos|Click on footer logos|Returns user to home page if not already there|:white_check_mark:|
    |Footer Social media icons|Click on icons|Directs user to social media home pages on new tab|:white_check_mark:|

- Sign Up page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Sign in link|Click on Sign in link at top of page if you already have an account|Directs user to Sign in page|:white_check_mark:|
    |Email field|Enter invalid email format or leave empty and click Sign up |Messages display to enter valid email and fill out field|:white_check_mark:|
    |Username field|Leave empty and click Sign up|Message displays to fill out field|:white_check_mark:|
    |Password field|Leave empty or invalid lenght and characters|Messages display to fill out field with correct characters|:white_check_mark:|
    |Password confirmation field|Leave empty or enter incorrectly|Messages to fill in filed and to enter same password displayed|:white_check_mark:|
    |Sign Up button|Enter valid data and click button|User directed to My bookings page with a successfully signed in message with users username displayed|:white_check_mark:|

- Sign In page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Sign up link|Click on Sign up link at top of page if user has not Signed up yet|Directs user to Sign up page|:white_check_mark:|
    |Username field|Leave empty or enter invalid username and click Sign in|Messages display to fill out field or username and or password is not correct|:white_check_mark:|
    |Password field|Leave empty or enter invalid password and click Sign in|Messages display to fill out field or username and or password is not correct|:white_check_mark:|
    |Sign In button|Enter valid data and click button|User directed to My bookings page with a successfully signed in message with users username displayed|:white_check_mark:|

- My Bookings Page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |My Bookings link in nav bar|Click on link|User directed to my booking page if not already there|:white_check_mark:|
    |Sign Out button|Click on button|User directed to Sign out page|:white_check_mark:|
    |Create a new booking button|Click on button|User directed to Create new booking page|:white_check_mark:|

- Create new booking page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Select Date field|Click on calendar icon on larger screens and anywhere in field for smaller screen sizes|Date picker calendar displays with current date highlighted|:white_check_mark:|
    |Date in past message|Select date in past and click submit|Message displays that you can not book date in past|:white_check_mark:|
    |Weekend day message|Select a weekend day and click submit|Message displays that you can only book date from Monday to Friday|:white_check_mark:|
    |Slot already booked message|Select same date and time as another booking|Message displays that this date and time slot has already been booked|:white_check_mark:|
    |Select time field|Click dropdown arrow or anywhere in field|List of 1 hour time slots from 9am-5pm excluding 1-2 for lunch are displayed to select|:white_check_mark:|
    |Submit button|Select valid date and time that has not already been booked and click Submit button|User directed back to my booking page with a booking created successfully message displayed confirmation email was sent, bookings created listed on page|:white_check_mark:|

- Delete modal

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Delete button|Click on delete button beside a booking|Delete booking modal displays asking user if they are sure they want to permanently delete booking|:white_check_mark:|
    |Delete modal close button|Click on delete modal close button|User returned to My bookings page and booking is not deleted|:white_check_mark:|
    |Delete modal delete button|Click on delete modal delete button|User returned to My booking page with message that booking has been deleted successfully, booking no longer listed on page |:white_check_mark:|

- Update page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Update button|Click on update button beside a booking|User directed to update booking page:white_check_mark:|
    |Select Date field|Click on calendar icon on larger screens and anywhere in field for smaller screen sizes|Date picker calendar displays with current date highlighted|:white_check_mark:|
    |Date in past message|Select date in past and click update|Message displays that you can not book date in past|:white_check_mark:|
    |Weekend day message|Select a weekend day and click update|Message displays that you can only book date from Monday to Friday|:white_check_mark:|
    |Slot already booked message|Select same date and time as another booking and click update|Message displays that this date and time slot has already been booked|:white_check_mark:|
    |Select time field|Click dropdown arrow or anywhere in field|List of 1 hour time slots from 9am-5pm excluding 1-2 for lunch are displayed to select|:white_check_mark:|
    |Update button|Select valid date and time that has not already been booked and click Update button|User directed back to my booking page, booking updated successfully message displayed and confirmation email was sent, updated booking listed on page|:white_check_mark:|

- Sign Out page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Sign out button|Click on button under message asking user if they are sure they want to Sign out|User directed back to home page with a confirmation message that they have signed out|:white_check_mark:|

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
        
### User Stories Testing

- Table of User Story Testing.

    |User Story|Testing|Result|
    |---|---|---|
    |As a user, I want to be able to easily navigate through the website on all devices.| Navigation bar displays clear menu options which are intuitive and collapse down to a drop down menu on smaller screen sizes.|:white_check_mark:|
    |As a user, I want to easily access information to learn about the golf academy and its offerings.| The home page provides all the information about the Golf Academy regarding lessons, duration, price and facilities.|:white_check_mark:|
    |As a user, As a user, I want to find the location on a map so I can easily plan my visit.| The home page provides provide a map of the location and the eircode of the Golf Academy.|:white_check_mark:|
    |As a user, I want to easily register an account with the golf academy.| The nav bar on the home page provides a link to the Sign up page, when the user enters a valid email, username and password they are signed into their bookings page.|:white_check_mark:|
    |As a user, I want to sign into my account to create, read, update and delete bookings.| The nav bar on the home page provides a link to the Sign in page, there is also a Sign in button on the first carousel image, when the user enters a valid username and password they are signed into their my bookings page where they can easily create, read, update and delete bookings.|:white_check_mark:|
    |As a user, I want clear notification messages when I complete an action successfully.|When a user successfully signs up, signs in, creates, updates, deletes and signs out there is a green success message displayed.|:white_check_mark:|
    |As a user, I want to clearly know when I'm signed into and out of my account.|When the user is signed into their account there is a message displayed at the right hand side of the nav bar that the username is signed in and the option to sign out in red beside it. The message and sign out option are not displayed if the user is not signed in.|:white_check_mark:|
    |As a user, I want to receive email confirmation when I make or update a booking.| When the user creates or updates a booking a green success message along with a email confirmation sent message is displayed, the new or updated booking details are emailed to the email address that the user resistered when they signed up.|:white_check_mark:|
    
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Responsiveness

- Using Chrome Mobile [Simulator](https://developer.chrome.com/docs/devtools/device-mode "Simulator") extension I have tested the website's responsiveness on different devices. Test results and screenshots below:

    | Device                | Responsive >=768px | Responsive <768px | Landing page Images |
    | --------------------- | ------------------ | ----------------- | ----------- | 
    | Galaxy S5             | N/A                | Good              | Good        |
    | iPhone 6/7/8          | N/A                | Good              | Good        |
    | iPad Pro              | Good               | N/A               | Good        |
    | Desktop 1024px        | Good               | N/A               | Good        |
    | Desktop > 1200px      | Good               | N/A               | Good        |

    <details><summary>Responsiveness Screenshots</summary>

    <br>

    **Mobile**

    | Home Page | Sign in Page | Bookings Page |
    | ---- | ----- | ------ |
    | ![Home](/documentation/resp-mobile-home.png) | ![Sign](/documentation/resp-mobile-signin.png) | ![Bookings](/documentation/resp-mobile-bookings.png) |

    **Tablet**

    | Home Page | Sign in Page | Bookings Page |
    | ---- | ----- | ------ |
    | ![Home](/documentation/ipad-home.png) | ![Sign](/documentation/ipad-signin.png) | ![Bookings](/documentation/ipad-bookings.png) |

    **Desktop**

    | Home Page | Sign in Page | Bookings Page |
    | ---- | ----- | ------ |
    | ![Home](/documentation/resp-desktop-home.png) | ![Sign](/documentation/resp-desktop-signin.png) | ![Bookings](/documentation/resp-desktop-bookings.png) |  

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Browser Compatibility

- Table of Browsers tested:

  | Browser | Intented Appearance | Intented Responsiveness | 
    | --------| ------------------- | ----------------------- |
    | Chrome  | Good | Good | 
    | Edge    | Good | Good | 
    | Firefox | Good | Good |

    <details><summary>Browser compatibility Screenshots</summary>

    <br>

    *Chrome*

    ![Chrome](/documentation/chrome.png) 

    *Edge*

    ![Edge](/documentation/edge.png)

    *Firefox*

    ![Firefox](/documentation/firefox.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Bugs

- Thankfully I didn't encounter any major bugs during development just small issues like pages not rendering correctly an deployed site and locally. This was caused by not running the collect static files command before deployment and by not changing the debug level back to True when working locally.

- The other issues encountered was with Lighthouse testing, the performane and best pratices scores were low. I improved the performance by converting all images to webp format. The best practice score was low due to originally using a google iframe for the map location. I chaged this to the google maps api when improved the score.

### Unfixed Bugs

- There are no bugs with the game that I am aware of.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Deployment

### Heroku

The site was deployed using Heroku following the steps below:

- Create a list of requirements using the following command in the terminal (`pip3 freeze > requirements.txt`).

- Heroku searches for this exact file name as it builds the project. This file contains the list of the packages installed during project development which are called dependencies. We need Heroku to install these dependecies as well in order for the project to run. 

- A **Procfile** is required to allow Heroku deployment to be properly configured to a gunicorn web app.

- In settings.py file configure the ALLOWED_HOSTS list with **heroku.com**.

- All environment variables in the env.py which gitignored on the repo must be configured correctly with the database details and secret keys.

- Activate your Heroku Student Pack account at the following link: [Heroku for Students]( https://www.heroku.com/github-students).

- From Heroku Dashboard click on **Create New App**, enter name of app, choose your region and then click **Create App**.

- Click on the **Settings** tab of the newly created app.

- Go to **Config Vars** section and enter the required hidden variables like database details and secret keys.

- Click on **Deploy** tab at top of screen.

- In **Deployment method** section selct **GitHub** and confirm by clicking **Connect to GitHub**.

- Serach for your GitHub repository name, once found click **Connect**.

- Scroll down on page and select either **Enable Automatic Deploys** which will rebuild your app every time you push a new change to GitHub or **Deploy Branch** which is a manual deployment so has to be selected after each change pushed to GitHub.

- Once app is built you can click on **Open app** at top of page which will open app on new page where you can copy URL. 

### Fork

To make a copy of a repository or to fork it using Github follow below steps:

- Go to **Github repository** to be copied.
- Click on the **Fork** button in upper right corner of page to copy.

### Clone

To copy the repository to your local machine in Github follow steps below:

- Go to **Github repository** to be cloned.
- Click on the **Code** button above the list of files.
- Select to clone using either  **HTTPS**, **SSH**, or **Github CLI** and click the **copy** button to copy the URL to clipboard.
- Open **Git Bash**.
- Change the current working directory to the one where you want the cloned directory.
- Type **git clone** and paste the URL from the clipboard. 
- Press **Enter** to create your local clone.

### Run Locally

- Go to the **GitHub repository**.
- Locate the green **Code** button above the list of files and click it.
- From the dropdown menu select **download Zip**.
- **Download** and open the zip file to run in an editor.
- Create an **env.py** file and input the environment variables
- Ensure **PostgreSQL** is installed on your computer and ports are open
- Create a virtual environment for installing the **python modules** in the pip file.
- Run python **makemigrations, migrate and runserver**.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Credits

For help and advice:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

Code inspiration:

- [LMS Django Walkthrough Project](https://codeinstitute.net "Developing with Django")


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;