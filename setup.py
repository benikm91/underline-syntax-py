from setuptools import setup, find_packages

setup(
    name='underline',
    version='0.1',
    description='Give Scala-Like underline syntax to Python',
    url='https://gitlab.fhnw.ch/benjamin.meyer1/kennwerte_immo_annotator',
    author='Benjamin Meyer',
    author_email='benjamin.meyer@fhnw.ch',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3',
    include_package_data=True,
    install_requires=[
    ],
)