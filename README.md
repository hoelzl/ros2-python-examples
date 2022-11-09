# Ros2 Example Programs

These programs are slightly modified versions of the examples
from the [Ros2 documentation](https://docs.ros.org/en/humble/Tutorials.html).

From the root directory of the package (in which this file lives), run

```shell
$ rosdep install -i --from-path src --rosdistro humble -y
rosdep install -i --from-path src --rosdistro humble -y
$ colcon build
Starting >>> py_pubsub
Finished <<< py_pubsub [0.69s]
```

Currently there is a warning during the build if you have a relatively new
Python version.

It would be necessary to fully convert the build system to setup.cfg format to
change this, but I don't know whether this would break anything with Ros2 and
currently don't have the time to figure it out.

Then *in a new terminal* enter the following:

```shell
$ . install/setup.bash
$ ros2 run py_pubsub talker
[INFO] [1667953978.736399100] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [1667953979.229030695] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [1667953979.729034670] [minimal_publisher]: Publishing: "Hello World: 2"
```

In another terminal enter:

```shell
$ . install/setup.bash
$ ros2 run py_pubsub listener
[INFO] [1667954078.045673482] [minimal_subscriber]: I heard: "Hello World: 9"
[INFO] [1667954078.538445915] [minimal_subscriber]: I heard: "Hello World: 10"
[INFO] [1667954079.038688179] [minimal_subscriber]: I heard: "Hello World: 11"
```

