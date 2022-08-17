from models.project import Project


def test_add_project(app):
    r_str = app.gen_random_string()
    project = Project(project_name=r_str)
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_projects_list_administrator()
    app.project.go_to_manage_projects()
    app.project.create_new_project(project.project_name)
    app.project.go_to_manage_projects()
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_projects_list_administrator()
    old_projects.append(project)
    # assert sorted(new_projects, key=Project.sort_by_name) == sorted(old_projects, key=Project.sort_by_name)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_projects_list_administrator(), key=Project.id_or_max)
