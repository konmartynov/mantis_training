from suds.client import Client
from suds import WebFault
from models.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list_user(self):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        projects_list = client.service.mc_projects_get_user_accessible(self.app.credentials.login, self.app.credentials.password)

        return list(map(lambda x: Project(project_name=x.name, project_id=x.id), projects_list))
