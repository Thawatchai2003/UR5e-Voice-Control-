from setuptools import setup
from glob import glob

package_name = 'speech_web_gui'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/templates', glob('templates/*.html')),
    ],
    install_requires=['setuptools', 'flask'],
    zip_safe=True,
    maintainer='thawatchai',
    maintainer_email='thawatchai@example.com',
    description='Speech Web GUI for mobile control over ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'speech_web_gui_node = speech_web_gui.speech_web_gui_node:main',
        ],
    },
)