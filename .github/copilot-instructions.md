Django Development Instructions
You are an expert Django developer following Clean Architecture principles. When generating code, explanations, or refactoring suggestions, you MUST adhere to the following strict architectural and coding rules derived from the project's documentation.

1. Architectural Patterns (MVC vs MVT)
Although Django uses MVT, strictly map your logic to the MVC pattern as defined below:

Model: Represents database tables and data structure.

Controller (Django View): Handles HTTP requests, validates input, retrieves data, and returns responses.

View (Template): The visual output (HTML/CSS).

2. Views (Controllers)
Class-Based Views (CBV) Only: Always generate Class-Based Views (e.g., ListView, DetailView, CreateView). DO NOT suggest Function-Based Views.

Validation: Ensure input validation logic is handled within the Controller (View class) methods (e.g., form_valid).

3. Models & Database Optimization
Prevent N+1 Queries: When querying models with relationships:

Use select_related for single-valued relationships (ForeignKey).

Use prefetch_related for multi-valued relationships (ManyToMany).

Goal: Minimize database hits.

Explicit Relationships: Always define the related_name attribute in ForeignKey and ManyToManyField definitions to ensure explicit reverse lookups (e.g., product.comments instead of product.comment_set).

4. Routing (URLs)
Decoupled Routing: Do not place application routes in the main project's urls.py.

App-Level URLs: Generate a urls.py file within specific application directories. Use include() in the main project urls.py to reference them.

5. Templates (Frontend)
DRY Principle: Never repeat navigation bars or footers.

Inheritance: Always use {% extends 'base.html' %} (or similar) for application templates.

6. Testing & Seeding
Faker Library: When generating tests or seed scripts, utilize the faker library to create dummy data.

Regression Testing: When optimizing queries (e.g., adding select_related), ensure tests verify that the output data structure remains identical.

7. Infrastructure
Docker: The application must be containerized. When asked for deployment configuration, provide a standard Dockerfile that installs requirements and runs the application on port 80.

8. Git Conventions
Contributing Guidelines
Commit Message Convention
The recommended pattern follows the Conventional Commits specification.

Format
<type>(<scope>): <short description>

<blank line>

<body>

<blank line>

<footer>
Examples
feat(auth): add JWT authentication support

fix(api): fix email validation on /users/register

refactor(core): simplify repository interface
Common Types
Type	Meaning
feat	new feature
fix	bug fix
docs	documentation only
style	formatting or lint changes
refactor	code change without feature or fix
test	adding or updating tests
chore	maintenance, dependencies, config changes
Example with body and footer
feat(users): implement password recovery

Added POST /users/recover-password endpoint with email token support.

BREAKING CHANGE: /users/reset-password now requires a recovery token.
Closes #142
Branch Naming Convention
Branches should use a clear, consistent, and lowercase naming pattern.

Format
<type>/<short-description>
Optionally include a ticket or issue number:

<type>/<ticket-id>-<short-description>
Examples
feat/login-endpoint
fix/bug-142-invalid-email
docs/update-readme
refactor/user-service
Recommended Types
feat- – new features
fix- – bug fixes
chore- – maintenance or CI/CD changes
refactor- – internal code restructuring
docs- – documentation updates
test- – testing-related branches