# Vulnerable Project

This is a sample project containing several common vulnerabilities for demonstration purposes.

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python app.py
    ```

## Vulnerabilities

1. **SQL Injection**: `/user/<username>`
2. **Command Injection**: `/run?command=<command>`
3. **Cross-Site Scripting (XSS)**: `/greet?name=<name>`
4. **Insecure Deserialization**: `/deserialize` (POST request with serialized data)