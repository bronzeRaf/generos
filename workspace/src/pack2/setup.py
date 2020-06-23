

from setuptools import setup

package_name = 'pack2'

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
    description = 'None',
    license = 'The license is MIT',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		'node2_exec = pack2.node2_node:main',
		'node2_c1 = pack2.node2_node:run_c1',
        ],
    },
)