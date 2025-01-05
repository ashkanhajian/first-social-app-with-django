# Social App

This project is a **social media application** with user authentication, posting features, and interactive functionalities like following, liking, and commenting. The app allows users to sign in with either email and password or a one-time password (OTP) sent to their registered phone number. Users can post text and images, interact with other users' content, and manage their accounts.

## Features

- **User Authentication**:
  - Login with email and password.
  - Login using a registered phone number with a one-time password (OTP).
- **Post Creation**:
  - Users can post images and text.
  - Posts can include tags.
  - Users can view posts with common tags.
- **Follow/Unfollow**: Users can follow and unfollow other users.
- **Like/Unlike**: Users can like and unlike posts, implemented using AJAX for smooth interaction.
- **Commenting**: Users can comment on posts.
- **Account Management**:
  - Delete account functionality.
  - Forgot password and reset password features.
- **Tagging**: Users can tag other users in posts.
- **Post Filtering by Tags**: Users can view posts with shared tags.
- **Notifications**:
  - Notifications are sent using Django signals when certain actions occur, such as new followers or comments.
- **AJAX Integration**: Liking, following, and other interactions are handled via AJAX for a seamless user experience.
- **Search**: Users can search based on various account details.
  
## Technologies Used

- **Backend**: [Django] - A Python web framework.
- **Frontend**: HTML, CSS, JavaScript (AJAX for interactions).
- **Database**: SQLite (can be changed to PostgreSQL or MySQL as needed).
- **Notifications**: Django signals for notification system.
- **Authentication**: Custom authentication system with email/password and OTP login.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashkanhajian/your-repo.git
   cd your-repo
Create a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Apply migrations:
bash
Copy code
python manage.py migrate
Create a superuser (admin account):
bash
Copy code
python manage.py createsuperuser
Run the server:
bash
Copy code
python manage.py runserver
Usage
Once the server is running, users can register, create posts, follow others, and interact with posts.
Admins can manage the platform through the admin panel.
Users can log in with either email/password or OTP.
Future Improvements
Implementing direct messaging between users.
Adding support for video posts.
Expanding notification system to include real-time updates.
