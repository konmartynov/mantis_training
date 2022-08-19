from sys import maxsize


class Project:

    def __init__(self, project_id=None, project_name=None):
        self.project_id = project_id
        self.project_name = project_name

    def __repr__(self):
        return "%s:%s" % (self.project_id, self.project_name)

    def __eq__(self, other):
        return (self.project_id is None or other.project_id is None or self.project_id == other.project_id)\
               and self.project_name == other.project_name

    def sort_by_name(self):
        if self.project_name:
            return self.project_name

    def id_or_max(self):
        if self.project_id:
            return int(self.project_id)
        else:
            return maxsize
