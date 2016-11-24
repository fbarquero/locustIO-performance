from locust import HttpLocust, TaskSet

class UserBehavior(TaskSet):

    def get_tasks(self):
        # client object and the requests are build in top of requests python module
        # the base url to access is defined by the host attibute
        # as client is an object
        self.client.get("/")

class WebsiteUser(HttpLocust):
    pass