from functools import cached_property


class RabbitMQTopicQueue:
    def __init__(self, channel, **kwargs):
        self.channel = channel
        self.kwargs = kwargs

    @cached_property
    def name(self):
        result = self.channel.queue_declare('', **self.kwargs)
        return result.method.queue


class RabbitMQTopicPublisher:
    def __init__(self, channel, exchange_name, routing_key):
        self.channel = channel
        self.exchange_name = exchange_name
        self.routing_key = routing_key

    def publish(self, message):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message
        )


class RabbitMQTopicSubscriber:
    def __init__(self, channel, exchange_name, queue, routing_key, **kwargs):
        self.channel = channel
        self.queue = queue
        self.kwargs = kwargs

        self.channel.queue_bind(
            exchange=exchange_name,
            queue=self.queue.name,
            routing_key=routing_key
        )

    def consume(self, callback):
        self.channel.basic_consume(
            queue=self.queue.name,
            on_message_callback=callback,
            **self.kwargs
        )
