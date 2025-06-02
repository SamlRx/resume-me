# Resume-Me

**Resume-Me** is a Python application that generates professional resumes in PDF format using YAML data and an HTML template. It leverages **Jinja2**, **PyYAML**, and **WeasyPrint** for rendering and file generation.

## Features

- Automatic PDF resume generation.
- Customization via a YAML file.
- Flexible and easy-to-edit HTML template.
- Advanced styling for professional output.

## Requirements

- Python >= 3.13

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SamlRx/resume-me.git
   cd resume-me
    ```
2. Create a virtual environment and activate it:
   ```bash
   uv sync
   uv .venv
   source .venv/bin/activate
    ```
3. Run the application:

   ```bash
   python -m src.resume_me.main
   ```

4. Generate dotenv file and inject your email and phone number:
   ```bash
   touch .env
   echo  "RESUME_EMAIL=<your_email>" >> .env
   echo  "RESUME_PHONE=<your_phone>" >> .env
   ```

## Usage
Modify the `resume.yaml` file with your personal information and experience.
   
