# Task 4: Secure Password Generator (CLI)

## Repository Name: synent-task4-password-generator-assistant

### 🔐 Project Description
This is a secure password generator built with Python. It allows users to generate strong, randomized passwords that include a mix of uppercase letters, lowercase letters, numbers, and special characters, making them highly resistant to brute-force attacks.

### 🛡️ Core Logic & Security
The password generator ensures that each generated password meets high security standards by:
- **Character Inclusion**: Automatically includes at least one character from each required set:
  - Uppercase (A-Z)
  - Lowercase (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&*...)
- **True Randomness**: Uses Python's `random` module to select characters and `random.shuffle()` to ensure no predictable patterns in the resulting password string.
- **Configurable Length**: Allows the user to specify the desired length (minimum 4 characters) to meet various application requirements.
- **Looping Generation**: Users can generate multiple passwords in a single session.

### 🌟 Key Features
- [x] Secure character set inclusion
- [x] Guarantees at least one character of each type
- [x] Customizable password length (default: 12)
- [x] Pattern-free through randomization and shuffling
- [x] Simple and intuitive CLI interface

### 🌐 Front-End & Demo
The project now includes two front-end options:

#### 1. Interactive Web Demo (HTML/JS)
A standalone web interface that runs directly in your browser without any dependencies.
- **File**: [index.html](file:///c:/projects/synent-task4-password-generator-assistant/index.html)
- **How to Use**: Simply open `index.html` in any web browser.

#### 2. Streamlit Dashboard (Python)
A powerful and modern Python-based web application for generating passwords.
- **File**: [app.py](file:///c:/projects/synent-task4-password-generator-assistant/app.py)
- **How to Use**:
  1. Install dependencies: `pip install -r requirements.txt`
  2. Run the app: `streamlit run app.py`

### ⚙️ How to Use (CLI)
1. Open your terminal and navigate to the project directory.
2. Run the generator:
   ```bash
   python password_generator.py
   ```
3. Enter a number between 1 and 30 when prompted.
4. Your new secure password will be displayed.
