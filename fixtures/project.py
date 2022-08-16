from models.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_projects(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//td[1]/a[7]").click()
        wd.find_element_by_xpath("//span[2]/a").click()

    def create_new_project(self, project_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//table[3]/tbody/tr"):
                if element.get_attribute("class") not in ('', 'row-category'):
                    cells = element.find_elements_by_tag_name("td")
                    project_name = cells[0].text
                    self.project_cache.append(Project(project_name=project_name))
        return list(filter(None, self.project_cache))

    def delete_project_by_name(self, name):
        wd = self.app.wd
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            cell_name = cells[0].find_element_by_tag_name("href").text
            if cell_name == name:
                cells[0].click()
                break
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
