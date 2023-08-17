# pbroker
Poxies for message brokers. Support for rabbitmq topic consumers and publisher.

## RabbitMQ
### RabbitMQ topic consumer

```
from proxies import rabbitmq as proxies

channel = ...
queue = proxies.RabbitMQTopicQueue(channel, exclusive=True)

consume_parameters = {'auto_ack': True}

subscriber = proxies.RabbitMQTopicSubscriber(
    channel, 'exchange name', queue,
    'topic', **consume_parameters
)

subscriber.consume(callback)

channel.start_consuming()
```

where **channel** is a rabbitmq channel and callback is a callable.


### RabbitMQ topic publisher

```
from proxies import rabbitmq as proxies

channel = ...

proxies.RabbitMQTopicPublisher(
    channel,
    'exchange name',
    'topic'
)

publisher.publish('some message')

```

where **channel** is a rabbitmq channel.

