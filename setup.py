from setuptools import setup, find_packages

setup(
    name='mobile_testing_framework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Appium-Python-Client==2.2.0',
        'pytest==7.4.3',
        'pytest-html==3.2.0'
    ],
    entry_points={'console_scripts': ['mobile-test=tests.test_critical_functionality:main']}
)