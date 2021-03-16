from setuptools import setup, find_packages


setup(
# the name must match the folder name 'verysimplemodule'
    name="fdriver", 
    version="0.0.1",
    author="AdamMusa",
    author_email="<adammusa2222@gmail.com>",
    description="this package is inspired by, the mvc architecture",
    long_description=open("README.txt").read() +"\n\n"+open("CHANGELOG.txt").read(),
    url ="",
    license = "MIT",
    packages=find_packages(),
    install_requires=["fastapi","uvicorn"], # add any additional packages that 
    # needs to be installed along with your package. Eg: 'caer'
    
    keywords=['mvr','python mvr','mvr python' 'fastapi mvr','mvr fastapi','mvc for fastapi','goode architecture for fastapi'],
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
