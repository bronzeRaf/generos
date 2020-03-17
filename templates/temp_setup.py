{# 
#This is a jinja2 template of the setup.py of ROS2 packages
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}


from setuptools import setup

package_name = '{{pack.packageName}}'

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
    maintainer = '{{pack.maintainer}}',
    maintainer_email = '{{pack.email}}',
    description = '{{pack.description}}',
    license = '{{pack.license}}',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		{% for en in entry_points %}
		'{{en}}',
		{% endfor %}
        ],
    },
)
