from jinja2 import Template
from weasyprint import HTML
import yaml
import json
from jsonschema import validate, ValidationError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if os.getenv("RESUME_EMAIL") is None or os.getenv("RESUME_PHONE") is None:
    print("Environment variables RESUME_EMAIL and RESUME_PHONE must be set.")
    exit(1)

# Load YAML
with open("resources/resume.yaml") as f:
    data = yaml.safe_load(f)

# Inject email and phone from env variables
data["contact"]["email"] = os.getenv("RESUME_EMAIL", "not_provided@example.com")
data["contact"]["phone"] = os.getenv("RESUME_PHONE", "000-000-0000")

# Load JSON Schema
with open("resources/resume_schema.json") as f:
    schema = json.load(f)

# Validate
try:
    validate(instance=data, schema=schema)
except ValidationError as e:
    print("YAML validation failed:", e)
    exit(1)

# Render template
with open("resources/resume_template.html") as f:
    template = Template(f.read())

rendered = template.render(**data)
HTML(string=rendered).write_pdf("target/resume.pdf")
