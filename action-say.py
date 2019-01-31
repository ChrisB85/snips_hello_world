#!/usr/bin/env python3
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
    sentence = 'OK, I say '

    if intent_message.intent.intent_name != 'kblachowicz:say':
        return

    word = intent_message.slots.word.first()

    if word is not None:
        sentence += word.value
    else:
        sentence += 'nothing'

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
