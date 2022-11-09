from setuptools import setup

package_name = "py_srvcli"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Matthias Hölzl",
    maintainer_email="tc@xantira.com",
    description="A simple client/server example for Ros2",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "client = py_srvcli.client:main",
            "server = py_srvcli.service:main",
        ],
    },
)
