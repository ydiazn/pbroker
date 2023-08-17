import unittest
from unittest import TestCase
from unittest.mock import Mock


from pbroker import rabbitmq as proxies


class RabbitMQTopicQueueTest(TestCase):
    def test_name(self):
        channel = Mock()
        result = Mock()
        channel.queue_declare.return_value = result
        result.method.queue = 'queue_name'
        kwargs = {'extra': 'extra'}

        queue = proxies.RabbitMQTopicQueue(channel, **kwargs)
        self.assertEqual('queue_name', queue.name)
        channel.queue_declare.assert_called_once_with('', **kwargs)


class RabbitMQTopicPublisherTest(TestCase):
    def test_publish(self):
        channel = Mock()
        publisher = proxies.RabbitMQTopicPublisher(channel, 'exchange', 'topic')
        publisher.publish('some message')

        channel.basic_publish.assert_called_once_with(
            exchange='exchange',
            routing_key='topic',
            body='some message'
        )


class RabbitMQTopicSubscriberTest(TestCase):
    def test_consume(self):
        channel = Mock()
        queue = Mock()
        queue.name = 'queue'
        callback = Mock()
        kwargs = {'extra': 'extra'}

        subscriber = proxies.RabbitMQTopicSubscriber(
            channel, 'exchange', queue, 'topic', **kwargs)
        subscriber.consume(callback)

        channel.queue_bind.assert_called_once_with(
            exchange='exchange',
            queue='queue',
            routing_key='topic'
        )
        channel.basic_consume.assert_called_once_with(
            queue='queue',
            on_message_callback=callback,
            **kwargs
        )


if __name__ == "__main__":
    unittest.main()