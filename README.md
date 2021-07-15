# AUDIOCAVE - Listen Music With Friends Together in a Room

Music Player web application for users listening songs together in a room.

### Project Directory Structure:-  

Initially, the project started with working both Django as backend and React as frontend in the same repository `main`. And running both on a single localhost server.

Currently, backend `audiocave-backend` and frontend `audiocave-frontend` are separated.

Default Branch `audiocave-backend` contains Backend (Django)

`audiocave-frontend`  contains Frontend (ReactJS).

### Why merge both backend and frontend together:-  

Since not deployed online, in order to test the project the `main` is used as a single localhost server in `ngrok` to use whenever want to go online.

### How to run project

1. Create a virtual environment using `python3 -m venv venv`
2. Activate using.
   On Linux `source venv/bin/activate`
   On Windows `venv\Scripts\activate`
3. Install required modules using `pip3 install -r requirements.txt`.
4. Run `npm run build` in `frontend` directory.
5. Run using `python manage.py runserver`

## Requirements

1. Node.js
2. Python3
