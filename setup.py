from setuptools import setup, find_packages


setup(
# the name must match the folder name 'verysimplemodule'
    name="mvr", 
    version="0.0.1",
    author="AdamMusa",
    author_email="<adammusa2222@gmail.com>",
    description="this package is inspired by, the mvc architecture",
    long_description="",
    url =""
    packages=find_packages(),
    install_requires=["fastapi","uvicorn"], # add any additional packages that 
    # needs to be installed along with your package. Eg: 'caer'
    
    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 5 - beta",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix :: Linux ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)