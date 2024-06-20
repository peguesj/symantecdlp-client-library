from setuptools import setup, find_packages

setup(
    name='symantec_dlp_client',
    version='0.1.0',
    description='Symantec DLP Client Package',
    author='Jeremiah Pegues',
    author_email='jeremiah.pegues@gmail.com',
    url='https://github.com/peguesj/symantecdlp-client-library',
    packages=find_packages(),
    install_requires=[
        'requests==2.25.1',
        'schedule==1.1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
