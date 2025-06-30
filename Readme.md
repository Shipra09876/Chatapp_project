
# A Real-time Chat application 


##  Description 

This Real-Time Chat Application is a full-stack messaging platform that allows users to communicate instantly with friends, manage their contacts, and maintain their chat history in a secure and interactive environment. The application is built to provide smooth user experiences with real-time message delivery and essential user account functionalities. The system has been thoughtfully designed with layered functionalities and clear user roles.


Here is some functionality :
- User registration system 
- Friend management system
- Chat management system
- monitoring and profiles management
- media upload system 
- Notification System
- live streaming

## Demo 
https://drive.google.com/file/d/1DKlHIicFcVBxGjCOo-oMnxdWyciB2ZZx/view?usp=sharing

## Features
### 1. User management system 
- User Registration  
- User Login
- User Profile 
- User logout 
- Forgot password
- Reset password 


### 2. Contact/ Friendship management system
- Send Friend Request 
- Find friend 
- Friend - request - view
- Friend - request - respond 
- View friends 
- Remove friend 
- Block User 
- Block user list 
- add Friend 

### 3. Chat management system
- Room creation 
- One to one chat 
- One to group 

### 4. Monitoring , logging and history : 
- History message and logs save into database

### 5. Media Upload System : 
- images , files , docs , videos etc

### 6. live streaming  : 
- video call and audio call etc

## Tech stack 
### Frontend : 
- HTML , CSS , JavaScript and React Js

### Backend : 
- Django + Django Rest Framework , JWT Authentication , EMail (SMTP)

### Websocket : 
- Django Channels 

### Databse : 
- Sqlite3 
## Installation
### Prerequisites:
- Python (>= 3.9)
- Node.js (>= 14.x)
- PostgreSQL (or your preferred DB)
- npm (comes with Node.js)
- Git
- Redis (for Django Channels, if used)
- Virtual Environment Tool (venv or virtualenv)


### Backend Installation Step:
#### Step 1: Navigate to backend folder
cd backend

#### Step 2: Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#### Step 3: Install required packages
pip install -r requirements.txt

#### Step 4: Configure your sqlite3 
 database in settings.py or .env file

#### Step 5: Apply migrations
python manage.py migrate

#### Step 6: Create superuser (optional but useful)
python manage.py createsuperuser

#### Step 7: Run the development server
python manage.py runserver

### Frontend Installation Step:
#### Step 1: Navigate to frontend folder
cd ../frontend

#### Step 2: Install dependencies
npm install

#### Step 3: Start frontend dev server
npm start  

#### Step 4: Start the application 

## Working :

- User Register the application 
- User login process
- User profile 
- User logout 

- User can send the request anyone who is register in the application
- User find the friend
- Receiver can access friend request
- Receiver respond by accept and reject the request
- Login users can access their friend list
- Login users can remove the friend from their friendlist
- Login user can block the friends
- User can access their block users list
- Add friend into friendlist 
- User can create room
- Friends can chat with each other
- Group Chat
- History message and logs save into database

-
## API endpoints
### Register :
http://localhost:8000/api/account/register/

### Login :
http://localhost:8000/api/account/login/

### Logout :
http://localhost:8000/api/account/logout/

### Profile :
http://localhost:8000/api/account/logout/

### Forgot password :
http://localhost:8000/api/account/change_password/

### Send friend request:
http://127.0.0.1:8000/api/contact/friend-request/

### View friend request: 
http://127.0.0.1:8000/api/contact/friend-request/view/

### Respond request:
http://127.0.0.1:8000/api/contact/friend-requests/respond/<id>

### View friend list :
http://127.0.0.1:8000/api/contact/friends/

### Remove friend:
http://127.0.0.1:8000/api/contact/friends/<login user id>/

### Block User :
http://127.0.0.1:8000/api/contact/block-user/

### Block User List:  
http://127.0.0.1:8000/api/contact/blocked-users/

### Find friend:
http://127.0.0.1:8000/api/contact/find-friend/?query=shreshth

### Add friend:
http://127.0.0.1:8000/api/contact/find-friend/?query=shreshth

### Private Chat:
http://127.0.0.1:8000/api/contact/chat-room/private/

### Group Chat:
http://127.0.0.1:8000/api/contact/chat-room/group/

### Group Chat Invite :
http://127.0.0.1:8000/api/contact/chat-room/group/invite/

###  Fetching message: 
http://127.0.0.1:8000/api/contact/chat-room/message/<login user id>/



## How it works
### 1. Real-Time Messaging (WebSockets via Django Channels)
#### -> When a user logs in and opens a chat, the frontend opens a WebSocket connection to the backend server.

#### -> This connection stays open, allowing live two-way communication between client and server.

#### -> When a message is sent, it is immediately broadcast to the recipient or the group using Channels.

#### -> The receiver’s frontend gets the new message instantly without refreshing.

### 2. Creating or Joining Chat Rooms
#### -> Users can: Create a new chat room (for group chats) Or automatically join a one-to-one private chat when messaging a friend.

#### -> The backend identifies rooms using unique room names or IDs.

#### -> When a user selects a chat, they are subscribed to that room's channel via WebSocket.


### 3. Sending and Receiving Messages
#### -> When a user types and sends a message:

#### -> It is sent through the WebSocket connection to the backend.

#### -> The backend processes the message, saves it to the database, and broadcasts it to the correct chat room.

#### -> All participants in that chat room receive the message in real time.


### 4. Message Storage and History
#### -> Every message is stored in a PostgreSQL database with metadata (sender, timestamp, room).

#### -> When a user opens a chat, the app fetches previous messages via REST API (or GraphQL) to show chat history.

#### -> Older messages remain available unless deleted or cleared by users.


## Screenshot 
## Deployment 
## Feedback

If you have any feedback, please reach out to us at shipragupta09876.com


# Hi, I'm Shipra Gupta! 👋


## 🚀 About Me
I'm a python software developer...

