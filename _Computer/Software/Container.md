# :whale: *Container* | [IBM](https://www.ibm.com/cloud/learn/containers) | [MS](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview) | [Google](https://cloud.google.com/learn/what-are-containers) | [Docker](https://www.docker.com/resources/what-container/) | [Kubernetes](https://kubernetes.io/docs/concepts/containers/)

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

### *Container Runtimes* | [Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

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

# :whale2: _Orchestration_ | [Docs](https://docs.docker.com/get-started/orchestration/)

Tools to manage, scale, and maintain containerized applications are called orchestrators, and the most common examples of these are Kubernetes and Docker Swarm.

## :whale2: _Docker Swarm Mode_ | [Docs](https://docs.docker.com/engine/swarm/)

### _[Scale the service in the swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/)_ | [Blog (KR)](https://sarc.io/index.php/cloud/1775-docker-19)

Once you have deployed a service to a swarm, you are ready to use the Docker CLI to scale the number of containers in the service. Continers running in a service are called "tasks".

1. If you haven't alreday, open a terminal and ssh into the machine where you run your manager node. For example, the tutorial uses a machine named `manager1`.
2. Run the following command to change the desired state of the service running in the swarm:
    - ```bash
      $ docker service scale <SERVICE-ID>=<NUMBER-OF-TASKS>
      ```
3. Run `docker service ps <SERVICE-ID>` to see the updated task list:
    - ```bash
      $ docker service ps helloworld

      NAME                                    IMAGE   NODE      DESIRED STATE  CURRENT STATE
      helloworld.1.8p1vev3fq5zm0mi8g0as41w35  alpine  worker2   Running        Running 7 minutes
      helloworld.2.c7a7tcdq5s0uk3qr88mf8xco6  alpine  worker1   Running        Running 24 seconds
      helloworld.3.6crl09vdcalvtfehfh69ogfb1  alpine  worker1   Running        Running 24 seconds
      helloworld.4.auky6trawmdlcne8ad8phb0f1  alpine  manager1  Running        Running 24 seconds
      helloworld.5.ba19kca06l18zujfwxyc5lkyn  alpine  worker2   Running        Running 24 seconds
      ```
    - You can see that swarm has created 4 new tasks to scale to a total of 5 running instances of Alpine Linux. THe tasks are distributed between the three nodes of the warm. One is running on `manager1`.
4. Run `docker ps` to see the containers running on the node where you're connected. THe following example shows the tasks running on `manager1`:
    - ```bash
      docker ps

      CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
      528d68040f95        alpine:latest       "ping docker.com"   About a minute ago   Up About a minute                       helloworld.4.auky6trawmdlcne8ad8phb0f1
      ```
    - If you want to see the containers running on other nodes, ssh into those nodes and run the `docker ps` command.

### _[Apply rolling updates to a service](https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/)_ | [Blog (KR)](https://sarc.io/index.php/cloud/1759-docker-18-rolling-update)

1. If you haven't already, open a terminal and ssh into the machine where you run your manage node. For example, the tutorial uses a machine named `manager1`.
2. Deploy your Redis tag to the swarm and configure the swarm with a 10 second update delay. Note that the following example shows an older Redis tag:
    - ```bash
      $ docker service create --replicas 3 --name redis --update-delay 10s redis:3.0.6
      ```
3. Inspect the `redis` service:
    - ```bash
      $ docker service inspect --pretty redis
      
      ...
      UpdateConfig:
       Parallelism: 1
       Delay:       10s
      ...
      ```
4. Now you can update the container image for `redis`. The swarm manager applies the update to nodes according to the `UpdateConfig` policy:
    - ```bash
      $ docker service update --image redis:3.0.7 redis
      ```
    - The scheduler applies rolling updates as follows by default:
      - Stop the first task.
      - Schedule update for the stopped task.
      - Start the container for the updated task.
      - If the update to a task returns `RUNNING`, wait for the specified delay period then start the next task.
      - If, at any time during the update, a task returns `FAILED`, pause the update.
