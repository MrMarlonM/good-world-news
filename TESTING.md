# Testing
## Manual Testing
### Iteration 1
#### User Story: [Breaking news for editor](https://github.com/MrMarlonM/good-world-news/issues/38)
- Acceptance Criteria:
    - Through a checkbox I can easily add or un-add articles as breaking news
    - The article shows prominently at the top of the page
- Manual Steps:
    - Log in as editor
    - Navigate to an article in the admin panel and click on edit
    - Check the box `is breaking news`
    - Safe the article
- Expected Outcome:
    - Now the article is presented as breaking news in the newsfeed
    - It has a banner breaking news at the top
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [User-friendly design](https://github.com/MrMarlonM/good-world-news/issues/23)
- Acceptance Criteria:
    - The design is responsive to different screen sizes
    - On every size the font is clearly readable
    - Images adjust their size accordingly
    - The elements position themselves according to the screen size
- Manual Steps:
    - Open the website in Google Chrome for Desktop
    - Right click on the site and click on inspect
    - Click on the Device Toolbar option in dev tools
    - Adjust the shown screen size from big to small
    - Look out for images and texts on all pages
- Expected Outcome:
    - The images, container and texts change their size and/or position according to the screen size.
    - Everything stays readable and is presented in a nice fashion
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Newsfeed on homepage](https://github.com/MrMarlonM/good-world-news/issues/24)
- Acceptance Criteria:
    - All articles are listed on the homepage
    - The articles are listed by date as default
    - The title, short description and image can be seen
    - When clicked on, the articles opens in full
- Manual Steps:
    - Go to the index.html page
    - Look for the published articles and compare it to the articles seen in the admin panel
    - See if all have a title, description and image
    - Click on the articles to see if they open
- Expected Outcome:
    - All published articles are shown
    - All articles have titles, short descriptions and images
    - All articles open in detail when clicked on
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Manage user accounts as admin](https://github.com/MrMarlonM/good-world-news/issues/14)
- Acceptance Criteria:
    - The administrator can view user accounts
    - The administrator can edit user accounts
    - The administrator can delete user accounts
- Manual Steps:
    - Log in to the admin panel as admin account
    - Click on section Users
    - Click on a specific user
    - Try to edit the user
    - Try to delete the user
- Expected Outcome:
    - All users are listed
    - The admin can edit user accounts
    - The admin can delete user accounts
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Create Articles as editor](https://github.com/MrMarlonM/good-world-news/issues/10)
- Acceptance Criteria:
    - It is possible to provide a styled text
    - It is possible to add a picture
    - It is possible to add a short description
- Manual Steps:
    - Log into the admin panel as editor
    - Click on `+Add` next to articles
    - Test if the text in the content section and excerpt section is customizable
    - Add a image
    - Safe article as published and check the website
- Expected Outcome:
    - The image shows with the uploaded image and the styled text
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Edit Articles as editor](https://github.com/MrMarlonM/good-world-news/issues/11)
- Acceptance Criteria:
    - All articles can be changed
    - The text, title and short description are changeable as well as the image
- Manual Steps:
    - Log in as editor
    - Click on articles and then on an existing article
    - CHange the title, text, excerpt and image
    - Safe the article as published
- Expected Outcome:
    - The article is now shown with all the changes
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Delete Articles as editor](https://github.com/MrMarlonM/good-world-news/issues/12)
- Acceptance Criteria:
    - It is possible to delete articles in the editor dashboard
    - After deletion the article is not visible anymore as well as all linked comments.
- Manual Steps:
    - Log in as editor
    - Go to the admin panel and click on Articles
    - Click on one article
    - Scroll down and click on delete in the bottom right corner
- Expected Outcome:
    - The article gets deleted and isn't shown anymore
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Login form for registered users](https://github.com/MrMarlonM/good-world-news/issues/6)
- Acceptance Criteria:
    - A log in form is provided where the user can log in with his user name and password
    - Once logged in the User can use all the provided functions.
    - The log in button is found in the menu
- Manual Steps:
    - Click on Login in the menu
    - Log in as user
    - Click on an article
    - Like/Unlike article
    - Comment article
    - Edit comment
    - Delete comment
    - Go back to newsfeed and like/unlike article
- Expected Outcome:
    - User can login and is redirected to newsfeed
    - Articles are likable and unlikable
    - Comment are writable, editable and deletable.
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Registration Form](https://github.com/MrMarlonM/good-world-news/issues/2)
- Acceptance Criteria:
    - A form is provided to fill in name, email and password for registration
    - After registration the user can directly log into the created account
- Manual Steps:
    - Make sure to be logged out
    - Click on Register in Menu
    - Fill in information and click on `Sign Up`
- Expected Outcome:
    - The account is created
    - The user is directly logged in
    - The user is redirected to index.
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Login form for editor](https://github.com/MrMarlonM/good-world-news/issues/8)
- Acceptance Criteria:
    - A login form is provided for editors
    - After logging in the editor can access the editor dashboard
- Manual Steps:
    - Click on login
    - Insert credentials of editor
    - Click on `Sign In`
- Expected Outcome:
    - The editor is redirected to the editor board
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Mobile-friendly navigation](https://github.com/MrMarlonM/good-world-news/issues/22)
- Acceptance Criteria:
    - The navigation bar is toggle-able so that it doesn't use to much real estate
    - The nav bar is easily findable at the top of the screen at all times
    - Buttons and links are clearly stated as such and distinct from other content
    - Buttons are big enough to be pressed on a touch screen
- Manual Steps:
    - Go to index.html on mobile device
    - Click in the right top corner on the Menu bars
    - Look if the menu is readable and the links are clickable
    - Go back to index.html and look if the buttons are big enough.
    - Go to contact page and see if the form and button is big enough and readable
    - Go to login and see if the form and button is big enough and readable
    - Go to register and see if the form and button is big enough and readable
    - Click on an article and scroll down to the comment section
    - See if the comment form is big enough
    - Post a comment and see if the buttons for edit and delete are big enough and readable
- Expected Outcome:
    - The menu opens when toggling the Menu bar in the corner
    - The buttons are all clickable and readable
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Contact Form](https://github.com/MrMarlonM/good-world-news/issues/27)
- Acceptance Criteria:
    - A feedback form is provided
    - The name, mail and message can be put in
    - The message is visible to the administrator
- Manual Steps:
    - Click on contact
    - See if the option to provide the name, email and message is provided
    - Fill out the form and press "Send message"
    - Login as admin
    - Click on messages and see if the message appears
- Expected Outcome:
    - The contact site exists
    - The fields are present
    - When submitting the form the message shows up in the admin panel
- Actual Outcome:
    - The expected outcome was fulfilled

### Iteration 2
#### User Story: [Website accessibility](https://github.com/MrMarlonM/good-world-news/issues/21)
- Acceptance Criteria:
    - Aria-labels are given for every link
    - Every image has alt-attributes
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [About page](https://github.com/MrMarlonM/good-world-news/issues/20)
- Acceptance Criteria:
    - An about page is existent
    - Information about the company and the team is found there
    - The information is visible for everyone
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Admin delete comments](https://github.com/MrMarlonM/good-world-news/issues/15)
- Acceptance Criteria:
    - Every comment can be deleted
    - After deletion the comment is not visible anymore
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Change the password as editor](https://github.com/MrMarlonM/good-world-news/issues/9)
- Acceptance Criteria:
    - Inside the editor dashboard is a button to change the password
    - The change takes place immediately
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Like articles](https://github.com/MrMarlonM/good-world-news/issues/4)
- Acceptance Criteria:
    - Logged in users can like articles
    - Every user can like each article only once
    - The likes for each article are counted and visible for everybody
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [User comment delete/edit](https://github.com/MrMarlonM/good-world-news/issues/39)
- Acceptance Criteria:
    - Under each comment is a button for deletion
    - Under each comment is a button for edit
    - The deletion asks for confirmation
    - The edit field is the same as the comment field
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Commenting on articles](https://github.com/MrMarlonM/good-world-news/issues/3)
- Acceptance Criteria:
    - When logged in a comment form is provided
    - Every article can be commented by every user
    - A confirmation that the comment was submitted or that there was an error is provided
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Admin comment approval](https://github.com/MrMarlonM/good-world-news/issues/17)
- Acceptance Criteria:
    - Comments need to be approved before they are visible
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Moderator comment approvement](https://github.com/MrMarlonM/good-world-news/issues/16)
- Acceptance Criteria:
    - Before a comment is visible publicly it must be approved
    - Moderators and admins are notified of new comments that are awaiting approval
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

#### User Story: [Delete comments as moderator](https://github.com/MrMarlonM/good-world-news/issues/13)
- Acceptance Criteria:
    - A moderator can delete any content
    - After deletion a comment is not visible anymore
- Manual Steps:
    - d
- Expected Outcome:
    - d
- Actual Outcome:
    - d

## Automated Testing

## Browser Compatibility
The website was tested on the following browsers to ensure cross-browser compatibility and consistent functionality:
- Desktop:
    - Google Chrome
    - Firefox
    - Microsoft Edge
- Mobile:
    - Chrome for Android
    - Safari for OS
    - Opera for Android

The website displayed and functioned correctly across all tested browsers and devices, providing a seamless user experience regardless of the platform.

## Code Validation
### HTML
The HTML code of the project was validated using the [W3C Markup Validation Service](https://validator.w3.org/).

Please refer to [this PDF](documentation/html-validation.pdf) containing all testing documentation.

### CSS
The CSS code of the project was verified using the [W3 jigsaw verification tool](https://jigsaw.w3.org/css-validator/).

![CSS jigsaw verification](documentation/css-validation.png)

### JavaScript
The Javascript code used in this project was verified using the [JS Hint](https://jshint.com/) linter.

![JS Hint verification](documentation/js-hint-comments.png)

### Python
For validation of the python code written throughout the project, please refer to the [Python Testing PDF](documentation/python-validation.pdf).

### Performance (Google Lighthouse)
The performance of the website was tested using [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview).

Whilst the score was mostly good, the performance was a little slower on mobile devices through the images not being optimized for smaller screens.  
However, through using the `Cloudinary` integration for Django it will be possible to automatically optimize images for screen sizes and internet speed but for this stage of the project I did not look further into it.  
The same is true for not optimal Best Practices score. This comes through Cloudinary using third-party-cookies on the website and sending images over as http instead of https.  
Both problems which should be solvable in a future edition of the website through refining the Cloudinary implementation.

![Image of lighthouse score on desktop](documentation/lighthouse-desktop.png)

![Image of lighthouse score on mobile](documentation/lighthouse-mobile.png)

![Image of lighthouse logs about cloudinary](documentation/lighthouse-log.png)

Please click [here](/README.md) to get back to the README.