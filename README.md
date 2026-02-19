# Django Project Setup Guide

## Prerequisites

Make sure you have the following installed:

- **Python**
- **pip**
- **Git**

## Setup Instructions
1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create and Activate a Virtual Environment

Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```

macOS / Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Generate the Secret Key
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

5. Use the Secret Key in the .env file
```bash
touch <project-name>/.env
```

```bash
# .env
SECRET_KEY='your_generated_secret_key_here'
```

6. Run the Development Server
```bash
python <project-name>/manage.py runserver
```

### Notes

CSCI 40 - Lab Submissions
