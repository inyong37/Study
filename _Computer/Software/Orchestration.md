# :whale2: [Orchestration](https://docs.docker.com/get-started/orchestration/)

`This page is from the 'Container' page.`

Tools to manage, scale, and maintain containerized applications are called orchestrators, and the most common examples of these are Kubernetes and Docker Swarm.

---

## :whale2: _Docker Swarm Mode_ | [Docs](https://docs.docker.com/engine/swarm/)

### [Scale the service in the swarm](https://github.com/inyong37/Vision/tree/master/Tutorial/Docker)

### [Apply rolling updates to a service](https://github.com/inyong37/Vision/blob/master/Tutorial/Docker/apply-rolling-updates-to-a-service.md)
   
---

## :whale2: *[Kubernetes](https://kubernetes.io/)* | [What is Kubernetes](https://kubernetes.io/docs/concepts/overview/) | [Tutorial](https://kubernetes.io/docs/tutorials/)

Kubernetes is a portable, extensible, open source platform for managing containerized workload and services, that facilitates both declarative configuration and automation. It has a large rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open-sourced the Kubernetes project in 2014. Kubernetes combines ovver 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community.

:desktop_computer: Tranditional deployment era:
- Hardware
- Operating System
- App

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

:bento: Virtualized deployment era:
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

:whale: Container deployment era:
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

### _[Introduction to Kubernetes architecture](https://www.redhat.com/en/topics/containers/kubernetes-architecture)_

A working Kubernetes deployment is called a cluster: the control plane and the compute machines, or nodes. Each node is its own Linux environment, and could be either a physical or virtual machines. Each node runs pods, which are made up of containers.

Kubernetes cluster:
- Control plane:
  - kube-apiserver
  - kube-scheduler
  - kube-controller-manager
  - etcd
- Compute machines:
  - kubelet
  - kube-proxy
  - Container runtime
  - Pod
- Persistant storage
- Container registry

Underlying infrastructure:
- Physical (bare-metal)/Virtual server
- Private/Public/Hybird Cloud server

### _[Components](https://kubernetes.io/docs/concepts/overview/components/)_ | [Blog (KR)](https://wiki.webnori.com/display/kubernetes/Architecture)

A Kubernetes cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.

- Control Pane Components
  - kube-apiserver
    - The API server is a component of the Kubernetes control plane that exposes the Kubernetes API.
    - The API server is the front end for the Kubernetes control plane.
  - etcd
    - Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.
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

kubelet:
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

### :package: _[Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)_

Kubernetes supports many types of volumes. A pod can use any number of volume types simultaneously. Ephemeral volume types have a lifetime of a pod, but persistent volumes exist beyond the lifetime of a pod. When a pod ceases to exist, Kubernetes destroys ephemeral volumes; however, Kubernetes does not destroy persistent volumes. For any kind of volume in a given pod, data is preserved across container restarts.

### :package: _[Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)_ | [Blog (KR)](https://waspro.tistory.com/580)

A `PersistentVolume (PV)` is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Clsses. It is a resource in the cluster just like a node is a cluster resource. PVs are volume plugins like Volumes, but have a lifecycle independent of any individual Pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

A `PersistentVolumeClaim (PVC)` is a request for storage by a user. It is similar to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can request specific levels of resources (CPU and Memory). Claims can request specific size and access modes (e.g., they can be mounted ReadWriteOnce (RWO), ReadOnlyMany (ROX) or ReadWriteMany (RWX), see AccessModes).

While `PersistentVolumeClaims` allow a user to consume abstract storage resources, it is common that users need PersistentVolumes with varying properties, such as performance, for different problems. Cluster administrators need to be able to offer a variety of PersistentVolumes that differ in more ways than size and access modes, without exposing users to the details of how those volumes are implemented. For these needs, there is the StoargeClass resource.

