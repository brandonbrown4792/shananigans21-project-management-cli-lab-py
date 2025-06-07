import unittest
from models.user import User
from models.project import Project
from models.task import Task

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User("Alex", "alex@example.com")
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@example.com")
        self.assertTrue(hasattr(user, "id"))

class TestProject(unittest.TestCase):
    def test_create_project(self):
        user_id = "test-user-id"
        project = Project("CLI Tool", "Build tool", "2025-06-30", user_id)
        self.assertEqual(project.title, "CLI Tool")
        self.assertEqual(project.user_id, user_id)

class TestTask(unittest.TestCase):
    def test_create_task(self):
        project_id = "test-project-id"
        task = Task("Implement CLI", "test-user-id", project_id)
        self.assertEqual(task.title, "Implement CLI")
        self.assertEqual(task.status, "incomplete")
    
    def test_mark_complete(self):
        task = Task("Do something", "someone", "proj123")
        task.mark_complete()
        self.assertEqual(task.status, "complete")

if __name__ == "__main__":
    unittest.main()
