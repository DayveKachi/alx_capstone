# Task Management API

## Overview
The Task Management API is designed to help users effectively manage their tasks through a series of robust and secure endpoints. It provides functionalities such as task creation, updating, deletion, filtering, sorting, and user management. The API ensures that each user can manage their own tasks securely without accessing other users' tasks.

## Functional Requirements

### Task Management (CRUD)
- **Create, Read, Update, and Delete (CRUD)** operations for tasks.
- Each task includes the following attributes:
  - **Title**
  - **Owner**
  - **Description**
  - **Due Date**
  - **Priority Level** (e.g., Low, Medium, High)
  - **Status** (e.g., Pending, Completed)
- **Validations**:
  - Due date must be in the future.
  - Restrict priority levels to predefined values.
  - Proper status updates.

### Users Management (CRUD)
- **Create, Read, Update, and Delete (CRUD)** operations for users.
- Each user has the following attributes:
  - **Username** (unique)
  - **Email** (unique)
  - **Password**
- Ensure users can manage their own tasks and cannot access tasks of other users.

### Mark Tasks as Complete or Incomplete
- Endpoint to mark tasks as complete or incomplete.
  - Once marked as complete, tasks cannot be edited unless reverted to incomplete.
  - Adds a timestamp when a task is marked as complete.

### Task Filters and Sorting
- Endpoint to list tasks with optional filters:
  - **Status** (Pending or Completed)
  - **Priority**
  - **Due Date**
- Allow sorting tasks by:
  - **Due Date**
  - **Priority Level**

## Installation (Commands are in bash)

1. **Clone the repository**:

   git clone https://github.com/DayveKachi/alx_capstone
   cd task-management-api


2. **Create a virtual environment**:

    python -m venv venv
    source venv/bin/activate

3. **Install dependencies**:

    pip install -r requirements.txt

4. **Apply migrations**:

    python manage.py migrate

5. **Run the development server**:

    python manage.py runserver
