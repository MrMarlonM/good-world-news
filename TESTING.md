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
    - Open website in google chrome
    - Right click on the background and choose inspect
    - Go to the Lighthouse section of Dev Tools
    - Create report
    - Ensure that the Accessibility Score is at 100
    - Ensure in the Passed Audits section of the Accessibility Section of the report that alt attributes and aria-labels where checked
- Expected Outcome:
    - The score is at 100
    - Aria-Labels and alt attributes where checked and passed the test
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [About page](https://github.com/MrMarlonM/good-world-news/issues/20)
- Acceptance Criteria:
    - An about page is existent
    - Information about the company and the team is found there
    - The information is visible for everyone
- Manual Steps:
    - Click on the menu toggler
    - Click on the about link in the menu that opened
    - Check that the page opens
    - Check if information about the company and the team is present
- Expected Outcome:
    - The about page opens and renders the text successfully
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Admin delete comments](https://github.com/MrMarlonM/good-world-news/issues/15)
- Acceptance Criteria:
    - Every comment can be deleted
    - After deletion the comment is not visible anymore
- Manual Steps:
    - Login as User 
    - Click on an article
    - Submit a comment
    - Logout
    - Log in as admin
    - Navigate to the Comments section
    - Click on the comment created by user
    - Delete comment
    - Click on view site 
    - Navigate to the commented article
    - Check that the comment is gone
- Expected Outcome:
    - When deleted from the admin the comment is not visible anymore
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Change the password as editor](https://github.com/MrMarlonM/good-world-news/issues/9)
- Acceptance Criteria:
    - Inside the editor dashboard is a button to change the password
    - The change takes place immediately
- Manual Steps:
    - Log in as editor
    - Click on change password in the admin panel
    - Follow the steps to change the password
- Expected Outcome:
    - The password is changed
    - The new password can be used to log in
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Like articles](https://github.com/MrMarlonM/good-world-news/issues/4)
- Acceptance Criteria:
    - Logged in users can like articles
    - Every user can like each article only once
    - The likes for each article are counted and visible for everybody
- Manual Steps:
    - Login as user
    - Navigate to the newsfeed
    - Click on the like button under an article
    - Click on the like button again to see that the article is unliked
    - Try the same for another article
- Expected Outcome:
    - When clicking on the like button the first time:
        - The heart gets red
        - To the like counter one more like is added
        - A message is shown to the user that the article was liked successful
    - When clicking on the like button the second time:
        - The heart becomes hollow again
        - The like counter is subtracted by one
        - A message is shown that the article was successfully unliked
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [User comment delete/edit](https://github.com/MrMarlonM/good-world-news/issues/39)
- Acceptance Criteria:
    - Under each comment is a button for deletion
    - Under each comment is a button for edit
    - The deletion asks for confirmation
    - The edit field is the same as the comment field
- Manual Steps:
    - Login as a user
    - Click on an article
    - Scroll down to the comment section
    - Add a new comment
    - Check if the delete and edit button are visible under the comment
    - Click on the edit button
    - Check if the comment body is transferred back into the comment form
    - Edit the comment and click on Update
    - Check if the comment is updated successfully
    - Click on delete and confirm the deletion in the modal that opens
    - Check if the comment is deleted 
- Expected Outcome:
    - When editing a comment the comment is edited successfully
    - When deleting a comment a modal opens to ask for confirmation and when confirming the comment is deleted
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Commenting on articles](https://github.com/MrMarlonM/good-world-news/issues/3)
- Acceptance Criteria:
    - When logged in a comment form is provided
    - Every article can be commented by every user
    - A confirmation that the comment was submitted or that there was an error is provided
- Manual Steps:
    - Login as user
    - Click on an article
    - Scroll down and check if a comment form is provided
    - Fill out the form and click on submit
    - Check if a confirmation message is shown
    - Check if the comment is posted
- Expected Outcome:
    - When clicking on submit a message is shown
    - The comment is posted and awaiting approval
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Admin comment approval](https://github.com/MrMarlonM/good-world-news/issues/17)
- Acceptance Criteria:
    - Comments need to be approved before they are visible
- Manual Steps:
    - Log in as user
    - Click on an article
    - Submit a new comment
    - Check that the comment awaits approval
    - Login as different user
    - Click on same article
    - Check if the comment is visible
- Expected Outcome:
    - The comment is only visible to the creator
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Moderator comment approvement](https://github.com/MrMarlonM/good-world-news/issues/16)
- Acceptance Criteria:
    - Before a comment is visible publicly it must be approved
    - Moderators can approve comments with a button under the unapproved comments
- Manual Steps:
    - Log in as moderator
    - Click on the same article the user commented earlier
    - Check the comment section if the comment is visible
    - Check if the approve button is visible
    - Click on approve
    - See if the comment is approved
    - Log in as a third user
    - Check the same article for the now approved comment
- Expected Outcome:
    - The moderator can see the unapproved comment
    - The comment is approvable through a button under the comment
    - When clicked on the button the comment is approved and visible to everybody
- Actual Outcome:
    - The expected outcome was fulfilled

#### User Story: [Delete comments as moderator](https://github.com/MrMarlonM/good-world-news/issues/13)
- Acceptance Criteria:
    - A moderator can delete any comment
    - After deletion a comment is not visible anymore
- Manual Steps:
    - Log in as moderator
    - Click on the article with the approved comment
    - Click on the delete button under the comment
    - Confirm the deletion
- Expected Outcome:
    - The comment is deleted
    - The comment is not visible anymore
- Actual Outcome:
    - The expected outcome was fulfilled

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