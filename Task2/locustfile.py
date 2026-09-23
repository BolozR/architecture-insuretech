import os

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # В RPS-тесте новые соединения распределяются между новыми репликами.
        if os.getenv("CLOSE_CONNECTIONS") == "1":
            self.client.headers["Connection"] = "close"

    @task
    def index(self):
        self.client.get("/")
