from locust import HttpLocust, TaskSet

class MyTaskSet(TaskSet):
    pass

class WebsiteUser(HttpLocust):
    task_set = MyTaskSet
    host = "http://www.example.com"
    stop_timeout = 30
    min_wait = 2000
    max_wait = 5000
