# Telemarketers Dashboard Application

The Telemarketers Dashboard is a web application designed to display performance metrics of telemarketers through various interactive visualizations. This guide will help you set up and run the application on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Git
- Python 3.x
- pip (Python package manager)

## Installation

Follow these steps to get the Telemarketers Dashboard up and running:

### 1. Clone the Repository

Open a terminal (Command Prompt or PowerShell on Windows, Terminal app on macOS) and run the following command to clone the repository:

```
git clone https://github.com/JupyterNoteFiend/Demo-Dashboard.git
```

### 2. Navigate to the Project Directory

Change into the project directory with:

```
cd Demo-Dashboard
```

### 3. Install Required Python Packages

Install all the required packages using pip. It's recommended to use a virtual environment to avoid conflicts with other packages. However, if you're okay with installing the packages globally, you can skip the virtual environment setup.

#### Virtual Environment Setup (Optional but Recommended)

- On **Windows**, run:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```

- On **macOS**, run:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

After activating the virtual environment, install the requirements with:

```
pip install -r requirements.txt
```

### 4. Run the Application

Start the dashboard application by running:

- On **Windows**:
  ```
  python TelemarketersDashboard.py
  ```

- On **macOS**:
  ```
  python3 TelemarketersDashboard.py
  ```

### 5. Access the Dashboard

Once the application is running, you will see a message in the terminal indicating that the server has started. Typically, it will say something like:

```
* Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
```

Open a web browser and go to the link provided in the terminal output to view the Telemarketers Dashboard.

## Support

For issues and questions, feel free to contact [repository owner's contact information or issue tracker link].
