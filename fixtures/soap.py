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

    def get_projects_list_user(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        projects_list = []

        for project in client.service.mc_projects_get_user_accessible(username,password):
            projects_list.append(Project(project_name=project.name))
        return projects_list

    def get_projects_list_administrator(self):
        return self.get_projects_list_user("administrator", "root")
