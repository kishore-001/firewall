from setuptools import find_packages, setup

setup(
    name="Firewall",  # Replace with your project's name
    version="0.1.0",
    author="Kishore",
    author_email="kishorepedu@gmail.com",  # Replace with your email
    description="A simple firewall implemented in Python with features like IP/MAC blocking, logging, and a GUI.",
    long_description=open("README.md").read(),  # Assumes you have a README file
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/firewall",  # Replace with your project URL
    packages=find_packages(),  # Automatically find packages in the project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Specify your license
        "Operating System :: Linux",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
    install_requires=[
        "bcrypt",
        "validators",
        "pyyaml",
        "kivy",  # GUI framework
    ],
)
