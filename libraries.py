class NeuroNetLibrary:
    def call(self, msisdn, date, script):
        pass


class NeuroNluRecognitionResult:
    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def entity(self, entity_name):
        pass

    def has_entities(self):
        pass


class NeuroNluLibrary:
    def extract(self):
        return NeuroNluRecognitionResult()


class NeuroVoiceLibrary:
    def say(self, name, val=None):
        pass

    def listen(self):
        pass






