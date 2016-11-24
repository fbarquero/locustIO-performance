from locust import HttpLocust, TaskSet

class UserBehavior(TaskSet):
    pass

class WebsiteUser(HttpLocust):
    pass