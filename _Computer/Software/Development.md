# Development

`This page is from the page 'Program'.`

## [CI/CD](https://en.wikipedia.org/wiki/CI/CD)

In software engineering, CI/CD or CICD is the combined practices of continuous integration (CI) and (more often) continuous delivery or (less often) continuous deployment (CD). They are sometimes referred to collectively as continuous development or continuous software development.

### [Continous Integration](https://en.wikipedia.org/wiki/Continuous_integration)

In software engineering, continous integration (CI) is the practice of merging all developers' working copies to a shared mainline several times a day. Nowadays it is typically implemented in such a way that it triggers an automated biuld with testing.

### [Continous Delivery](https://en.wikipedia.org/wiki/Continuous_delivery)

Continous delivert (CD) is a software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time and, following a pipeline through a "production-like environment", without doing so manually. It aims at building, testing, and releasing software with greater speed and frequency. The approach helps reduce the costs, time, and risk of delivering changes by allowing for mote incremental updates to applications in production. A straightforward and repeatable deployment process is important for continuous delivery.

Continuous delivery contrast with continous deployment (also abbreviated CD), a similar approach in which software is also produced in short cycles but through automated deployments even to production rather than requiring a "click of a button" for that last stel. As such, continous deployment can be viewed as a more complete form of automation than continous delivery.

### [Continous Deployment](https://en.wikipedia.org/wiki/Continuous_deployment)

Continous deployment (CD) is a software engineering approach in which software functionalities are delivered frequently and through automated deployments.

Continous deployment contrashs with continous delivery (also abbreviated CD), a similar approach in which software functionalities are also frequently delivered and deemed to be potentially capable of being deployed, but are actualyl not deployed. As such, continous deployment can be viewed as a more complete form of automation than continous delivery.