[Types of Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes):
- PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins:
  - cephyfs - CephFS volume
    - GlusterFS and Ceph
    - Both of them are distributed file systems that can be used to provide shared storage for a Kubernetes cluster.
    - But, they requires more setup and management. 
  - csi - Container Storage Interface (CSI)
  - fc - Fibre Channel (FC) storage
  - hostPath - HostPath volume (for single cnode testing only; WILL NOT WORK in a multi-node cluster; consider using `local` volume instead)
  - iscsi - iSCSI (SCSI over IP) storage)
  - local - loca storage devices mounted on nodes.
  - nfs - Network File System (NFS) storage
    - NFS
    - It is simple and easy to set up, it can be used for storage on-premises or in the cloud.
    - It is commonly used as a shared storage solution for multi-node Kubernetes clusters.
    - It may require you to use an external tool or service to create snapshots.
  - rbd - Rados Block Device (RBD) volume
- The following types of PersistentVolume are deprecated. This means that support is still available but will be removed in a future Kubernetes release.
  - awsElasticBlockStore - AWS Elastic Block Store (EBS) (deprecated in v1.17)
    - AWS Elastic Block Store (EBS)
    - It is similar to GCE PD.
    - It is a good option if you are running your Kubernetes cluster on Amazon Web Service (AWS).
    - AWS EBS has built-in snapshot functionality that can be used to create point-in-time copies of your data.
  - azureDisk - Azure Disk (deprecated in v1.19)
    - Azure Disk
    - Is is a good option if you are running your Kubernetes cluster on Microsoft Azure.
  - azureFile - Azure File (deprecated in v1.21)
  - cinder - Cinder (OpenStack block storage) (deprecated in v1.18)
  - flexVolume - FlexVolume (deprecated in v1.23)
  - gcePersistentDisk - GCE Persistent Disk (deprecated in v1.17)
    - GCE Persistent Disk
    - It is a good option if you are running your Kubernetes cluster on Google Cloud Platform (GCP), they provide a highly available and scalable block storage option.
    - GCE PD has built-in snapshot functionality that can be used to create point-in-time copies of your data.
  - portworxVolume - Portworx volume (deprecated in v1.25)
  - vsphereVolume - vSphere VMDK volume (deprecated in v1.19)
- Older versions of Kubernetes also supported the following in-tree PersistentVolume types:
  - photonPersistentDisk - Photon controller persistent disk. (not available starting v1.15)
  - scaleIO - ScaleIO volume (not available starting v1.21)
  - flocker - Flocker storage (not available starting v1.25)
  - quobyte - Quobyte volume (not available starting v1.25)
  - storageos - StorageOS volume (not available starting v1.25)

