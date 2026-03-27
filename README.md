# ROS2 MQTT Bridge

A ROS2 workspace demonstrating mock sensor nodes and an MQTT bridge for publishing sensor data to an MQTT broker.

## What it does

- **`mock_gps`** - Publishes GPS location and heading data on ROS2 topics
- **`mock_system`** - Publishes system status data on ROS2 topics
- **`ros_mqtt_bridge`** - Subscribes to ROS2 topics and publishes serialized protobuf messages to an MQTT broker

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- An MQTT broker (e.g., Mosquitto) running locally or accessible from the container

## Getting started

### 1. Open in dev container

Open the project in VS Code and click **Reopen in Container** when prompted (or run `Dev Containers: Reopen in Container` from the command palette).

The container will automatically:
- Mount the project to `/repo_root`
- Set working directory to `/repo_root/ros2_ws`
- Run `rosdep update && rosdep install --from-paths ros2_ws/src --ignore-src -r -y`
- Source ROS2 Humble in your bash sessions

### 2. Build the workspace

```bash
# Terminal starts in /repo_root/ros2_ws
colcon build
```

### 3. Source the workspace

```bash
source install/setup.bash
```

> **Note:** ROS2 Humble is already sourced via `.bashrc`. You only need to source the workspace overlay.

### 4. Run the nodes

**Launch all nodes at once** (recommended):

```bash
ros2 launch ros_mqtt_bridge all_nodes.launch.py
```

**Or run nodes individually** in separate terminals (each sourced):

```bash
# Terminal 1
ros2 run mock_gps mock_gps

# Terminal 2
ros2 run mock_system mock_system

# Terminal 3
ros2 run ros_mqtt_bridge ros_mqtt_bridge
```

## Packages

| Package | Type | Description |
|---------|------|-------------|
| `mock_gps` | Python | Mock GPS node publishing location and heading |
| `mock_system` | Python | Mock system node publishing system status |
| `ros_mqtt_bridge` | Python | Bridge that subscribes to ROS2 topics and publishes to MQTT |

## Configuration

The MQTT bridge can be configured via environment variables or a `.env` file in `ros2_ws/src/ros_mqtt_bridge/`:

- `MQTT_HOST` - MQTT broker host (default: `localhost`)
- `MQTT_PORT` - MQTT broker port (default: `1883`)

For macOS hosts, set `MQTT_HOST=host.docker.internal` to reach a broker running on the host.

## Inspecting ROS2 topics

```bash
# List all topics
ros2 topic list

# Echo messages from a specific topic
ros2 topic echo /gps/location
ros2 topic echo /system/status
```

## Inspecting MQTT messages

If you have an MQTT broker running and `mosquitto_sub` installed:

```bash
mosquitto_sub -h localhost -t "marinor/#" -v
```

## Cleaning the workspace

Remove build artifacts manually:

```bash
rm -rf build install log
```

Or install the `colcon-clean` plugin:

```bash
pip install colcon-clean
colcon clean workspace
```
