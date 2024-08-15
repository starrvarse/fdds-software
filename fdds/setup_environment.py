# setup_environment.py

required_packages = """
Flask==2.3.2
cryptography==41.0.3
pytest==7.4.0
pandas==2.0.3
"""

with open("requirements.txt", "w") as file:
    file.write(required_packages)
