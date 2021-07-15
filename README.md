# AUDIOCAVE - Listen Music With Friends Together in a Room

Music Player web application for users listening songs together in a room.

This `audiocave-backend` branch contains only `Backend` part of the project.  

To see `Frontend`, switch to `audiocave-frontend`.

### Project Directory Structure  

Initially, the project started with working both Django as backend and React as frontend in the same repository `main`. And running both on a single localhost server.

Currently, backend `audiocave-backend` and frontend `audiocave-frontend` are separated.

Default Branch `audiocave-backend` contains Backend (Django)

`audiocave-frontend`  contains Frontend (ReactJS).

### Why merge both backend and frontend together  

Since not deployed online, in order to test the project the `main` is used as a single localhost server in `ngrok` to use whenever want to go online.

### How to run project

1. Firstly switch to main branch to run project on localhost.  
2. Create a virtual environment using `python3 -m venv venv`
3. Activate using.
   On Linux `source venv/bin/activate`
   On Windows `venv\Scripts\activate`
4. Install required modules using `pip3 install -r requirements.txt`.
5. Run `npm run build` in `frontend` directory.
6. Run using `python manage.py runserver`

### To create Database:-  

Database should be created before runnign server.
Simply, create database and credentials in `.env` file so that they can be access in settings.py file when configuring database.

## Requirements

1. Node.js
2. Python3
3. PostgreSql
