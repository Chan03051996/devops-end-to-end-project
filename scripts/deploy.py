import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)

run("git pull origin main")
run("docker build -t devops-app .")
run("docker tag devops-app your-dockerhub/devops-app:latest")
run("docker push your-dockerhub/devops-app:latest")
run("kubectl apply -f deployment.yaml")
