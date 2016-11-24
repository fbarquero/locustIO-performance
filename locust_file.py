from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    @task
    class SubTaskSet(TaskSet):
        @task
        def my_sub_task(self):
            pass

        @task
        def my_sub_task_2(self):
            pass

    @task
    def parent_task(self):
        pass


class WebsiteUser(HttpLocust):
    pass