5. Run `docker service inspect --pretty redis` to see the new image in the desired state:
    - ```bash
      $ docker service inspect --pretty redis
      ```
    - The output of `service inspect` shows if your update paused due to failure:
    - ```bash
      $ docker service inspect --pretty redis

      ID:             0u6a4s31ybk7yw2wyvtikmu50
      Name:           redis
      ...snip...
      Update status:
       State:      paused
       Started:    11 seconds ago
       Message:    update paused due to failure or early termination of task 9p7ith557h8ndf0ui9s0q951b
      ...snip...
      ```
    - To restart a paused update run `docker service update <SERVICE-ID>`. For example:
    - ```bash
      $ docker service update redis
      ```
    - To avoid repeating certain update failures, you may need to reconfigure the service by passing flags to `docker service update`.
6. Run `docker service ps <SERVICE-ID>` to watch the rolling update:
    - ```bash
      $ docker service ps redis

      NAME                                   IMAGE        NODE       DESIRED STATE  CURRENT STATE            ERROR
      redis.1.dos1zffgeofhagnve8w864fco      redis:3.0.7  worker1    Running        Running 37 seconds
       \_ redis.1.88rdo6pa52ki8oqx6dogf04fh  redis:3.0.6  worker2    Shutdown       Shutdown 56 seconds ago
      redis.2.9l3i4j85517skba5o7tn5m8g0      redis:3.0.7  worker2    Running        Running About a minute
       \_ redis.2.66k185wilg8ele7ntu8f6nj6i  redis:3.0.6  worker1    Shutdown       Shutdown 2 minutes ago
      redis.3.egiuiqpzrdbxks3wxgn8qib1g      redis:3.0.7  worker1    Running        Running 48 seconds
       \_ redis.3.ctzktfddb2tepkr45qcmqln04  redis:3.0.6  mmanager1  Shutdown       Shutdown 2 minutes ago
      ```

---

## :whale2: *[Kubernetes](https://kubernetes.io/)* | [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/) | [Tutorial](https://kubernetes.io/docs/tutorials/)

Kubernetes is a portable, extensible, open source platform for managing containerized workload and services, that facilitates both declarative configuration and automation. It has a large rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open-sourced the Kubernetes project in 2014. Kubernetes combines ovver 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community.

### :desktop_computer: Tranditional deployment era

- Hardware
- Operating System
- App

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

### :bento: Virtualized deployment era

- Hardware
- Operating System
- Hypervisor
- Virtual Machine
  - Operating Syste,
  - Bin/Library
  - App

As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.

Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.

Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware.

### :whale: Container deployment era

- Hardware
- Operating System
- Container Runtime
- Container
  - Bin/Library
  - App

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

### _[Components](https://kubernetes.io/docs/concepts/overview/components/)_ | [Blog (KR)](https://wiki.webnori.com/display/kubernetes/Architecture)

A Kubernetes cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.

- Control Pane Components
  - kube-apiserver: The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane.
  - etcd: Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.
  - kube-scheduler
  - kube-controller-manager
  - cloud-controller-manager
- Node Components
  - kubelet
  - kube-proxy
  - Container runtime
- Addons
  - DNS
  - Web UI (Dashboard)
  - Container Resource Monitoring
  - Cluster-level Logging

### _[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)_

```bash
kubectl get node
kubectl get node -o wide
kubectl top nodes
kubectl describe node <insert-node-name-here>
```

- 컨테이너 app이 작동하는 서버로, master API에 의해 node로 명령을 받고 실제 워크로드를 생성하여 서비스가 실행된다.
- Node에는 kubelet, kube-proxy, cAdvisor, container runtime이 배포된다.
- Kubernetes의 기본 container runtime은 Docker이지만 다른 runtime을 사용할 수 있다.
- Node를 여러개 구성해 하나의 cluster를 구성하며, 여러개로 구성하면 서비스 가용성이 향상된다.

