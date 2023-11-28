### [中文版](./readme_zh.md)

### Setup:

1. **Installation**:
   - Install Flask-Migrate: `pip install flask-migrate`
   - Install Flask-Mail: `pip install flask-mail`
   - Install Flask-WTF: `pip install flask-wtf`
   - Install Email Validator: `pip install email_validator`

2. **Database Migration**:
   - Initialize migration: `flask db init`
   - Generate migration: `flask db migrate`
   - Apply migration: `flask db upgrade`

### [Steps Taken](#email-verification-and-database)

#### Setting Up Email Verification:

1. **Flask-Mail Configuration**:
   - Configure email in the app's config
   - Initialize Flask-Mail in extensions
   - Create a view function in `auth.py` for sending emails
   - Test email functionality

2. **Email Verification and Database**:
   - Store verification codes in the database (modify models)
   - Implement three-step migration for database changes
   - Implement AJAX response in JSON format for email verification

3. **Frontend Implementation**:
   - Update HTML paths
   - Integrate AJAX for frontend
   - Implement countdown functionality for verification

### [Form Validation](#user-authentication)

1. **Flask-WTF Setup**:
   - Create form validation using Flask-WTF
   - Utilize the Email Validator package for email validation

### [User Authentication](#question-and-answer-functionalities)

1. **Login Page Backend**:
   - Modify forms for database login tables
   - Update authentication functions
   - Implement session and secret key for login functionality

2. **Hooks and Authentication**:
   - Implement two hooks functions in `app.py`
   - Toggle between logged-in and non-logged-in states

3. **Logout Functionality**:
   - Create a view function for the logout page

### [Question and Answer Functionalities](#troubleshooting-css-loading-issues)

1. **Create Q&A Views and Pages**:
   - Implement view functions and HTML pages for posting questions and answers
   - Modify models for Q&A functionalities
   - Implement decorators to validate user login status for posting questions

2. **Render Q&A Templates**:
   - Update `index.html` and corresponding view functions in Q&A module
   - Modify avatar images for Q&A section

3. **Implement Q&A Listing Page**:
   - Update `detail.html` and view functions for question details
   - Implement navigation from index to question details

4. **Troubleshooting CSS Loading Issues**:
   - Identify issues with CSS file loading
   - Resolve by using `url_for` instead of relative paths in `base.html`

### [Answer Models and Corrections](#submission-error-correction)

1. **Troubleshooting Database Table Creation**:
   - Address issues with table creation errors
   - Resolve by deleting the database and migrations, then recreating

2. **Model Correction**:
   - Correct the model discrepancies for the 'author' field

3. **Password Field Length Adjustment**:
   - Address password field length limitation causing server errors
   - Modify the password field length in the model and perform migrations

4. **Submission Error Correction**:
   - Resolve submission error by adding a missing 'return' statement in the view function

5. **Implement Answer Submission**:
   - Backend: Validate form and view functions for posting answers
   - Frontend: Update the detail page for rendering answer lists

6. **Search Functionality**:
   - Backend: Implement search functionality in the Q&A module
   - Frontend: Update base HTML for search functionality

### [Additional Tasks](#project-completion)

- Improve commit messages and document previously fixed errors
- Write an English version of the markdown documentation

### [Project Completion](#中文版)

- Finished the project by implementing all functionalities
- Video Tutorial: [Link](https://www.bilibili.com/video/BV17r4y1y7jJ?p=41&vd_source=1a0df84062fc3afe05ddb5436ffce988)
- GitHub Repository: [Link](https://github.com/MUC-NBM/zlktqa)

This structured English version offers a detailed overview of the project steps and issues resolved, with navigational links for easier access to specific sections.