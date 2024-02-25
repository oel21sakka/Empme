# Overall

This is a skeleton application designed to manage employee data with basic CRUD operations. It showcases various Django features such as pagination, signals, and filters, covering the entire Django process from authentication and authorization to working with the ORM and handling templates using base template and DTL alongside the views, and URLs routing.

# Company Domain

This domain encompasses models for companies and departments, along with views to manage them. Only administrators can create companies, after which any company staff can modify or remove departments.
with Dynamic Department Updates: Departments update dynamically on the webpage using AJAX to retrieve company-related departments.

## Endpoints

- Company List: Displays a list of companies.
- Create Company: Allows only administrators to create new companies.
- Company Detail View: Provides details on departments and employees within a company. Accessible only to administrators and company staff.

# Employee Domain

This domain includes models for employees and workflows, featuring:

- A signal tied to employee creation that automatically generates a workflow for the user.
- A method and Django filter, `is_company`, to determine if a user is company staff.
- Workflow functionality indicating how long ago the workflow was updated and how long the employee has been with the company.

## Endpoints

- Employee List: Administrators can view all employees, while others can only see employees within their own company.
- Register: Allows users to register as employees.
- Login / Logout: Provides authentication functionality.
- Employee Detail: Allows viewing, editing, and deleting employee data. Access restricted to administrators, company staff, and the respective user.
- Workflow View: Administrators can view all workflows, while company staff and regular users see only their own.

# Project Domain

This domain encompasses the project model with Dynamic Department and Employee Updates: Departments and employees update dynamically using AJAX.

## Endpoints

- Create Project: Only administrators can create projects.
- List Projects: Displays a list of all projects.
- Project Detail View: Provides detailed information on a project. Accessible to administrators and company staff.

# API Domain

This section provides a basic API to access resources, featuring filtering, ordering, search, and pagination capabilities.
