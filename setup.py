from setuptools import setup, find_packages
import unittest

def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='PyElGamal',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Package for ElGamal encryption implementation',
    packages=find_packages(),
    install_requires=[
        'gmpy2',
        'rubenesque'
    ],
    test_suite='setup.run_tests',
    tests_require=['unittest'],
    url='https://github.com/your_username/PyElGamal',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
