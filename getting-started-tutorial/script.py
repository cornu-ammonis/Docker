import docker
client = docker.from_env()
test_container = client.containers.run("cornuammonis/tutorialrepo:tag", ports = {80:80}, detach=True)
print ("launched container with id " + str(test_container.id))