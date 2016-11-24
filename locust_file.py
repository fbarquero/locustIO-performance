from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    @task
    class SubTaskSet(TaskSet):
        @task
        def my_sub_task(self):
            self.client.get("/about")

        @task
        def my_sub_task_2(self):
            self.client.get("/test")

    @task
    def parent_task(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    host = "http://www.example.com"
    stop_timeout = 30
