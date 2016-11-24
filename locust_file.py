from locust import HttpLocust, TaskSet

class MyTaskSet(TaskSet):

    def get_tasks(self):
        # client object and the requests are build in top of requests python module
        # the base url to access is defined by the host attibute
        # as client is an object
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    host = "http://www.example.com"
    stop_timeout = 30
    min_wait = 2000
    max_wait = 5000