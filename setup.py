from setuptools import setup, find_packages

setup(
    name='degel-python-utils',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # List your runtime dependencies here
    ],
    extras_require={
        'dev': [
            'pytest',  # example of a development dependency
            # Add other development dependencies here
        ],
    },
    python_requires='>=3.12',
    author='David Goldfarb',
    author_email='deg@degel.com',
    description='Shared Python utilies from Degel Software Ltd.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deg/degel-python-utils',
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
