# Pitch App
## Author
[Preston-Too](https://github.com/Preston-Too)

## Live Link

## Description
Pitch App is an application that is developed using flask, and its main aim is to allow the users to register and create new pitches. The users can also comment on the pitches that are already there, like and dislike them.

## User Stories
What the user does...
* Register and login users.
* View the pitches other people have posted.
* Vote on the pitch they liked and give it a downvote or upvote.
* Create and submit a pitch in any category.
* view the different categories.

## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Preston-Too/PitchApp.git```

* Move to the folder and install requirements
    ```pip install -r requirements.txt```

* Running the application
    ```python3.6 manage.py runserver / .start.sh```
* Testing the application
    ```python3.6 manage.py test```


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|On loading View Pitch category | Click on category|Taken to the clicked category|
|Click on View pitch| Redirected to the login page if not logged in| Signs In / Signs Up|
|Click on Click create new pitch | If logged in, display form to add a pitch|  Redirected to the home page|
|Click add comment button| Redirects to the comment page|Displays a comment form and a like and dislike button|
|Click on Sign Out | Redirects to the comment page|Signs user out|
|Click on profile|Redirects to the profile page| User adds bio and profile picture and views pitches the user has made|


## Technologies Used

* python3.8
* Flask
* Bootstrap

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [toopreston@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2020 **Preston Too**