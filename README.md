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

4. Run the Development Server
```bash
python recipebook/manage.py runserver
```

### Note

The .env file is already tracked in this repository for the sake of convenience. (In actual practice this will be ommited)

CSCI 40 - Lab 1 Submission
