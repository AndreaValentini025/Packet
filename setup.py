import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AttivitaProgettuale-VAProject",
    version="0.2.49",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreaValentini025/",
    project_urls={
        "AttivitaProgettuale": "https://github.com/AndreaValentini025/Packet.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "application",
                 "AttivitaProgettuale": "application/AttivitaProgettuale"},
    packages=setuptools.find_packages(),

    python_requires=">=3.6",

    install_requires=["Django >= 4.0","django-widget-tweaks"]
)
