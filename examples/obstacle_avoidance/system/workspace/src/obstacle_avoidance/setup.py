

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
    description = 'This is an obstacle avoidance ROS 2 package.',
    license = 'Apache License 2.0',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		'sonar_exec = obstacle_avoidance.sonar_node:main',
		'motor_exec = obstacle_avoidance.motor_node:main',
		'controller_exec = obstacle_avoidance.controller_node:main',
        ],
    },
)