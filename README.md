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

   git clone https://github.com/DayveKachi/alx_capstone<br/>
   cd task_api


2. **Create a virtual environment**:

    python -m venv venv<br/>
    source venv/bin/activate

3. **Install dependencies**:

    pip install -r requirements.txt

4. **Apply migrations**:

    python manage.py migrate

5. **Run the development server**:

    python manage.py runserver



## Usage

## Endpoints

- **Authentication**

  - POST /api/login/: login and obtain authentication token.

- **Tasks**

  - GET /api/tasks/list/: List all tasks with optional filters and sorting.

  - GET /api/tasks/: List all tasks with default sorting by due_date.

  - POST /api/tasks/: Create a new task.

  - GET /api/tasks/<id>/: Retrieve a task by ID.

  - PUT /api/tasks/<id>/: Update a task by ID.

  - PATCH /api/tasks/<id>/: Partially update a task by ID.

  - DELETE /api/tasks/<id>/: Delete a task by ID.

- **Users**

  - GET /api/users/: List all users.

  - POST /api/users/new/: Create a new user.

  - GET /api/users/<id>/: Retrieve a user by ID.

  - PUT /api/users/<id>/update/: Fully or partially Update a user by ID.

  - DELETE /api/users/<id>/delete/: Delete a user by ID.

- **Mark Task Complete/Incomplete**:

  - PATCH /api/tasks/<id>/status/: Mark a task as complete or incomplete.

## Example Requests

- **create a task**

  POST /api/tasks/<br/>
    {
      "title": "Finish project report",
      "description": "Complete the final draft of the project report",
      "due_date": "2025-01-20",
      "priority": "High",
      "status": "Pending"
    }

- **Mark Tasks as complete**

  PATCH /api/tasks/1/status/<br/>
    {
      "status": "Completed"
    }
