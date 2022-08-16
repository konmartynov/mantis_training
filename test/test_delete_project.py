from models.project import Project
import random


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        r_str = app.gen_random_string()
        project = Project(project_name=r_str)
        app.project.go_to_manage_projects()
        app.project.create_new_project(project)
    app.project.go_to_manage_projects()
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.project_name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.sort_by_name) == sorted(old_projects, key=Project.sort_by_name)
