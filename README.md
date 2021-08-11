<h1 align="center">Keto 4 Me</h1>

![website on all devices](readme_images/responsive_keto.PNG "Picture of website on all devices")

Keto 4 Me is a diet recipe website. Everyone knows dieting isn't easy. Recipes are hard to find. Are they tasty enough for you? Will it impact my diet? All questions which people ask themselves when searching the internet.  

Keto 4 Me is a website for people who are on the Keto diet. This website is a place where people on the diet can get inspired, search for tasty recipes and post their favourite recipes also to the community on the diet. 

Keto 4 Me is designed to inspire people for tasty meal ideas. Everyone is welcome to create an account and add their Keto recipes. If the user has an account, he/she can add, edit and delete their recipes. 

This project is the third out of four Milestone Projects in the Full Stack Web Development Program I am attending at The Code Institute.

**[View the live project here.](https://keto4me.herokuapp.com/)**

---

## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href="#ux-goals">1.1. Project goals</a>
  - <a href="#ux-stories">1.2 User stories</a>
  - <a href="#ux-design">1.3 Design</a>
  - <a href="#ux-architecture">1.4 Information architecture</a>
  - <a href="#ux-mockup">1.5 Mockup designs</a>
- <a href="#features">2. Features</a>
  - <a href="#features-existing">2.1 Existing features</a>
  - <a href="#features-future">2.2 Features left to implement in the future</a>
- <a href="#technologies">3. Technologies used</a>
- <a href="#testing">4. Testing</a>
- <a href="#deployment">5. Deployment</a>
- <a href="#credits">6. Credits</a>
- <a href="#Acknowledge">7. Acknowledge</a>
- <a href="#Acknowledge">8. Disclaimer</a>

---

<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project goals 

- Making a full-stack site that allows users to manage a common dataset about a particular domain. 
- Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask and MongoDB.

- Creating a website that serves as a platform where people can get inspired for keto ideas and where they can share their keto recipes. 
- Creating a website that is simple to understand and easy to navigate.
- The users of the website can make use of CRUD (create, read, update and delete) for the recipes listed. 

<span id="ux-stories"></span>

### 1.2 User stories 

**First-time visitor goals:**
1. As a first time visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet. 
2. As a first time visitor, I want to be able to navigate easily through the website, so I can find everything easily. 
3. As a first time visitor, I want to see an overview of all recipes, so I can get inspired by all recipes.
4. As a first time visitor, I want to be able to search recipes by categories, so I can quickly scan the recipes by category. 
5. As a first time visitor, I want to be able to search recipes based on words, so I can find recipes easily. (For example, I can search the word avocado and all recipes with the ingredient Avovado or avocado in the recipe name will appear.)
6. As a first time visitor, I want to register an account on the website, so I can share my recipes on Keto 4 Me. 

**Site member goals:** 

All the goals of first-time visitors also apply for site members. There are additional user stories to the site members because they have more access to the website. See the additional user stories below. 
1. As a site member, I want to add my recipes, so I can share my recipes. 
2. As a site member, I want to edit my recipes, so I can update information in the recipe.
3. As a site member, I want to delete my recipes, so I can remove the recipe when it is no longer relevant. 
4. As a site member, I want to login to my profile, so I have access to my recipes. 
5. As a site member, I want to logout of my profile, so I am no longer active in a session on the website. 


**Admin goals:**

All the goals of the first time visitors and site members also apply for the admin. The admin has additional user stories to manage the categories of the recipes. 
1. As an admin, I want to add new categories, so I can make the categories clear and manageable. 
2. As an admin, I want to edit categories, so I can update categories. 
3. As an admin, I want to delete categories, so I can remove categories when they are no longer relevant. 
4. I want my users to have a very simple and straight forward approach to my website. 
5. I want them to be able to easily navigate the website.
6. I want them to upload their own recipes. The more recipes that are on the website, the more visitors there'll be

<span id="ux-design"></span>

### 1.3 Design 

- #### Colour scheme 
The two colours that are used for the recipe website are very neutral and simple. I have chosen these colours because the colours give a sleek and uncluttered appearance. 

![Colour scheme](readme_images/blue_grey.PNG "Colour used on website") ![Colour scheme](readme_images/white.PNG "Colour used on website") ![Colour scheme](readme_images/black.PNG "Colour used on website")

- **The blue-grey colour** is used for the header, footer background, the flash messages background and the recipes container box. 
- **The black colour** is used on some of the text headers and also in the recipes. 
- **The white colour** is used for the majority of the text when it's placed on the blue-grey background giving a very clean and easy to read website

- #### Fonts
The **Sans Serif** font is used throughout the whole website. 

- #### Icons
In the project, icons are used that are provided by [Font Awesome](https://fontawesome.com/). The Icons that are used have functional purposes such as the hamburger menu and social media icons. 

- #### Images
The images I used for this project came from [Delish](https://www.delish.com//), and also [BBC recipe website](https://www.bbc.co.uk/food/recipes). Images are used on all the recipes and also for the hero image box which rotates 4 images. 

 #### Defensive design 

    - The user is not able to break the site by clicking on buttons. 
    - The signup form: 
        - The username has to be between 5-15 characters and only must contain letters and numbers. 
        - The password has to be between 5-15 characters and only must contain letters and numbers.
    - The add and edit recipe form:
     - The recipe name has to be between minumum 5 characters and only must contain letters and numbers
        - The category has to be chosen.
        - The number of serves and prepping time has to be numbered.
    - A recipe can't be deleted by just one click. If someone clicks on the delete button, there wil be a pop up with a confirmation if someone is sure to delete the recipe.

#### Interactive design 

    - The website has to be easy to navigate. 
    - The user can quickly find the information he/she wants to find. 

![Interactive design](readme_images/interactive1.PNG)

<span id="ux-architecture"></span>

### 1.4 Information architecture
The project has three collections in the database. The database structure in MongoDB is as follows: 

![Information architecture](readme_images/mongodb_wireframe.PNG)

<span id="ux-mockup"></span>

### 1.5 Wireframe designs
Wireframe designs are made with [Balsamiq](https://balsamiq.com/)

All wireframes can be viewed here [Wireframes](readme_images/wireframes)