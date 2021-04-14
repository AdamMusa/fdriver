from setuptools import setup, find_packages


setup(
# the name must match the folder name 'verysimplemodule'
    name="fdriver",
    version="0.0.8",
    author="AdamMusa",
    author_email="adammusa2222@gmail.com",
    description="mvc archhitecture for fastapi",
    long_description="fdriver is a cli program which facilitates the implementation of an mvc architecture in the api. An API made with fdriver is automatically modular, easy to test and exportable because fdriver dockerizes your API " +"\n\n"+open("CHANGELOG.txt").read(),
    url ="https://github.com/AdamMusa/fdriver",
    license = "MIT",
    packages=find_packages(),
    install_requires=["fastapi","uvicorn","typer"], # add any additional packages that 
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['fdriver' ,'fastapi mvc' ,'mvc for fastapi','goode architecture for fastapi'],
    classifiers= [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        'console_scripts':[
            'fdriver=fdriver.main:app',
        ]
    }
)


#python stupe.py sdist
# twine upload dist/*