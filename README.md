# generate_content
generating content as per requirements of user by giving input to web page
# AI-Powered Content Generator and Quality Checker

## Project Overview

This project is a web-based application built with **Flask** that provides two main functionalities:

1.  **Content Generation**: Generate articles, blogs, or other content based on a specified topic, type, length, and audience.
2.  **Quality Checker**: Analyze any given text for plagiarism, grammar issues, and overall quality using the **Cohere API**.

The application is structured to be easy to use, with a clean and responsive user interface. All generated and checked content is stored in a history tab for easy access.

-----

## Technology Stack

  * **Backend**: Python, Flask
  * **AI/ML**: Cohere API
  * **Frontend**: HTML, CSS, JavaScript

-----

## Folder Structure

The project follows a standard Flask application structure to keep the code organized and manageable.

```
/ai-content-generator
├── app.py
├── quality_checker.py
├── genei.py
├── templates/
│   ├── main.html
│   ├── history.html
│   └── quality_check.html
└── static/
    └── robot.png
```

### File Descriptions:

  * `app.py`: This is the main Flask application file. It defines the routes for all the web pages and handles the API endpoints for content generation and quality checking.
  * `quality_checker.py`: This Python module contains the logic to interact with the Cohere API to perform plagiarism and quality checks on a given text.
  * `genei.py`: This module, not provided in the files, is responsible for generating the initial content.
  * `templates/`: This folder holds all the HTML files for the application's user interface.
  * `static/`: This folder contains static assets like images, CSS files, and JavaScript files. The `robot.png` image is used for the user profile avatar in the sidebar navigation.