[Kubernetes Storage Using Ceph](https://www.velotio.com/engineering-blog/kubernetes-storage-using-ceph): Ceph는 Gluster, Swift에 비해 trasfer speed, latency가 좋고, access가 쉽고, scale up/down이 빠르다.

[쿠버네티스 가상스토리지(Ceph) 설치](https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html)

### [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)

A `VolumeSnapshotContent` is a snapshot taken from a volume in the cluster that has been provisioned by an administrator. It is a resource in the cluster just like a PersistentVolume is a cluster resource.

A `VolumeSnapshot` is a request for snapshot of a volume by a user. It is similar to a PersistentVolumeClaim

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

---

### _[Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)_ | [Blog (KR)](https://hyeo-noo.tistory.com/m/362)

`This content has moved to the 'inyong37/Vision/Tutorial/Kubernetes.md' page.`

---

### *[minikube](https://minikube.sigs.k8s.io/docs/)* | [Hello MiniKube](https://kubernetes.io/docs/tutorials/hello-minikube/)

Minikube quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. We proudly focus on helping application developers and new Kubernetes users.

### _[MicroK8s](https://microk8s.io/)_ by Canonical | [GitHub](https://github.com/canonical/microk8s)

Zero-ops, pure-upstream Kubernetes, from developer workstations to production.

### _[K3S](https://k3s.io/)_

The certified Kubernetes distribution built for IoT & Edge computing.

### _[Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine)_

A scalable and automated Kubernetes service. GKE is a simple way to automatically deploy, scale, and manage Kubernetes.

### _[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)_

The most trusted way to start, run, and scale Kubernetes.

### _[Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift)_

Red Hat® OpenShift® is a unified platform to build, modernize, and deploy applications at scale. Work smarter and faster with a complete set of services for bringing apps to market on your choice of infrastructure.

### _[OKD](https://www.okd.io/)_ | [Blog (KR)](https://velog.io/@_gyullbb/OKD-%EA%B0%9C%EC%9A%94)

The Community Distribution of Kubernetes that powers Red Hat OpenShift.

[MicroK8s vs K3s vs minikube](https://microk8s.io/compare)

---

### [Kubevirt](https://kubevirt.io/) | [GitHub](https://github.com/kubevirt/kubevirt) | [Blog](https://www.tigera.io/blog/using-kubernetes-to-orchestrate-vms/) | [Blog (KR)](https://daaa0555.tistory.com/478)

KubeVirt is a virtual machine management add-on for Kubernetes. The aim is to provide a common ground for virtualization solutions on top of Kubernetes.

CentOS:
- [Deploy Kubernetes on CentOS 7](https://severalnines.com/blog/installing-kubernetes-cluster-minions-centos7-manage-pods-services)
- [Deploy Kubernetes on CentOS 7 and Ubuntu 18 respectively](https://medium.com/@dimuthudesilva24/setting-up-a-simple-kubernetes-cluster-on-ubuntu-and-centos-61d73f43f36b)

Multi-OS Kubernetes:
- [Unified Management of Multi-OS Kubernetes Cluster](https://rafay.co/the-kubernetes-current/unified-management-of-multi-os-kubernetes-clusters/): K8s를 구성하는 cluster를 여러 OS로 구성함.
- [Adapt apps for mixed-OS Kubernetes cluster using node selectors or taints and tolerations in AKS hybrid](https://learn.microsoft.com/en-us/azure/aks/hybrid/adapt-apps-mixed-os-clusters): K8s를 구성하는 cluster를 여러 OS로 구성하고 pod을 node를 지정해서 실행시킴.

---

### :package: [Helm](https://helm.sh/) | [Saramin (KR)](https://saramin.github.io/2020-05-01-k8s-cicd/#cd-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

The package manager for Kubernetes

Helm은 app의 yaml 파일들의 집합을 chart로 관리한다.

### :package: _[Krew](https://krew.sigs.k8s.io/)_

Krew is the plugin manager for kubectl command-line tool.

### [Rancher](https://www.rancher.com/) | [Saramin (KR)](https://saramin.github.io/2020-05-01-k8s-cicd/#cd-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

Rancher is a Kubernetes management tool to deploy and run clusters anywhere and on any provider.

---

### Reference
- MicroK8s, https://microk8s.io/, 2022-12-15-Thu.
- MicroK8s GitHub, https://github.com/canonical/microk8s, 2022-12-15-Thu.
- K3S, https://k3s.io/, 2022-12-15-Thu.
- Deploying Kubernetes on CentOS7 Blog, https://severalnines.com/blog/installing-kubernetes-cluster-minions-centos7-manage-pods-services, 2022-12-15-Thu.
- Deploy Kubernetes on CentOS 7 and Ubuntu 18 respectively Blog, https://medium.com/@dimuthudesilva24/setting-up-a-simple-kubernetes-cluster-on-ubuntu-and-centos-61d73f43f36b, 2022-12-15-Thu.
- Multi-OS Kubernetes Blog, https://rafay.co/the-kubernetes-current/unified-management-of-multi-os-kubernetes-clusters/, 2022-12-15-Thu.
- Multi-OS Kubernetes MS Docs, https://learn.microsoft.com/en-us/azure/aks/hybrid/adapt-apps-mixed-os-clusters, 2022-12-15-Thu.
- GUI Application Stackoverflow, https://stackoverflow.com/questions/16296753/can-you-run-gui-applications-in-a-linux-docker-container/25280523#25280523, 2023-01-03-Tue.
- Ubuntu VNC GitHub, https://github.com/fcwu/docker-ubuntu-vnc-desktop, 2023-01-03-Tue.
- Google Kubernetes Engine, https://cloud.google.com/kubernetes-engine, 2023-01-03-Tue.
- Amazon Elastic Kubernetes Service (EKS), https://aws.amazon.com/eks/, 2023-01-03-Tue.
- Red Hat OpenShift, https://www.redhat.com/en/technologies/cloud-computing/openshift, 2023-01-03-Tue.
- OKD, https://www.okd.io/, 2023-01-03-Tue.
- OKD Blog KR, https://velog.io/@_gyullbb/OKD-%EA%B0%9C%EC%9A%94, 2023-01-03-Tue.
- Kubevirt Blog, https://www.tigera.io/blog/using-kubernetes-to-orchestrate-vms/, 2023-01-03-Tue.
- Kubevirt Blog KR, https://daaa0555.tistory.com/478, 2023-01-03-Tue.
- MicroK8S vs K3s vs minikube, https://microk8s.io/compare, 2023-01-11-Wed.
- Introduction to Kubernetes architecture, https://www.redhat.com/en/topics/containers/kubernetes-architecture, 2023-01-11-Wed.
- What is container orchestration, https://www.redhat.com/en/topics/containers/what-is-container-orchestration, 2023-01-11-Wed.
- Volumes, https://kubernetes.io/docs/concepts/storage/volumes/, 2023-01-11-Wed.
- KubeVirt, https://kubevirt.io/, 2023-01-12-Thu.
- KubeVirt GitHub, https://github.com/kubevirt/kubevirt, 2023-01-12-Thu.
- Kubernetes Storage using Ceph, https://www.velotio.com/engineering-blog/kubernetes-storage-using-ceph, 2023-01-12-Thu.
- 쿠버네티스 가상스토리지(Ceph) 설치, https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html, 2023-01-12-Thu.
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
- YAML Configuration Blog KR, https://hyeo-noo.tistory.com/m/362, 2022-11-22-Tue.
- Minikube Drivers, https://minikube.sigs.k8s.io/docs/drivers/, 2022-11-24-Thu.
- Kubernetes Components, https://kubernetes.io/docs/concepts/overview/components/, 2022-11-25-Fri.
- Nodes, https://kubernetes.io/docs/concepts/architecture/nodes/, 2022-11-25-Fri.
- Controllers, https://kubernetes.io/docs/concepts/architecture/controller/, 2022-11-25-Fri.
- Kubernetes Scheduler, https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/, 2022-11-25-Fri.
- Kubernetes Architecture Blog KR, https://wiki.webnori.com/display/kubernetes/Architecture, 2022-11-29-Tue.
- Here is the package manager for k8s : krew, https://dev.to/omrisama/comment/1bjb2, 2023-01-30-Mon.
- krew VS helm, https://www.libhunt.com/compare-krew-vs-helm, 2023-01-30-Mon.
- Kubernetes, https://kubernetes.io/, 2022-10-11-Tue.
- What is Kubernetes, https://kubernetes.io/docs/concepts/overview/, 2022-10-11-Tue.
- Pod Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/, 2022-10-18-Tue.
- Init Containers Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/init-containers/, 2022-10-18-Tue.
- Ephemeral Containers Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/, 2022-10-18-Tue.
- Kubernetes Tutorial, https://kubernetes.io/docs/tutorials/, 2022-10-19-Wed.
- Minikube, https://minikube.sigs.k8s.io/docs/, 2022-10-19-Wed.
- Disruptions Kubernetes, https://kubernetes.io/docs/concepts/workloads/pods/disruptions/, 2022-10-25-Tue.
- Orchestration Docker Docs, https://docs.docker.com/get-started/orchestration/, 2022-11-21-Mon.
- Swarm Docker Docs, https://docs.docker.com/engine/swarm/, 2022-11-21-Mon.
- Scale the service in the swarm Docker Docs, https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/, 2022-11-21-Mon.
- Docker 가상 환경 구축 입문 (19) - 서비스 스케일링 Blog KR, https://sarc.io/index.php/cloud/1775-docker-19, 2023-04-07-Fri.
