# Ros2 Example Programs

These programs are slightly modified versions of the examples
from the [Ros2 documentation](https://docs.ros.org/en/humble/Tutorials.html).


## Building the Ros2 packages

From the root directory of the package (in which this file lives), run

```shell
$ rosdep install -i --from-path src --rosdistro humble -y
rosdep install -i --from-path src --rosdistro humble -y
$ colcon build
Starting >>> simple_pubsub
Starting >>> simple_client_server
Finished <<< simple_client_server [0.90s]
Finished <<< simple_pubsub [0.92s]

Summary: 2 packages finished [1.05s]
```

Currently there are warnings during the build if you have a relatively new
Python version.

It would be necessary to fully convert the build system to setup.cfg format to
change this, but I don't know whether this would break anything with Ros2 and
currently don't have the time to figure it out.


## Running the Pub/Sub Example

*In a new terminal* enter the following:

```shell
$ . install/setup.bash
$ ros2 run simple_pubsub talker
[INFO] [1667953978.736399100] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [1667953979.229030695] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [1667953979.729034670] [minimal_publisher]: Publishing: "Hello World: 2"
```

In another terminal enter:

```shell
$ . install/setup.bash
$ ros2 run simple_pubsub listener
[INFO] [1667954078.045673482] [minimal_subscriber]: I heard: "Hello World: 9"
[INFO] [1667954078.538445915] [minimal_subscriber]: I heard: "Hello World: 10"
[INFO] [1667954079.038688179] [minimal_subscriber]: I heard: "Hello World: 11"
```

## Running the Client/Server example

*In a new terminal* enter the following:

```shell
$ . install/setup.bash
$ ros2 run simple_client_server server
```

```shell
$ . install/setup.bash
$ run simple_client_server client 2 3
[INFO] [1667955235.127477298] [minimal_client_async]: Result of add_two_ints: for 2 + 3 = 5
```

