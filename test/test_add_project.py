from models.project import Project


def test_add_project(app):
    r_str = app.gen_random_string()
    project = Project(project_name=r_str)
    app.project.go_to_manage_projects()
    old_projects = app.project.get_project_list()
    app.project.create_new_project(project)
    app.project.go_to_manage_projects()
    new_projects = app.project.get_project_list()
    old_projects.append(Project(project_name=r_str))
    assert sorted(new_projects, key=Project.sort_by_name) == sorted(old_projects, key=Project.sort_by_name)
