from setuptools import setup
from glob import glob

package_name = 'phone_audio_bridge'

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
    description='Phone audio bridge: browser mic -> ROS2 UInt8MultiArray',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'phone_audio_bridge_node = phone_audio_bridge.phone_audio_bridge_node:main',
        ],
    },
)
