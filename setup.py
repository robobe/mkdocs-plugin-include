from setuptools import setup, find_packages


setup(
    name='mkdocs-your-plugin',
    version='0.1.0',
    description='A MkDocs plugin that include other source file',
    long_description='',
    keywords='mkdocs',
    url='',
    author='robobe',
    author_email='robobe2020@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'code_include = mkdocs_plugin_include:CodeInclude'
        ]
    }
)
