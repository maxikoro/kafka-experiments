from confluent_kafka import Producer
import time

p = Producer({'bootstrap.servers': 'kafka'})

from pylorem import LoremIpsum
# some_data_source = [[i, LoremIpsum.sentence()] for i in range(100000)]
i = 0

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('{}... Message delivered to {} [{}]'.format(msg.value().decode('utf-8')[:15], msg.topic(), msg.partition()))

while i < 100000:
    i=i+1
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    time.sleep(0.2)

    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    p.produce('topic1', value=(str(i)+' '+LoremIpsum.sentence()).encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()