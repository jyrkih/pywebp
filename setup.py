#!/usr/bin/env python3

from setuptools import setup, find_packages


def get_long_description():
    """Load long project description from the README."""
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except ImportError:
        long_description = open('README.md').read()
    return long_description


setup(
    name='webp',
    version='0.1.0a13',
    url='https://github.com/anibali/pywebp',
    packages=find_packages(include=['webp', 'webp.*', 'webp_build']),
    package_data={'webp_build': ['*.h', '*.c']},
    author='Aiden Nibali',
    description='Python bindings for WebP',
    license='MIT',
    long_description=get_long_description(),
    test_suite='tests',
    setup_requires=['astroid<2.0', 'pylint==1.9.3', 'cffi>=1.0.0', 'conan>=1.8.0', 'importlib_resources>=1.0.0'],
    cffi_modules=['webp_build/builder.py:ffibuilder'],
    install_requires=['enum34>=1.1.6', 'astroid<2.0', 'pylint==1.9.3', 'future>=0.17.1', 'cffi>=1.0.0', 'Pillow>=4.0.0', 'numpy>=1.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'License :: OSI Approved :: MIT License',
    ]
)