Kubelet:
- Node에 배포되는 agent로, master의 API 서버와 통신한다.
    - Node가 수행해야 할 명령을 받아 수행한다.
    - Node의 상태 등을 master로 전달하는 역할을 한다.
- Pod의 manifest file에 따라 컨테이너를 실행, 중지, 또는 마운트의 기능을 한다.
- Node의 상태를 정기적으로 health-check하고, data를 API 서버로 전송한다.

Kube-proxy:
- Node로 들어오는 network traffic을 적절하게 container로 라우팅한다.
- Load balancing 등 node로 들어오고 나가는 network traffic을 프록시한다.
- Node와 master 간의 다양한 중계 및 network 통신을 관리한다.

Container Runtime:
- Pod을 통해 배포된 컨테이너를 실행하는 container runtime 역할을 한다.
- Container runtime은 기본적으로 Docker를 사용한다.
    - 다른 runtime을 사용할 수 있다.

cAdvisor:
- 각 node에서 기동되는 모니터링 agent이다.
- Node 내에서 가동되는 containers의 상태와 성능 등의 정보를 수집하여 master의 API 서버로 전달한다.
    - 전송된 데이터들은 주로 모니터링을 위해서 사용된다.

### _[Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)_

### _[Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)_

### _[Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)_

Required fields:
- In the `.yaml` file for the Kubernetes object you want to create, you'll need to set values for the following fields:
- `apiVersion`
  - Which version of the Kubernetes API you're using to create this object
- `kind`
  - What kind of object you want to create
- `metadata`
  - Data that helps uniquely identify the object, including a `name` string, `UID`, and optional `namespace`
- `spec`
  - What state you desire for the object

### _[Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)_

### _[Pods](https://kubernetes.io/docs/concepts/workloads/pods/)_

```bash
kubectl get pods
kubectl get pods -all-namespaces
kubectl get pods -o wide
kubectl describe pods ${POD_NAME}
```

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.

A Pod (as in a pod of whales or pea pod) is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled. In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.

As well as application containers, a Pod can contain init containers that run during Pod startup. You can also inject ephmeral containers for debugging if your cluster offers this.

While Kubernetes supports more container runtimes than just Docker, Docker is the most commonly known runtime, and it helps to describe Pods using some terminology from Docker.

The shared context of a Pod is a set of Linux namespaces, cgroups, and potentially other facets of isolation - the same things that isolate a container. Within a Pod's context, the individual applications may have further sub-isolations applied.

A Pod is similar to a set of containers with shared namespaces and shared filesystem volumes.

_[Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)_:
- `Pending`
  - The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run.
  - This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.
- -> `Running`
  - The Pod has been bound to a node, and all of the containers have been created.
  - At least one container is still running, or is in the process of starting of restarting.
- -> `Succeeded` or `Failed`
  - All Containers in the Pod have terminated in success, and will not be restarted.
  - All containers in the Pod have terminated, and at least one container has terminated in failure.
  - That is, the container either exited with non-zero status or was terminated by the system.
- `Unknown`
  - For some reason the state of the Pod could not be obtained. This phase typically occures due to an error in communicating with the node where the Pod should be running.
- When a Pod is being deleted, it is shown as `Terminating` by some kubectl commands. This `Terminating` status is not one of the Pod phases. A Pod is granted a term to terminated gracefully, which defaults to 30 seconds. You can use the flag `--force` to terminate a Pod by force.

Container states:
- `Waiting`
  - A container in the `Waiting` state is still running the operations it requires in order to complete start up:
    - for example, pulling the container image from a container image registry,
    - or applying Secret data.
  - When you use `kubectl` to query a Pod with a container that is `Waiting`, you also see a Reason field to summarize why the container is in that state.
- `Running`
  - The `Running` status indicates that a container is executing without issues.
  - If there was a `postStart` hook configured, it has already executed and finished.
  - When you use `kubectl` to query a Pod with a container that is `Running`, you also see information about when the container entered the `Running` state.
