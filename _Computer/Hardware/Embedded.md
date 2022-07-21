# Embedded System | [Wiki](https://en.wikipedia.org/wiki/Embedded_system)
- Summary
  - 특정 기능을 위한 시스템이다(일반적인 용도의 PC와 차이가 있다). Dedicated function system (contrast in general personal computer)
  - 시간 제약 조건을 포함한 시스템이 있다(i.e. 자동차 운전 시스템 등의 real-time deadline이 존재하는 시스템). Constraint in time  

An embedded system is a computer system-a combination of a computer processor, computer memory and input/output peripheral devices-that has a dedicated function within a larger mechanical or electronic system. It is embedded as part of a complete device often including eletrical or electronic hardware and mechanical parts. Because an embedded system typically controls physical operations of the machine that it is embedded within, it often has real-time computing constraints. Embedded systems control many devices in common use today. In 2009, it was estimated that ninety-eight percent of all micorprocessors manufactured were used in embedded systems.

Modern embedded systems are often based on microcontrollers (i.e. microprocessors with integrated memory and peripheral interfaces), but ordinary microprocessors (using external chips for memory and peripheral interface circuits) are also common, expecially in more complex systems. In either case, the processor(s) used may be types ranging from general purpose to those specialized in a certain class of computations, or even custom designed for the application at hand. A common standard class of dedicated processors is the digital signal processor (DSP).

Since the embedded system is dedicated to specific tasks, design engineers can optimize it to reduce the size and cost of the product and increase its reliability and performance. Some embedded systems are mass-produced, benefiting from economies of scale.

Embedded systems range in size from portable personal devices such as digital watches and MP3 players to bigger machines like home appliances, industrial assembly lines, robots, transport vehicles, traffic light controllers, and medical imaging systems. Often they constitute subsystems of other machines like avionics in aircraft and spacecraft. Large installations like factories, pipelines and electrical grids rely on multiple embedded systems networked together. Generalized through software customization, embedded systems such as programmable logic controllers frequently comprise their functional units.

Embedded systems range from those law in complexity, with a single microcontroller chip, to very high with multiple units, peripherals and networks, which may reside in equipment racks or across large geographical areas connected via long-distance communications lines.

## [Book: Programming Embedded Systems](https://books.google.co.kr/books?id=nPZaPJrw_L0C&pg=PA1&redir_esc=y&hl=ko#v=onepage&q&f=false)

### What Is an Embedded System?

An embedded system is a combination of computer hardware and software-and perhaps additional parts, either mechanical or electronic-designed to perform a dedicated function. A good example os the microwave oven, Almost every household has one, and tens of millions of them are used every day, but very few people realize that a computer processor and software are involved in the preparation of their lunch or dinner.

The design of an embedded system to perform a dedicated function is in direct contrast to that of the personal computer. It too is comprised of computer hardware and software and mechanical components (disk drives, for example). However, a personal computer is not designed to perform a specific function. Rather, it is able to do many different things. Many people use the term general-purpose computer to make this distinction clear. As shipped, a general-purpose computer is a blank slate; the manufacturer does not know what the customer will do with it. One customer may use if for a network file server, another may use it exclusively for playing games, and a third may use it to write the next great American novel.

Frequently, an embedded system is a component within some larger system. For example, modern cars and trucks contains many embedded systems. One embedded system controls the antilock brakes, another monitors and controls the vehicle’s emissions, and a third displays information on the dashboard. Some luxury car manufacturers have even touted the number of processors (often more than 60, including one in each headlight) in advertisements. In most cases, automotive embedded systems are connected by a communications network.

It is important to point out that a general-purpose computer interfaces to numerous embedded systems. For example, a typical computer has a keyboard and mouse, each of which is an embedded system. These peripherals each contains a processor and software and is designed to perform a specific function. Another example is a modem, which is designed to send and receive digital data over an analog telephone line; that’s all it does. And the specific function of other peripherals can each be summarized in a single sentence as well.

The existence of the processor and software in an embedded system may be unnoticed by a user of the device. Such is the case for a microwave oven, MP3 player, or alarm clock. In some cases, it would even be possible to build a functionally equivalent device that does not contain the processor and software. This could be done by replacing the processor-software combination with a custom integrated circuit (IC) that performs the same functions in hardware. However, the processor and software combination typically offers more flexibility than a hardwired design. It is generally much easier, cheaper, and less poser intensive to use a processor and software in an embedded system.

- History and Future

### Real-Time Systems
One subclass of embedded systems deserves an introduction at this point. A real-time system has timing constraints. The function of a real-time system is thus partly specified in terms of its ability to make certain calculations or decisions in a timely manner. These important calculations or activities have deadlines for completion.

The crucial distinction among real-time systems lies in what happens if a deadline is missed. For example, if the real-time system is part of an airplane’s flight control system, the lives of the passengers and crew may be endangered by a single missed deadline. However, if instead the system involved in satellite communication, the damage could be limited to a single corrupt data packet (which may or may not have catastrophic consequences depending on the application and error recovery scheme). The more severe the consequence, the more likely it will be said that the deadline is “hard” and thus, that the system is a hard real-time system. Real-time systems at the other end of this continuum are said to have “soft” deadlines-a soft real-time system.

- Non-real time ← soft real time → hard real time
    - Computer simulation, User interface, Internet video, Cruise control, Telecommunications, Flight control, Electronic engine

Real-time system design is not simply about speed. Deadlines for real-time systems vary; one deadline might be in a millisecond, while another is an hour away. The main concern for a real-time system is that there is a guarantee that the hard deadlines of the system are always met. In order to accomplish this the system must be predictable.

The architecture of the embedded software, and its interaction with the system hardware, play a key role in ensuring that real-time systems meet their deadlines. Key software design issues include whether polling is sufficient or interrupts should be used, and what priorities should be assigned to the various tasks and interrupts. Additional forethought must go into understanding the worst-case performance requirements of the specific system activities.

All of the topics and examples presented in this book are applicable to the designers of real-time systems. The designer of a real-time system must be more diligent in his work. He must guarantee reliable operation of the software and hardware under all possible conditions. And, to the degree that human lives depend upon the system’s proper execution, this guarantee must be backed by engineering calculations and descriptive paperwork.

## [Book: Embedded System Design](https://books.google.co.kr/books?id=BjNZXwH7HlkC&pg=PA2&redir_esc=y#v=onepage&q&f=false)
- What is an embedded system?

---

### [Bootlin](https://bootlin.com/)

Bootlin is an engineering company specialized in embedded Linux and more generally in Free and OPen Source software for embedded systems.

---

### Reference
- Embedded System Wiki, https://en.wikipedia.org/wiki/Embedded_system, 2022-06-22-Wed.
- Programming Embedded Systems with C and GNU Development Tools 2nd Ed., O’REILLY, 2006, https://books.google.co.kr/books?id=nPZaPJrw_L0C&pg=PA1&redir_esc=y&hl=ko#v=onepage&q&f=false, 2022-06-21-Tue.
- Embedded Systems Design 2nd Ed., Newnes, 2003, https://books.google.co.kr/books?id=BjNZXwH7HlkC&pg=PA2&redir_esc=y#v=onepage&q&f=false, 2022-06-21-Tue.
- bootlin, https://bootlin.com/company/about-us/, 2022-07-21-Thu.
- bootlin, https://bootlin.com/, 2022-07-21-Thu.
