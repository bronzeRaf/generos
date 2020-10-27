{# 
#This is a jinja2 template of the setup.py of ROS2 launch packages
#
# Written in 26/10/2020
# Written by Rafael Brouzos
#}

import os
from glob import glob
from setuptools import setup

package_name = '{{pack.packageName}}'

setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        # Include all launch files
        (os.path.join('share', package_name), glob('{{pack.packageName}}/*.launch.py'))
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = '{{pack.maintainer}}',
    maintainer_email = '{{pack.email}}',
    description = '{{pack.description}}',
    license = '{{pack.license}}',
    tests_require = ['pytest']
)
