# Application Name: Online Out Pass Service (OOPS)

## Overview
Online Out Pass Service (OOPS) is a role-based leave and out-pass management system for students, teachers, and wardens. It provides a simple interface for users to request, approve, or reject leave applications efficiently. The system currently stores user details in an Excel file and can be expanded with database integration in the future.

## Features
- **Student Page:** Allows students to request leaves.
- **Teacher Page:** Manages teacher leave requests (Day Out and Long Leave options).
- **Warden Page:** Approves or denies leave requests.
- **User Management:** User details are stored in an Excel file (`user_details.xlsx`).

## Files and Their Functions
- `login_page.py`: Handles user authentication.
- `student_page.py`: Provides the interface for student leave requests.
- `teacher_page_dayout.py`: Manages short-term leave requests for teachers.
- `teacher_page_longleave.py`: Manages long-term leave requests for teachers.
- `warden_page.py`: Enables wardens to review and approve leave requests.
- `user_details.xlsx`: Stores user credentials and details.

## Requirements
- Python 3.x
- Required Python libraries (install using `pip install -r requirements.txt` if available)

## Installation and Usage
1. Clone or download the project.
2. Install dependencies if necessary.
3. Run `login_page.py` to start the application.

## Future Enhancements
- Database integration instead of an Excel file.
- Improved UI for better user experience.
- Notifications for leave approval/rejection.

