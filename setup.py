import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypwdgen",
    version="v1.0.3",
    author="polluxtroy3758",
    author_email="2147396+polluxtroy3758@users.noreply.github.com",
    description="Complex password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polluxtroy3758/pypwdgen",
    project_urls={
        "Bug Tracker": "https://github.com/polluxtroy3758/pypwdgen/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
