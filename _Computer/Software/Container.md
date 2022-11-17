# :whale2: *Container* | [IBM](https://www.ibm.com/cloud/learn/containers) | [MS](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview) | [Google](https://cloud.google.com/learn/what-are-containers) | [Docker](https://www.docker.com/resources/what-container/) | [Kubernetes](https://kubernetes.io/docs/concepts/containers/)

A container image is a ready-to-run software package, containing everything needed to run an application: the code and any runtime it requires, application and system libraries, and default values for any essential settings.

By design, a container is immutable: you cannot change the code of a container that is already running. If you have a containerized application and want to make changes, you need to build a new image that includes the change, then recreate the container to start from the updated image.

A container is a standard unit of software that packages up code and all its dependencies so that application runs quickly and reliably from one computing envrionment to another.

A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

### *Image* | [Kubernetes](https://kubernetes.io/docs/concepts/containers/images/)

A container image represents binary data that encapsulates an application and all its software dependencies. Container images are executable software bundles that can run standalone and that make very well defined assumptions about their runtime environment.

You typically create a container image of your application and push it to a registry before referring to it in a Pod.

### Container vs. Image | [Blog](https://circleci.com/blog/docker-image-vs-container/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--japac-en-dsa-maxConv-auth-brand&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjwteOaBhDuARIsADBqReilj0_xL4-DCdjzB9-nBAf7OgqEETNDrDTGgfwE2kbLPGVzl62tyXYaAlY4EALw_wcB)

Image ~~ Program

Container ~~ Process


### *[Open Container Initiative (OCI)](https://opencontainers.org/)*

The Open Container Initiative is an open governance structure for the express purpose of creating open industry standards around container formats and runtimes.

Established in June 2015 by Docker and other leaders in the container industry, the OCI currently contains two specifications: the Runtime Specification (runtime-spec) and the Image Specification (image-spec). The Runtime Specification outlines how to run a "filesystem bundle" that is unpacked on disk. At a high-level an OCI implementation would download an OCI Image then unpack that image into an OCI Runtime filesystem bundle. At this point the OCI Runtime Bundle would be run by an OCI Runtime.

### *Container Runtime Interface (CRI)* | [Kubernetes](https://kubernetes.io/docs/concepts/architecture/cri/)

The CRI is a plugin interface which enables the kubelet to use a wide variety of container runtimes, without having a need to recomplile the cluster components.

You need a working container runtime on each Node in your cluster, so that the kubelet can launch Pods and their containers.

The Container Runtime Interface (CRI) is the main protocol for the communication between the kubelet and Container Runtime.

The Kubernetes Container Runtime Interface (CRI) defines the main gRPC protocol for the communication between the cluster components kubelet and container runtime.

## *Container Runtimes* | [Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

The container runtime is the software that is responsible for running containers.

Kubernetes supports container runtimes such as containerd, CRI-O, and any other implementation of the Kubernetes CRI (Container Runtime Interface).

You need to install a container runtime into each node in the cluster so that Pods can run there.

Kubernetes 1.25 requires that you use a runtime that conforms with the Container Runtime Interface (CRI).

---

## :whale: *[Docker](https://www.docker.com/)* | [Docs](https://docs.docker.com/get-started/overview/)

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

### Docker Containers killed by system | [IBM](https://www.ibm.com/docs/en/doc/4.0.1?topic=docker-containers-killed-by-system)

This problem is related to a lack of memory in the docker desktop configuration: the different docker containers have not enough space to be allocated causing either the application to start very slowly or for some services to be killed by docker during their startup.

To correct this problem, go to the Docker Desktop Settings and increase the allocation of Memory to a valid value. We advise to allocate at least 6Gb for simple applications.

### Causes | [Evidian](https://www.evidian.com/products/high-availability-software-for-application-clustering/docker-container-high-availability-cluster-synchronous-replication-failover/)

- Hardware failures (20% of problems), including the complete failure of a computer room.
- Software failures (40% of problems), including restart of critical processes.
- Human errors (40% of problems).

### Ubuntu Image Container | [Blog (KR)](https://sleepyeyes.tistory.com/67)

Method 1.

```bash
sudo docker pull ubuntu
sudo docker create -it --name u1 ubuntu # without '-it': exited right away
sudo docker start u1
sudo docker exec -it u1 /bin/bash # not attach
exit # in container
sudo docker rm u1
```

Method 2.

```bash
sudo docker run it name u1 ubuntu # attach
# KEY: CONTROL & P or CONTROL & Q # in container
```

### Network among the Containers | [Blog (KR)](https://jeongchul.tistory.com/636)

80 port는 host의 ip를 그대로 사용할 수 있다.

### Send a file to/from Container | [Stackoverflow](https://stackoverflow.com/questions/22907231/how-to-copy-files-from-host-to-docker-container)

to: `sudo docker cp foofile {container_id/name}:/`

from: `sudo docker cp {container_id/name}:/home/{username}/foofile /home/{username}/`

