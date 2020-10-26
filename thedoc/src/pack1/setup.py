

from setuptools import setup

package_name = 'pack1'

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
    description = ' P1 desc',
    license = 'The license is MIT',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		'node1_exec = pack1.node1_node:main',
		'node3_exec = pack1.node3_node:main',
		'node3_c2 = pack1.node3_node:run_c2',
        ],
    },
)