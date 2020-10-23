

from setuptools import setup

package_name = 'obstacle_avoidance'

setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = 'bronzeRaf',
    maintainer_email = 'rnm1816@gmail.com',
    description = 'This is a package that implements an obstacle avoidance algorithm for a robot of one CPU and two SONARS.',
    license = 'Apache License 2.0',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		'sonar1_exec = obstacle_avoidance.sonar1_node:main',
		'sonar2_exec = obstacle_avoidance.sonar2_node:main',
		'cpu_exec = obstacle_avoidance.cpu_node:main',
        ],
    },
)