* CI/CD? [Blog KR](https://llshl.tistory.com/50)
  * CI란: application codes가 repository에 merge되어 automatically build, test되어 integrated되는 것이다; code -> build -> test
  * CD란(마지막 배포가 수동이면 delivery, 자동이면 deployment): 배포될 준비가 끝난 application을 배포하는 것이다; release -> deploy

---

## :hammer_and_wrench: DevOps | [AWS](https://aws.amazon.com/devops/what-is-devops/?nc1=h_ls)

DevOps is the combination of cultural philosophies, practices, and tools that increases an organization's ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market.

### How DevOps Works

Under a DevOps model, development and operations teams are are no longer "siloed". Sometimes, these two teams are merged into a single team where the engineers work across the entire application lifecycle, from development and test to deployment to operations, and develop a range of skills not limited to a single function.

In some DevOps models, quality assurance and security teams may also become more tightly integrated with development and operations and throughout the application lifecycle. When security is the focus of everyone a DevOps team, this is sometimes referred to as DevSecOps.

These teams use practices to automate processes that historically have been manual and slow. They use a technology stack and tooling which help them operate and evolve applications quickly and reliably. These tools also help engineers independently accomplish tasks (for example, deploying code or provisioning infrastructure) that normally would have required help from other teams, and this further increases a team's velocity.

### Benefits of DevOps

- Speed

Move at high velocity so you can innovate for customers faster, adapt to changing markets better, and grow more efficient at driving business results. The DevOps model enables your developers and operations teams to achieve these results. For example, microservies and continuous delivery let teams take ownership of services and then release updates to them quicker.

- Rapid Delivery

Incrase the frequency and pace of releases so you can innovate and improve your product faster. The quicker you can release new features and fix bugs, the faster you can respond to your customers' needs and build competitive advantage. Continuous integration and continous delivery are practices that automate the software release process, from build to deploy.

- Reliability

Ensure the quality of application updates and infrastructure changes so you can reliably deliver at a more rapid pace while maintaining a positive experience for end users. Use practices like continuous integration and continous delivery to test that each change is functional and safe. Monitoring and logging practices help you stay informed of performance in real-time.

- Scale

Operate and manage your infrastructure and development processes at scale. Automation and consistency help you manage complex or changing systems efficiently and with reduced risk. For example, infrastructure as code helps you manage your development, testing, and production environments in a repeatable and more efficient manner.

- Improved Collaboration

Build more effective teams under a DevOps cultural model, which emphasizes values such as ownership and accountability. Developers and operations teams collaborate closely, share many responsibilities, and combine their workflows. This reduce inefficiencies and saves time (e.g. reduced handover periods between developers and operations, writing code that takes into account the environment in which it is run).

- Security

Move quickly while retaining control and preserving compliance. You can adopt a DevOps model without sacrificing security by using automated compliance policies, find-grained controls, and configuration management techniques. For example, using infrastructure as code and policy as code, you can define and then track compliance at scale.

### Pipeline | [Azure](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) | [AWS](https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/) | [AWS Example](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-devops-example.html)

```Bash
Source code changes are pushed to the repository ->
1. MyRepository: template.yaml, application source code
Pipeline execution start to run through the pipeline -> 
2. MyPipeline
2-1. Source Stage
* GitHub: Source Action
Transition ->
2-2. Prod Stage
* Build: CodeBuild Built Action
* Unit Test: CodeBuild Test Action
* Deploy to Env: CodeDeploy Deploy Action
* Integration Test: CodeBuild Test Action
```

---

## :books: Types of Deployments

### Zero Downtime Deployment | [Samsung SDS](https://www.samsungsds.com/kr/insights/1256264_4627.html) | [Blog (KR)](https://loosie.tistory.com/m/781)

### Rolling Update

Change running instance gradually.

Pros:

- easy to manage due to maintain resources
- easy to roll back due to deploy gradually

Cons: 

- need to consider service capacity with stricted resources
- may cause a compatibility problem due to co-existing different version of services

### Blue Green Deployment | [RedHat](https://www.redhat.com/en/topics/devops/what-is-blue-green-deployment)

Blue green deployment is an application release model that gradually transfers user traffic from a previous version of an app or microservice to a nearly identical new release-both of which are running in production.

The old version can be called the blue environment while the new version can be known as the green environment. Once production traffic is fully transferred from blue to green, blue can standby in case of rollback or pulled from production and updated to become the template upon which the next update is made.

There are downsides to this continuous deployment model. Not all environments have the same uptime requirements or the resources to properly perform CI/CD processes like blue green. But many apps evolve to support such continuous delivery as the enterprises supporting them digitally transform.

Convert traffic to new services from old services at once.

Pros:

- easy to roll back
- can test before deployment
- can reuse old service environment
- less possibility to cause overload

Cons:

- cost a lot: it needs resource as double
  - Virtual/Cloud enviroment is recommended such as AWS, containers(docker), and virtually machines.

### Canary Release

Canary Release method is a deployment strategy that detects problems fast as it can while it deploys new service. It can control versions with using load balancer and deploy gradually with monitoring and feedbacks.

Pros:

- test before deployment
- minimize negative effects, enlarge traffic, easy rollback with phased deployment

Cons:

- need version control due to co-exist of different versions

---

## Tools | [Blog KR](https://ichi.pro/ko/hyeonjae-sayong-ganeunghan-choegoui-ci-cd-dogu-27gaji-194611649728144) | [Jenkins vs. GitHub Actions](https://choseongho93.tistory.com/295)

  * Tools: [Jenkins](https://www.jenkins.io/), TeamCity, CircleCI, [Travis CI](https://www.travis-ci.com/), Bamboo, GoCD, CodeShip, GitLab CI, [Jenkins X](https://jenkins-x.io/), Shippable, Buildkite, Concourse CI, Codefresh, Buddy, Buildbot, Semaphore, Wercker (Oracle), Integrity, Weave Flux, NeverCode, AutoRabit, CruiseControl, Bitrise, DroneCI, UrbanCode (IBM), Strider CD, FinalBuilder, [GitHub Actions](https://github.com/features/actions)

### [Jenkins](https://www.jenkins.io/) | [Docs](https://www.jenkins.io/doc/)

Jenkins is a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software.

Jenkins can be installed through native system pakcages, Docker, or enen run standalone by any machine with a Java Runtime Environment (JRE) installed.

* Jenkins
 * Pros: Free, Open source, Plugins, References (Community, Users)
 * Cons: Resource/Server Required (as t2.medium), Docker (Environment) 

### [Jenkins X](https://jenkins-x.io/) | [Blog KR](https://uzihoon.com/post/eabb9930-5f8a-11ea-8839-c791ea9b277c)

### [Travis CI](https://www.travis-ci.com/)

* Travis CI
 * Pros: GitHub, Process, Setup, No Resource/Server Required
 * Cons: Expensive (129 USD/MON), Different Environment btw Local and VM, Plugins, Update (Git Push)

### [GitHub Actions](https://github.com/features/actions) | [GitHub](https://github.com/actions)

* GitHub Actions
 * Pros: Setup, Process, Languages, Frameworks, Faster than Jenkins, Free (3000 MIN/MON for Private Repo), Cloud (No Environment Required), Async CI/CD
 * Cons: References, Documents, Workflow, UI

### [GitLab Runner](https://docs.gitlab.com/runner/)

GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline.

---

### Reference
- CI/CD, https://deveric.tistory.com/106, 2020-09-14-Mon.
- DevOps AWS, https://aws.amazon.com/devops/what-is-devops/?nc1=h_ls, 2022-10-11-Tue.
- Blue Green Deployment RedHad, https://www.redhat.com/en/topics/devops/what-is-blue-green-deployment, 2022-10-17-Mon.
- Zero Downtime Deployment Samsung SDS, https://www.samsungsds.com/kr/insights/1256264_4627.html, 2022-10-18-Tue.
- Zero Downtime Deployment 3 Methods Blog KR, https://loosie.tistory.com/m/781, 2022-10-18-Tue.
- DevOps Test Blog KR, https://angel927.tistory.com/150, 2022-10-24-Mon.
- CI/CD Wiki, https://en.wikipedia.org/wiki/CI/CD, 2023-03-31-Fri.
- Continous Integration Wiki, https://en.wikipedia.org/wiki/Continuous_integration, 2023-03-31-Fri.
- Continous Deployment Wiki, https://en.wikipedia.org/wiki/Continuous_deployment, 2023-03-31-Fri.
- Jenkins, https://www.jenkins.io/, 2023-03-31-Fri.
- GitLab Runner, https://docs.gitlab.com/runner/, 2023-03-31-Fri.
- Docs Jenkins, https://www.jenkins.io/doc/, 2023-03-31-Fri.
- Azure Pipelines, https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops, 2023-09-11-Mon.
- AWS CI/CD Pipeline, https://aws.amazon.com/getting-started/hands-on/set-up-ci-cd-pipeline/, 2023-09-11-Mon.
- AWS DevOps Pipeline, https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-devops-example.html, 2023-09-11-Mon.
- CI/CD Blog KR, https://llshl.tistory.com/50, 2023-09-11-Mon.
- CI/CD Tools Blog KR, https://ichi.pro/ko/hyeonjae-sayong-ganeunghan-choegoui-ci-cd-dogu-27gaji-194611649728144, 2023-09-11-Mon.
- Jenkins X, https://jenkins-x.io/, 2023-09-11-Mon.
- Jenkins X Blog KR, https://uzihoon.com/post/eabb9930-5f8a-11ea-8839-c791ea9b277c, 2023-09-11-Mon.
- Travis CI, https://www.travis-ci.com/, 2023-09-11-Mon.
- GitHub Actions, https://github.com/features/actions, 2023-09-11-Mon.
- GitHub Actions GitHub, https://github.com/actions, 2023-09-11-Mon.
- Jenkins vs. GitHub Actions Blog KR, https://choseongho93.tistory.com/295, 2023-09-11-Mon.
- Banksalad Blog KR, https://blog.banksalad.com/tech/become-an-organization-that-deploys-1000-times-a-day/?gclid=CjwKCAjw1uiEBhBzEiwAO9B_HV8BhfRxfb0JIyNYevpEnqo6MeCHIrTAeRL4fmvTPeIUqzR3Aurb8BoC_hgQAvD_BwE, 2023-09-11-Mon.
