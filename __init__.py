from mycroft import MycroftSkill, intent_file_handler


class Discroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('discroft.intent')
    def handle_discroft(self, message):
        self.speak_dialog('discroft')


def create_skill():
    return Discroft()

