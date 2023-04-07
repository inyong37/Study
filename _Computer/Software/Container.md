# :whale: [Container](https://www.docker.com/resources/what-container/) | [IBM](https://www.ibm.com/cloud/learn/containers) | [MS](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview) | [Google](https://cloud.google.com/learn/what-are-containers) | [Kubernetes](https://kubernetes.io/docs/concepts/containers/)

A container image is a ready-to-run software package, containing everything needed to run an application: the code and any runtime it requires, application and system libraries, and default values for any essential settings.

By design, a container is immutable: you cannot change the code of a container that is already running. If you have a containerized application and want to make changes, you need to build a new image that includes the change, then recreate the container to start from the updated image.

A container is a standard unit of software that packages up code and all its dependencies so that application runs quickly and reliably from one computing envrionment to another.

A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

### [Image](https://kubernetes.io/docs/concepts/containers/images/)

A container image represents binary data that encapsulates an application and all its software dependencies. Container images are executable software bundles that can run standalone and that make very well defined assumptions about their runtime environment.

You typically create a container image of your application and push it to a registry before referring to it in a Pod.

[Docker image versus container: What are the differences?](https://circleci.com/blog/docker-image-vs-container/): Image는 Program, Container는 Process와 대응됨.

### [Open Container Initiative (OCI)](https://opencontainers.org/)

The Open Container Initiative is an open governance structure for the express purpose of creating open industry standards around container formats and runtimes.

Established in June 2015 by Docker and other leaders in the container industry, the OCI currently contains two specifications: the Runtime Specification (runtime-spec) and the Image Specification (image-spec). The Runtime Specification outlines how to run a "filesystem bundle" that is unpacked on disk. At a high-level an OCI implementation would download an OCI Image then unpack that image into an OCI Runtime filesystem bundle. At this point the OCI Runtime Bundle would be run by an OCI Runtime.

### Container Runtime Interface (CRI) | [Kubernetes](https://kubernetes.io/docs/concepts/architecture/cri/)

The CRI is a plugin interface which enables the kubelet to use a wide variety of container runtimes, without having a need to recomplile the cluster components.

You need a working container runtime on each Node in your cluster, so that the kubelet can launch Pods and their containers.

The Container Runtime Interface (CRI) is the main protocol for the communication between the kubelet and Container Runtime.

The Kubernetes Container Runtime Interface (CRI) defines the main gRPC protocol for the communication between the cluster components kubelet and container runtime.

### Container Runtimes | [Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

The container runtime is the software that is responsible for running containers.

Kubernetes supports container runtimes such as containerd, CRI-O, and any other implementation of the Kubernetes CRI (Container Runtime Interface).

You need to install a container runtime into each node in the cluster so that Pods can run there.

Kubernetes 1.25 requires that you use a runtime that conforms with the Container Runtime Interface (CRI).

---

## :whale: [Docker](https://www.docker.com/) | [Docs](https://docs.docker.com/get-started/overview/)

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

### [Compose](https://docs.docker.com/compose/)

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

Compose works in all environments: production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your applcations:
- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service

The key features of Compose that make it effective are:
- Have multiple isolated environments on a single host
- Preserves volume ata when containers are created
- Only recreate containers that have changed
- Supports variables and moving a composition between environments

### Docker Containers killed by system | [IBM](https://www.ibm.com/docs/en/doc/4.0.1?topic=docker-containers-killed-by-system)

This problem is related to a lack of memory in the docker desktop configuration: the different docker containers have not enough space to be allocated causing either the application to start very slowly or for some services to be killed by docker during their startup.

To correct this problem, go to the Docker Desktop Settings and increase the allocation of Memory to a valid value. We advise to allocate at least 6Gb for simple applications.

### Causes | [Evidian](https://www.evidian.com/products/high-availability-software-for-application-clustering/docker-container-high-availability-cluster-synchronous-replication-failover/)

- Hardware failures (20% of problems), including the complete failure of a computer room.
- Software failures (40% of problems), including restart of critical processes.
- Human errors (40% of problems).

### [Deploy Ubuntu Image Container](https://github.com/inyong37/Vision/blob/master/Tutorial/Docker/ubuntu-image-container.md)

### Network among the Containers | [Blog (KR)](https://jeongchul.tistory.com/636)

80 port는 host의 ip를 그대로 사용할 수 있다.

### Move a File [to](https://github.com/inyong37/Vision/blob/master/Tutorial/Docker/moving-a-file-from-host-os-to-a-container.md) / [From](https://github.com/inyong37/Vision/blob/master/Tutorial/Docker/moving-a-file-from-a-container-to-host-os.md) a Container

### GUI Application | [Stackoverflow](https://stackoverflow.com/questions/16296753/can-you-run-gui-applications-in-a-linux-docker-container/25280523#25280523) | [Ubuntu-VNC GitHub](https://github.com/fcwu/docker-ubuntu-vnc-desktop)

### [Dockerfile](https://docs.docker.com/engine/reference/builder/)

Docker can build images automatically by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.

---

# :whale2: [Orchestration](https://docs.docker.com/get-started/orchestration/)

`This part has moved to the 'Orchestration' page.`

---

### Reference
- Open Container Initiative, https://opencontainers.org/, 2022-07-26-Tue.
- Container Runtime Interface Kubernetes, https://kubernetes.io/docs/concepts/architecture/cri/, 2022-07-26-Tue.
- Container IBM Cloud, https://www.ibm.com/cloud/learn/containers, 2022-10-17-Mon.
- Container MicroSoft Cloud, https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview, 2022-10-17-Mon.
- Container Google Cloud, https://cloud.google.com/learn/what-are-containers, 2022-10-17-Mon.
- Container Docker, https://www.docker.com/resources/what-container/, 2022-10-17-Mon.
- Docker, https://www.docker.com/, 2022-10-17-Mon.
- What is a Docker, What is a container, https://docs.docker.com/get-started/overview/, 2022-10-17-Mon.
- Container Runtimes Kubernetes, https://kubernetes.io/docs/setup/production-environment/container-runtimes/, 2022-10-18-Tue.
- Container Kubernetes, https://kubernetes.io/docs/concepts/containers/, 2022-10-18-Tue.
- Image Kubernetes, https://kubernetes.io/docs/concepts/containers/images/, 2022-10-18-Tue.
- Docker Containers killed by system IBM, https://www.ibm.com/docs/en/doc/4.0.1?topic=docker-containers-killed-by-system, 2022-10-25-Tue.
- SafeKit solves for Docker Evidian, https://www.evidian.com/products/high-availability-software-for-application-clustering/docker-container-high-availability-cluster-synchronous-replication-failover/, 2022-10-25-Tue.
- Container vs. Image Blog, https://circleci.com/blog/docker-image-vs-container/, 2022-10-27-Thu.
- Network among the Containers Blog KR, https://jeongchul.tistory.com/636, 2022-10-27-Thu.
- Using sysctls in a Kubernetes Cluster, https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/, 2022-11-17-Thu.
- Scaling Blog KR, https://sarc.io/index.php/cloud/1775-docker-19, 2022-11-21-Mon.
- Apply rolling updates to a service Docker Docs, https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/, 2022-11-21-Mon.
- Docker Compose, https://docs.docker.com/compose/, 2022-12-02-Fri.
- Dockerfile, https://docs.docker.com/engine/reference/builder/, 2023-04-07-Friday.
