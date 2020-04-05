import ocm
from setuptools import setup, find_packages

setup(
    name='one-click-man',
    version=ocm.__version__,
    packages=find_packages(),
    url='https://github.com/thoxvi/one-click-man',
    author='Thoxvi',
    author_email='A@Thoxvi.com',
    description='',
    include_package_data=True,
    entry_points={
        'console_scripts': ['ocm=ocm.start_fooling_yourself:main']
    },
)
