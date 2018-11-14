
class Client:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def get_resource_id(self, name):
        return 10


class JobTemplate:
    def __init__(self, client, name, project, template):
        self.client = client
        self.name = name
        self.project = project
        self.template = template

    def get_resource(self):
        return "{{ jobtemplate: {0} }}".format(self.client.get_resource_id(self.name))
