# _Architecture_

## 32

### i386

### mips

### mipsel

### x86

## 64

### i686

### amd64

### mips64el

### s390x

## ARM

### armel

## Power

### ppc64el

## Debian on arm

- The ARM EABI (armel) port targets a range of older 32-bit ARM devices, particularly those used in NAS hardware and a variety of *plug computers.
- The newer ARM hard-float (armhf) port supports newer, more powerful 32-bit devices using version 7 of the ARM architecture specification.
- The 64-bit ARM (arm64) port supports the latest 64-bit ARM-powered devices.
  - known in some other places as AArch64.
  - This port was released for the first time with Jessie (Debian 8).
  - 'arm64' is the Debian port name for the 64-bit Armv8 architecture, referred to as 'aarch64' in upstream toolchains (GNU triplet aarch64-linux-gnu), and some other distros.
  - The port was started in 2010 (by Arm and Linaro working with the community in commendable fashion) long before hardware was available so that there would be something to run when it arrived.
  - Hardware started to becoming available in October 2013, but access was restricted. Debian was very kindly donated two 8-core APM machines, installed in March 2014 running two buildds in Debian-ports. One was split with xen so we also had an unofficial porterbox. Arm supplied two Junos in August 2014, and Linaro 3 APM boxes in October, which are the current official build and porter machines.

---

### [Microservice Architecture](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices)

A microserfice architecture consists of a collection of small, autonomous services. Each service is self-contained and should implement a single business capability within a bounded context. A bounded context is a natural division within a business and provides an explicit boundary within which a domain model exists.

What are microservices?
* Microservices are small, independent, and loosely coupled. A single small team of developers can write and maintain a service.
* Each service is a separate codebase, which can be managed by a small development team.
* Services can be deployed independently. A team can update an existing service without rebuilding and redeploying the entire application.
* Services are responsible for persisting their own data or external state. This differs from the traditional model, where a separate data layer handles data persistence.
* Services communicate with each other by using well-defined APIs. Internal implementation details of each service are hidden from other services.
* Supports ployglot programming. For example, services don't need to share the same technology stack, libraries, or frameworks.

Benefits:
* Agility
* Small, focused teams
* Small code base
* Mix of technologies
* Fault isolation
* Scalability
* Data isolation

Challenges
* Complexity: A microservices application has more moving parts than the equivalent monolithic application. Each service is simpler, but the entire system as a whole is more complex.
* Development and testing: Writing a small service that relies on other dependent services requires a different approach than writing a traditional monolithic or layered application. Existing tools are not always designed to work with service dependencies. Refactoring across service boundaries can be difficult. It is also challenging to test service dependencies, especially when the application is evolving quickly.
* Lack of governance: The decentralized approach to building microservices has advantages, but it can also lead to problems. You might end up with so many different languages and frameworks that the application becomes hard to maintain. It might be useful to put some project-wide standards in place, without overly restricting teams' flexibility. This especially applies to cross-cutting functionality such as logging.
* Network congestion and latency: The use of many small, granular services can result in more interservice communication. Also, if the chain of service dependencies get too long (service A calls B, which calls C...), the additional latency can become a problem. You will need to design APIs carefully. Avoid overly chatty APIs, think about serialization formats, and look for places to use asynchronous communication patterns like queue-based load leveling.
* Data integrity: With each microservice responsible for its own data persistence. As a result, data consistency can be a challenge. Embrace eventual consistency where possible.
* Management: To be successful with microservices requires a mature DevOps culture. Correlated logging across services can be challenging. Typically, logging must correlate multiple service calls for a single user operation.
* Versioning: Updates to a service must not break services that depend on it. Multiple services could be updated at any given time, so without careful design, you might have problems with backward or forward compatibility.
* Skill set: Microservices are highly distributed systems. Carefully evaluate whether the team has the skills and experience to be successful.

---

### Reference
- debian ARM Ports, https://www.debian.org/ports/arm/, 2022-08-05-Fri.
- Microservice Architecture Azure, https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices, 2023-12-12-Tue.
