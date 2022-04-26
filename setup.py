import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polls-AndreVale025",
    version="0.1.70",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreaValentini025/",
    project_urls={
        "Polls": "https://github.com/AndreaValentini025/Prova.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "django-polls",
                 "polls": "django-polls/polls"},
    packages=setuptools.find_packages(),

    python_requires=">=3.6",
)
