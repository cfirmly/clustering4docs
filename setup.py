import soyclustering
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="soyclustering",
    version=soyclustering.__version__,
    author=soyclustering.__author__,
    author_email='soy.lovit@gmail.com',
    url='https://github.com/lovit/clustering4docs',
    description="Python library for document clustering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["numpy>=1.22.0"],
    keywords=['document clustering', 'clustering labeling'],
    packages=find_packages()
)
# Dec 31, 2021 numpy>=1.22.0  scikit-learn 1.0.2

# 1.23.5

# matplotlib v3.5.1 Dec 11, 2021