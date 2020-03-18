import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'ChromePy',  
    version = '0.0.5',
    scripts = [ ],
    author = "Matheus Vanzan",
    author_email = "matheusvnzn@gmail.com",
    description = "Python Selenium Remote for ChromeDriver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/matheusvanzan/chromepy",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)