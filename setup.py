import setuptools

MODULE_NAME='whiner'

packages_list = ['lib'] + [
    f'{'lib'}.{package_name}' 
    for package_name in setuptools.find_namespace_packages(where='lib')
]

setuptools.setup(
    name=MODULE_NAME,
    description='Module used for sandboxing in Whiner suite',
    author='Kamil Rybacki',
    packages=packages_list,
    python_requires='>=3.9',
    version='0.1',
    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=[
        'docker==4.1.0',
        'configparser==5.2.0',
    ],
    zip_safe=False
)
