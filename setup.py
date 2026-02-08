from setuptools import find_packages,setup 

def get_requirements(file_path:str):
    '''
    This function will return required python packages

    '''
    requirements = []
    with open(file_path, 'r') as file:
        package = file.readlines()
        package = [pack.replace("\n", "") for pack in package]

        if '-e .' in package:
            package.remove('-e .')

        return package


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Sumed',
    author_email = 'sumedchougale99@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('Requirements.txt')
)