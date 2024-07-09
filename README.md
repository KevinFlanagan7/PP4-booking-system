![Logo](/static/images/logo.jpg)

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
        - [Epics](#epics)
        - [MoSCoW](#moscow)  
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Tools & Libraries](#tools--libraries)
- [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Features Testing](#features-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Fork](#fork)
    - [Clone](#clone)
- [Credits](#credits)
- [Comments](#comments)

## UX

## User Stories


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

I have used the [Font Awesome library](https://fontawesome.com/ "Font Awesome") for the social media icons in the footer and a [Favicon generator](https://favicon.io/ "Favicon") for the browser tab icon.


### Structure

I have built the website with a mobile first mindset using the iphone 6 (375px) as the smallest screen size for styling to look good on. The screen size breakpoints that I will be using are from [Bootstrap breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/).

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
    - user_id: Integer, foreign key references User(id). The ID of the user who made the booking.
    - date: The date of the booking.
    - time: The time of the booking.
    - created_on: The timestamp when the booking was created.

The relationship between user and booking is one-to-many. Each user can have multiple bookings, with the user_id in the booking table referencing the id in the user table.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
    

### Agile Methodology


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features

## Existing Features

### Home Page



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


  


## Features to be Implemented



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML") Included in CI Template.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS") Included in CI Template.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Tools & Libraries

* [Colorama](https://pypi.org/project/colorama/)
* [Python Validator](https://pep8ci.herokuapp.com/)
* [Heroku](https://dashboard.heroku.com/apps)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Testing

### Code Validation

    
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Features Testing

- Home Page 

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    

    


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

        
### User Stories Testing

- Table of User Story Testing.

    | User Story | Testing |
    | :--- | :--- | 
    |As a user, ||
    
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Browser Compatibility

- Table of Browsers tested, as the project is terminal based mobile device testing was not applicable.

  | Browser | Intented Appearance | Intented Responsiveness | 
    | --------| ------------------- | ----------------------- |
    | Chrome  |  |  | 
    | Edge    |  |  | 
    | Firefox |  |  |

    <details><summary>Browser compatibility Screenshots</summary>

    *Chrome*

    ![Chrome]() 

    *Edge*

    ![Edge]()

    *Firefox*

    ![Firefox]()

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Bugs


### Unfixed Bugs



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Deployment

### Heroku

The site was deployed using Heroku following the steps below:

- Create a list of requirements using the following command in the terminal (pip3 freeze > requirements.txt).

- Heroku searches for this exact file name as it builds the project. This file contains the list of the packages installed during project development which are called dependencies. We need Heroku to install these dependecies as well in order for the project to run. 

- Activate your Heroku Student Pack account at the following link: [Heroku for Students]( https://www.heroku.com/github-students).

- From Heroku Dashboard click on **Create New App**, enter name of app, choose your region and then click **Create App**.

- Click on the **Settings** tab of the newly created app.

- Go to **Config Vars** section and in the field for KEY enter **PORT**, in the VALUE field enter **8000** and then click **ADD**.

- If your project uses a **creds.json** file you will need to set a config var by adding **CREDS** to KEY field and copying contents of creds.json file into **VALUE** field.

- Go to Buildpacks section and click on **Add buildpack**.

- Select **python** and click on **Save changes**.

- Click on **Add buildpack** again, select **nodejs** and click on **Save changes**.

- Make sure buildpacks are in order with python on top and nodejs underneath.

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