- `Terminated`
  - A container in the `Terminated` state began execution and then either ran to completion or failed for some reason.
  - When you use `kubectl` to query a Pod with a container that is `Terminated`, you see a reason, an exit code, and the start and finish time for that container's period of execution.
  - If a container has a `preStop` hook configured, this hook runs before the container enters the `Terminated` state.

Pod conditions:
- `PodScheduled`
  - the Pod has been scheduled to a node.
- `PodHasNetwork`
  - (alpha feature; must be enabled explicitly) the Pod sandbox has been successfully created and networking configured.
- `ContainersReady`
  - all containers in the Pod are ready.
- `Initialized`
  - all init containers have completed successfully.
- `Ready`
  - the Pod is able to serve requests and should be added to the load balancing pools of all matching Services.

### _[Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)_

### _[Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/)_

### _[Persistent Volumes (PV)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)_ | [Blog (KR)](https://waspro.tistory.com/580)

A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Clsses. It is a resource in the cluster just like a node is a cluster resource. PVs are volume plugins like Volumes, but have a lifecycle independent of any individual Pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

A PersistentVolumeClaim (PVC) is a request for storage by a user. It is similar to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., they can be mounted ReadWriteOnce (RWO), ReadOnlyMany (ROX) or ReadWriteMany (RWX), see AccessModes).

While PersistentVolumeClaims allow a user to consume abstract storage resources, it is common that users need PersistentVolumes with varying properties, such as performance, for different problems. Cluster administrators need to be able to offer a variety of PersistentVolumes that differ in more ways than size and access modes, without exposing users to the details of how those volumes are implemented. For these needs, there is the StoargeClass resource.

- emptyDir
- hostpath
- Network Volume

### _[Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)_

Pods do not disappear until someone (a person or a controller) destroy them, or there is an unavoidable hardware or system software error.

### _[Using sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)_

### _[ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)_

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarntee the availablilty of a specified number of identical Pods.

### _[Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)_ | [Saramin (KR)](https://saramin.github.io/2022-05-17-kubernetes-autoscaling/)

In Kubernetes, a HorizontalPodAutoscaler automatically updates a workload resource (such as a Deployment or StatefulSet), with the aim of automatically scaling the workload to match demand.

Horizontal scaling means that the response to increased load is to deploy more Pods. This is different from vertical scaling, which for Kubernetes would mean assigning more resources (for example: memory or CPU) to the Pods that are already running for the workload.

If the load decreases, and the number of Pods is above the configured minimum, the HorizontalPodAutoscaler instructs the workload resource (the Deployment, StatefulSet, or other similar resource) to scale back down.

Horizontal pod autoscaling does not apply to objects that can't be scaled (for example: a DaemonSet.)

The HorizontalPodAutoscaler is implemented as a Kubernetes API resource and a controller. The resource determines the behavior of the controller. The horizontal pod autoscaling controller, running within the Kubernetes control plane, periodically adjusts the desired scale of its target (for example, a Deployment) to match observed metrics such as average CPU utilization, average memory utilization, or any other custom metric you specify.

---


### *[minikube](https://minikube.sigs.k8s.io/docs/)* | [Hello MiniKube](https://kubernetes.io/docs/tutorials/hello-minikube/)

Minikube quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. We proudly focus on helping application developers and new Kubernetes users.

### _[Drivers](https://minikube.sigs.k8s.io/docs/drivers/)_