---

## :whale: *[Kubernetes](https://kubernetes.io/)* | [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/) | [Tutorial](https://kubernetes.io/docs/tutorials/)

Kubernetes is a portable, extensible, open source platform for managing containerized workload and services, that facilitates both declarative configuration and automation. It has a large rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open-sourced the Kubernetes project in 2014. Kubernetes combines ovver 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community.

### Going back in time

- Tranditional deployment era

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

- Virtualized deployment era

As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.

Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.

Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware.

- Container deployment era

Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.

Containers have become popular because they provide extra benefits, such as:

- Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use.
- Continuous development, integration, and deployment: provides for reliable and frequent container image build and deployment with quick and efficient rollbacks (due to image immutability).
- Dev and Ops separation of concerns: create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
- Observability: not only surfaces OS-level information and metrics, but also application health and other signals.
- Environmental consistency across development, testing, and production: Runs the same on a laptop as it does in the cloud.
- Cloud and OS distribution portability: Runs on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else.
- Application-centric management: Raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources.
- Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine.
- Resource isolation: predictable application performance.
- Resource utilization: high efficiency and density.

### *Pod* | [Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/)

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.

A Pod (as in a pod of whales or pea pod) is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled. In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.

As well as application containers, a Pod can contain init containers that run during Pod startup. You can also inject ephmeral containers for debugging if your cluster offers this.

### *[minikube](https://minikube.sigs.k8s.io/docs/)* | [Hello MiniKube](https://kubernetes.io/docs/tutorials/hello-minikube/)

Minikube quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. We proudly focus on helping application developers and new Kubernetes users.

### *[Init Continers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)*

### *[Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/)*

### *Disruptions* | [Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

Pods do not disappear until someone (a person or a controller) destroy them, or there is an unavoidable hardware or system software error.

### _[Using sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)_

---

### Reference
- Open Container Initiative, https://opencontainers.org/, 2022-07-26-Tue.
- Container Runtime Interface Kubernetes, https://kubernetes.io/docs/concepts/architecture/cri/, 2022-07-26-Tue.
- Kubernetes, https://kubernetes.io/, 2022-10-11-Tue.
- What is Kubernetes, https://kubernetes.io/docs/concepts/overview/, 2022-10-11-Tue.
- Container IBM Cloud, https://www.ibm.com/cloud/learn/containers, 2022-10-17-Mon.
- Container MicroSoft Cloud, https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview, 2022-10-17-Mon.
- Container Google Cloud, https://cloud.google.com/learn/what-are-containers, 2022-10-17-Mon.
- Container Docker, https://www.docker.com/resources/what-container/, 2022-10-17-Mon.
- Docker, https://www.docker.com/, 2022-10-17-Mon.
- What is a Docker, What is a container, https://docs.docker.com/get-started/overview/, 2022-10-17-Mon.
- Container Runtimes Kubernetes, https://kubernetes.io/docs/setup/production-environment/container-runtimes/, 2022-10-18-Tue.
- Container Kubernetes, https://kubernetes.io/docs/concepts/containers/, 2022-10-18-Tue.
- Image Kubernetes, https://kubernetes.io/docs/concepts/containers/images/, 2022-10-18-Tue.
- Pod Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/, 2022-10-18-Tue.
- Init Containers Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/init-containers/, 2022-10-18-Tue.
- Ephemeral Containers Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/, 2022-10-18-Tue.
- Kubernetes Tutorial, https://kubernetes.io/docs/tutorials/, 2022-10-19-Wed.
- Minikube, https://minikube.sigs.k8s.io/docs/, 2022-10-19-Wed.
- Disruptions Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/disruptions/, 2022-10-25-Tue.
- Docker Containers killed by system IBM, https://www.ibm.com/docs/en/doc/4.0.1?topic=docker-containers-killed-by-system, 2022-10-25-Tue.
- SafeKit solves for Docker Evidian, https://www.evidian.com/products/high-availability-software-for-application-clustering/docker-container-high-availability-cluster-synchronous-replication-failover/, 2022-10-25-Tue.
- Ubuntu Container Image Blog KR, https://sleepyeyes.tistory.com/67, 2022-10-27-Thu.
- Container vs. Image Blog, https://circleci.com/blog/docker-image-vs-container/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--japac-en-dsa-maxConv-auth-brand&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjwteOaBhDuARIsADBqReilj0_xL4-DCdjzB9-nBAf7OgqEETNDrDTGgfwE2kbLPGVzl62tyXYaAlY4EALw_wcB, 2022-10-27-Thu.
- Network among the Containers Blog KR, https://jeongchul.tistory.com/636, 2022-10-27-Thu.
- Send a file to/from Container Stackoverfliw, https://stackoverflow.com/questions/22907231/how-to-copy-files-from-host-to-docker-container, 2022-10-27-Thu.
- Using sysctls in a Kubernetes Cluster, https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/, 2022-11-17-Thu.
