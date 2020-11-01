
import os
from glob import glob
from setuptools import setup

package_name = 'launch_host2'

setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        # Include all launch files
        (os.path.join('share', package_name), glob('launch_host2/*.launch.py'))
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = 'Generos',
    maintainer_email = 'rnm1816@gmail.com',
    description = 'This is a package, generated from Generos to contain the Deployment configuration of a Host. This package contains all the Launch Files that the user created in the model.',
    license = 'Inherited from Repository',
    tests_require = ['pytest']
)