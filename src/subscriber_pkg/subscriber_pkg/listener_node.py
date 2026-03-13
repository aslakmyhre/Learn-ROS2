import rclpy
from rclpy.node import Node
from my_interfaces.msg import Greeting


class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.subscription = self.create_subscription(
            Greeting,
            'greetings',
            self.on_greeting,
            10,
        )
        self.get_logger().info('ListenerNode started, subscribing to /greetings')

    def on_greeting(self, msg: Greeting):
        self.get_logger().info(
            f'Received from "{msg.sender}" (#{msg.count}): {msg.message}'
        )

        if msg.count == 3:
            raise Exception('Simulated error after receiving 3 messages')


def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
