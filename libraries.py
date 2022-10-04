class NeuroNetLibrary:
    def call(self, msisdn, date, script):
        pass


class NeuroNluRecognitionResult:

    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def utterance(self):
        pass

    def entity(self, entity_name):
        pass

    def has_entity(self, entity_name):
        pass

    def has_entities(self):
        pass


class NeuroNluLibrary:
    def __init__(self, nlu_call, event_loop):
        self.nlu_call = nlu_call
        self.event_loop = event_loop

    def extract(self):
        return NeuroNluRecognitionResult()


class NeuroVoiceLibrary:
    def __init__(self, nlu_call, loop):
        self.nlu_call = nlu_call
        self.loop = loop

    def say(self, name, val=None):
        pass

    def listen(self):
        pass






