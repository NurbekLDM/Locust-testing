from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1-5 seconds between tasks
    
    @task(5)  # Higher weight for homepage
    def homepage(self):
        self.client.get("/")
    
    @task(3)
    def projects_page(self):
        self.client.get("/projects")
    
    @task(2)
    def about_page(self):
        self.client.get("/about")
    
    @task(2)
    def features_page(self):
        self.client.get("/features")
    
    @task(3)
    def blog_page(self):
        self.client.get("/blog")
        
    @task(1)
    def blog_posts(self):
        # Simulate viewing specific blog posts
        for post_id in range(1, 6):  # Test 5 different blog posts
            self.client.get(f"/blog/{post_id}")