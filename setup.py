import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abroca", # Replace with your own username
    version="0.0.1",
    author="Disha, Vaibhav Kaushik",
    author_email="disha.7003@gmail.com",
    description="package for computing and visualizing the Absolute Between-ROC Area (ABROCA)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VaibhavKaushik3220/abroca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)