Linux:
- Docker - container-based (preferred)
- KVM2 - VM-based (preferred)
- VirtualBox - VM
- QEMU - VM (experimental
- None - bare-metal
- Podman - container (experimental)
- SSH - remote ssh

macOS:
- Docker - VM + Container (preferred)
- Hyperkit - VM
- VirtualBox - VM
- Parallels - VM
- VMware Fusion - VM
- QEMU - VM (experimental)
- SSH - remote ssh

Windows:
- Hyper-V - VM (perferred)
- Docker - VM + Container (preferred)
- VirutalBox - VM
- VMware Workstation - VM
- QEMU - VM (experimental)
- SSH - remote ssh

### Issue: minikube start

```bash
* minikube v1.28.0 on Ubuntu 22.04
* Unable to pick a default driver. Here is what was considered, in preference order:
  - docker: Not healthy: "docker version --format {{.Server.Os}}-{{.Server.Version}}" exit status 1: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
  - docker: Suggestion: Add your user to the 'docker' group: 'sudo usermod -aG docker $USER && newgrp docker' <https://docs.docker.com/engine/install/linux-postinstall/>
```

### _[Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)_ | [Blog (KR)](https://hyeo-noo.tistory.com/m/362)

1. _[Create a Kubernetes cluster](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)_
    - ```bash
      # Step 1: Cluster up and running
      minikube version
      minikube start
      # Step 2: Cluster version
      kubectl version
      # Step 3: Cluster details
      kubectl cluster-info
      kubectl get nodes
      ```
      
2. _[Deploy an app](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)_
    - ```bash
      # Step 1: kubectl basics
      kubectl version
      kubectl get nodes
      # Step 2: Deploy our app
      kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
      kubectl get deployments
      # Step 3: View our app
      echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n";
      kubectl proxy
      curl http://localhost:8001/version
      export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
      echo Name of the Pod: $POD_NAME
      curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/ 
      ```
      
3. _[Explore your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)_
    - ```bash
      # Step 1: Check application configuration
      kubectl get pods
      kubectl describe pods
      # Step 2: Show the app in the terminal
      echo -e "\n\n\n\e[92mStarting Proxy. After starting it will not output a response. Please click the first Terminal Tab\n"; kubectl proxy
      export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
      echo Name of the Pod: $POD_NAME
      curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
      # Step 3: View the container logs
      kubectl logs $POD_NAME
      # Step 4: Executing command on the container
      kubectl exec $POD_NAME -- env
      kubectl exec -ti $POD_NAME -- bash
      cat server.js
      curl localhost:8080
      exit
      ```
      
4. _[Expose your app publicly](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)_
    - ```bash
      # Step 1: Create a new service
      kubectl get pods
      kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
      kubectl get services
      kubectl describe services/kubernetes-bootcamp
      export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
      echo NODE_PORT=$NODE_PORT
      curl $(minikube ip):$NODE_PORT
      # Step 2: Using labels
      kubectl describe deployment
      kubectl get pods -l app=kubernetes-bootcamp
      kubectl get services -l app=kubernetes-bootcamp
      export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
      echo Name of the Pod: $POD_NAME
      kubectl label pods $POD_NAME version=v1
      # Step 3 Deleting a service
      kubectl delete service -l app=kubernetes-bootcamp
      kubectl get services
      curl $(minikube ip):$NODE_PORT
      kubectl exec -ti $POD_NAME -- curl localhost:8080
      ```
      
5. _[Scale up your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/)_
    - ```bash
      # Step 1: Scaling a deployment
      kubectl get deployments
      kubectl get rs
      kubectl scale deployments/kubernetes-bootcamp --replicas=4
      kubectl get deployments
      kubectl get pods -o wide
      kubectl describe deployments/kubernetes-bootcamp
      # Step 2: Load Balancing
      kubectl describe services/kubernetes-bootcamp
      export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
      echo NODE_PORT=$NODE_PORT
      curl $(minikube ip):$NODE_PORT
      # Step 3: Scale Down
      kubectl scale deployments/kubernetes-bootcamp --replicas=2
      kubectl get deployments
      kubectl get pods -o wide
      ```
      
6. _[Update your app](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)_
    - ```bash
      # Step 1: Update the version of the app
      kubectl get deployments
      kubectl get pods
      kubectl describe pods
      kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
      kubectl get pods
      # Step 2: Verify an update
      kubectl describe services/kubernetes-bootcamp
      export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
      echo NODE_PORT=$NODE_PORT
      curl $(minikube ip):$NODE_PORT
      kubectl rollout status deployments/kubernetes-bootcamp
      kubectl describe pods
      # Step 3: Rollback an update
      kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
      kubectl get deployments
      kubectl get pods
      kubectl describe pods
      kubectl rollout undo deployments/kubernetes-bootcamp
      kubectl get pods
      kubectl describe pods
      ```

---

### _[HELM](https://helm.sh/): The package manager for Kubernetes_ | [Saramin (KR)](https://saramin.github.io/2020-05-01-k8s-cicd/#cd-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

App의 YAML 파일들의 집합을 chart로 관리

### _[Rancher](https://www.rancher.com/): One Platform Kubernetes Management_ | [Saramin (KR)](https://saramin.github.io/2020-05-01-k8s-cicd/#cd-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

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
- Send a file to/from Container Stackoverflow, https://stackoverflow.com/questions/22907231/how-to-copy-files-from-host-to-docker-container, 2022-10-27-Thu.
- Using sysctls in a Kubernetes Cluster, https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/, 2022-11-17-Thu.
- Orchestration Docker Docs, https://docs.docker.com/get-started/orchestration/, 2022-11-21-Mon.
- Swarm Docker Docs, https://docs.docker.com/engine/swarm/, 2022-11-21-Mon.
- Scale the service in the swarm Docker Docs, https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/, 2022-11-21-Mon.
- Scaling Blog KR, https://sarc.io/index.php/cloud/1775-docker-19, 2022-11-21-Mon.
- Apply rolling updates to a service Docker Docs, https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/, 2022-11-21-Mon.
- Rolling updates Blog KR, https://sarc.io/index.php/cloud/1759-docker-18-rolling-update, 2022-11-21-Mon.
- Horizontal Pod Autoscale Kubernetes, https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/, 2022-11-21-Mon.
- ReplicaSet, https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/, 2022-11-21-Mon.
- Objects Kubernetes, https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/, 2022-11-22-Tue.
- Kubernetes HPA Saramin KR, https://saramin.github.io/2022-05-17-kubernetes-autoscaling/, 2022-11-22-Tue.
- Kubernetes CD Saramin KR, https://saramin.github.io/2020-05-01-k8s-cicd/#cd-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4, 2022-11-22-Tue.
- HELM, https://helm.sh/, 2022-11-22-Tue.
- Rancher, https://www.rancher.com/, 2022-11-22-Tue.
- PV Blog KR, https://waspro.tistory.com/580, 2022-11-22-Tue.
- PV, https://kubernetes.io/docs/concepts/storage/persistent-volumes/, 2022-11-22-Tue.
- Pod Lifecycle, https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/, 2022-11-22-Tue.
- Deployments, https://kubernetes.io/docs/concepts/workloads/controllers/deployment/, 2022-11-22-Tue.
- Learn Kubernetes Basics, https://kubernetes.io/docs/tutorials/kubernetes-basics/, 2022-11-22-Tue.
- Using Minikube to Create a Cluster, https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/, 2022-11-22-Tue.
- Using kubectl to Create a Deployment, https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/, 2022-11-22-Tue.
- Viewing Pods and Nodes, https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/, 2022-11-22-Tue.
- Using a Service to Expose Your App, https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/, 2022-11-22-Tue.
- Running Multiple Instances of Your App, https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/, 2022-11-22-Tue.
- Performing a Rolling Update, https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/, 2022-11-22-Tue.
- YAML Configuration Blog KR, https://hyeo-noo.tistory.com/m/362, 2022-11-22-Tue.
- Minikube Drivers, https://minikube.sigs.k8s.io/docs/drivers/, 2022-11-24-Thu.
- Kubernetes Components, https://kubernetes.io/docs/concepts/overview/components/, 2022-11-25-Fri.
- Nodes, https://kubernetes.io/docs/concepts/architecture/nodes/, 2022-11-25-Fri.
- Controllers, https://kubernetes.io/docs/concepts/architecture/controller/, 2022-11-25-Fri.
- Kubernetes Scheduler, https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/, 2022-11-25-Fri.
- Kubernetes Architecture Blog KR, https://wiki.webnori.com/display/kubernetes/Architecture, 2022-11-29-Tue.
