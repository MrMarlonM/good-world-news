# Good World News
Live Version:

Repository:

Developed By:

## About
Good World News is the News Website for everyone that needs a dose of positivity. The aim is to provide regular updates about everything positive happening on our planet and beyond. No more, no less.

## User Experience Design
### The Big Picture
The website was created for everyone that needs a break from the chaos of their day-to-day life and the focus lays on creating a calm and relaxing atmosphere. For that a light background was chosen, together with big, easily readable and clearly separated content.  
The navigation is kept simple and intuitive to use whilst making sure everything is accessible on deskops as well as on mobile phones and tablets.

### Target Audience
The target audience for this news website are curious people who have a general interest in nature and science, but only want to hear about the good parts of the news cycle.  
And most important: People that just need a break and want to relax in an environment that guarantees to be free from any disturbing information.

### Epics and User Stories
To make sure the interests of the target audience are met, the following Epics with their respective User Stories where created:

#### **EPIC 1:** News Feed as an endless scroll
- **USER STORY:** As a visitor I can see the latest news on the homepage so that I can directly dive into it without further disruption

- **USER STORY:** As a visitor I can see more articles when I'm scrolling down so that I do not need to load a new site to see more content

- **USER STORY:** As a visitor I can sort the articles as needed so that I can directly see content most relevant to me

#### **EPIC 2:** Logging in as an editor
- **USER STORY:** As an editor I can create new articles so that I can update the endless feed with the latest news

- **USER STORY:** As an editor I can log in so that I can access the editor dashboard

- **USER STORY:** As an editor I can edit my own articles so that I can correct mistakes and adapt to changing events

- **USER STORY:** As an editor I can delete my own articles so that I can remove content that is not relevant anymore

- **USER STORY:** As an editor I can change my password so that I can maintain a high level of security

#### **EPIC 3:** Admin panel for moderation of the plattform
- **USER STORY:** As a site administrator I can manage user accounts so that I can keep everything in order

- **USER STORY:** As a site administrator I can delete comments so that I can remove illegal content

- **USER STORY:** As a site admin I can approve comments before they are published so that no illegal content is posted

- **USER STORY:** As a moderator I can approve new and edited comments before they are published so that no illegal content is posted

- **USER STORY:** As a moderator I can delete comments so that I can remove illegal content

- **USER STORY:** As a site admin I can view web analytics so that I'm informed about trends

#### **EPIC 4:** Website Accessibility
- **USER STORY:** As a mobile user I can clearly see the content on the web page so that I can enjoy the experience

- **USER STORY:** As a mobile user I can navigate the website easily so that everything is accessible

- **USER STORY:** As a handicapped person I can use a screen reader to navigate the website so that I'm included as a possible user

#### **EPIC 5:** Contact Form to reach the Company
- **USER STORY:** As a visitor I can contact the company so that I can provide feedback or ask questions

#### **EPIC 6:** About Page
- **USER STORY:** As a visitor I can visit the about page so that I learn more about the company and the team

- **USER STORY:** As a visitor I can see the mission statement and values of the company so that I know what they stand for and what I can expect

#### **EPIC 7:** Registration Form
- **USER STORY:** As a new visitor I can create an account so that I can use advanced features

#### **EPIC 8:** Logging in as a Visitor
- **USER STORY:** As a registered user I can Log In to my account so that I can use advanced features

- **USER STORY:** As a registered user I can change my password so that I can secure my account if needed

#### **EPIC 9:** User Interaction
- **USER STORY:** As a registered user I can comment on posts so that I can share my thoughts and interact with other users and the authors

- **USER STORY:** As a registered user I can like articles so that I show that I show my appreciation of it

- **USER STORY:** As a visitor I can share articles easily through a button so that I can send them to others or share them on social media with ease

## Technologies Used
### Languages
- [Python 3.12.2](https://www.python.org/downloads/release/python-3122/): As primary server-side language.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): For interactivity on the website.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): To style the website.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The markup language for the website.

### Frameworks and Libaries
- [Django](https://www.djangoproject.com/): The framework used for the logic behind the project.
- [Bootstrap](https://getbootstrap.com/): The library used for styling and customization.

### Tools and Helpers
- [Freeconvert](https://www.freeconvert.com/webp-converter): To convert images into webp.
- [Pexels](https://www.pexels.com/): For free images.
- [Google Gemini](https://gemini.google.com/): To write the Fiction Articles
- [Balsamiq](https://balsamiq.com/): For creation of the Wireframes and Database Models
- [Fontawesome](https://fontawesome.com/): For icons used on the website.
- [Google Fonts](https://fonts.google.com/): For implementation of different fonts.
- [Heroku](https://www.heroku.com/): To host the live version
- [Github](https://github.com/): To host the code base
- [Git](https://git-scm.com/): For version control
- [VS Code](https://code.visualstudio.com/): As Code Editor
- [Gitpod](https://www.gitpod.io/): As Virtual Development Environment
- [Pip3](https://pypi.org/project/pip/): As package manager for dependencies.
- [Allauth](https://django-allauth.readthedocs.io/en/latest/): For authentification of different users.
- [Spycopg2](https://pypi.org/project/psycopg2/): As database driver to connect to the database.
- [Gunicorn](https://gunicorn.org/): As webserver to run the website.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/): As cloud database to store the data.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/open/): For debugging the Website.

## Design
### Wireframes
For the Wireframes drawn for this project plese refer to [this PDF](documentation/wireframes-good-world-news.pdf).

## Bugs
### Solved Bugs
- *Bug 1:*  
When applying height and width to images in the newsfeed, the images didn't render properly and stretched or compressed without keeping the right ratio.  
*Solution:*  
To solve the issue, the `width` was set to a `percent value` and the `height` to `auto`

- *Bug 2:*  
When using a url variable `contact_url` in the `base.html` template, it didn't work as intended and couldn't find the corresponding url.  
*Solution:*  
When trying to solve the issue, I found that assigning variables at the top of the template does not work and the issue was resolved through defining the link directly over the url name `href="{% url 'contact' %}"` as given in the `urls.py`.

- *Bug 3:*  
When starting the server in development it didn't work and the server crashed. In the console a `TypeError` was encountered.  
*Solution:*  
The cause for this was a typo in the `forms.py` file within the `contact` app. The instead of an `EmailInput` field an `EmailField` was used which is an unexpected keyword.

- *Bug 4:*  
When using `Summernote` to decorate the articles it didn't work and the page was printing all html tags as plain text.  
*Solution:*  
The problem arose because of Djangos build in feature to excape HTML content automatically for security reasons. To solve the problem the template filter `safe` was used.

### Unsolved Bugs
- Images that are provided through Cloudinary are linked as http instead of https. This affects the performance of the website in Lighthouse enormously.