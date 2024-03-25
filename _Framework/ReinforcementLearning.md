# Reinforcement Learning

---

# :hammer_and_wrench: Frameworks and Libraries :books:

## :books: Acme | [GitHub](https://github.com/google-deepmind/acme) | Google Brain & DeepMind

Acme is a library of reinforcement learning (RL) building blocks that strives to expose simple, efficient, and readable agents. These agents first and foremost serve both as reference implementations as well as providing strong baselines for algorithm performance. However, the baseline agents exposed by Acme should also provide enough flexibility and simplicity that they can be used as a starting block for novel research. Finally, the building blocks of Acme are designed in such a way that the agents can be run at multiple scales (e.g. single-stream vs. distributed agents).

:construction: The last release was on Feb 10, 2022

## :books: [Gym](https://www.gymlibrary.dev/index.html) | [GitHub](https://github.com/openai/gym)

A toolkit for developing and comparing reinforcement learning algorithms.

Gym is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. Since its release, Gym's API has become the field standard for doing this.

:construction: The last release was on Oct 5, 2022.

### Gym Documentation

All development of Gym has been moved to Gymnasium, a new package in the Farama Foundation that's maintained by the same team of developers who have maintained Gym for the past 18 months. If you're already using the latest release of Gym (v0.26.2), then you can switch to v0.27.0 of Gymnasium by simply replacing import gym with import gymnasium as gym with no additional steps. Gym will not be receiving any future updates or bug fixes, and no further changes will be made to the core API in Gymnasium.

Read more about the Farama Foundation and the backstory of the transition from Gym to Gymnasium - Announcing The Farama Foundation: https://farama.org/Announcing-The-Farama-Foundation

### Important Notice

The team that has been maintaining Gym since 2021 has moved all future development to Gymnasium, a drop in replacement for Gym (import gymnasium as gym), and Gym will not be receiving any future updates. Please switch over to Gymnasium as soon as you're able to do so. If you'd like to read more about the story behind this switch, please check out this blog post.

## :books: [Gymnasium](https://gymnasium.farama.org/) | [GitHub](https://github.com/Farama-Foundation/Gymnasium) | OpenAI

Gymnasium is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. This is a fork of OpenAI's Gym library by its maintainers (OpenAI handed over maintenance a few years ago to an outside team), and is where future maintenance will occur going forward.

## :books: [KerasRL](https://keras-rl.readthedocs.io/en/latest/) | [GitHub](https://github.com/keras-rl/keras-rl)

Deep Reinforcement Learning for Keras.

keras-rl implements some state-of-the art deep reinforcement learning algorithms in Python and seamlessly integrates with the deep learning library Keras.

Furthermore, keras-rl works with OpenAI Gym out of the box. This means that evaluating and playing around with different algorithms is easy.

:construction: The last release was on May 1, 2018.

## :books: [Pearl](https://pearlagent.github.io/) | [GitHub](https://github.com/facebookresearch/Pearl)

A Production-ready Reinforcement Learning AI Agent Library.

Pearl is a new production-ready Reinforcement Learning AI agent library open-sourced by the Applied Reinforcement Learning team at Meta. Furthering our efforts on open AI innovation, Pearl enables researchers and practitioners to develop Reinforcement Learning AI agents. These AI agents prioritize cumulative long-term feedback over immediate feedback and can adapt to environments with limited observability, sparse feedback, and high stochasticity. We hope that Pearl offers the community a means to build state-of-the-art Reinforcement Learning AI agents that can adapt to a wide range of complex production environments.

[[2023] Pearl, A Production-ready Reinforcement Learning Agent (arXiv)](https://arxiv.org/pdf/2312.03814.pdf)

[[2023] Pearl, A Production-ready Reinforcement Learning Agent (NIPS)](https://pearlagent.github.io/pearl_detailed_intro.pdf)

Pearl was built with a modular design so that industry practitioners or academic researchers can select any subset and flexibly combine features below to construct a Pearl agent customized for their specific use cases. Pearl offers a diverse set of unique features for production environments, including dynamic action spaces, offline learning, intelligent neural exploration, safe decision making, history summarization, and data augmentation.

Pearl is in progress supporting real-world applications, including recommender systems, auction bidding systems and creative selection.

* Examples
  * [Using DQN and Double DQN in Pearl with different neural network instantiations](https://nbviewer.org/github/facebookresearch/Pearl/blob/main/tutorials/sequential_decision_making/DQN_and_DoubleDQN_example.ipynb)

* [pearl](https://github.com/facebookresearch/Pearl/tree/main/pearl)
* Policy
  * [deep_q_learning.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/policy_learners/sequential_decision_making/deep_q_learning.py)
  * [bootstrapped_dqn.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/policy_learners/sequential_decision_making/bootstrapped_dqn.py)
* Network
  * [q_value_networks.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/neural_networks/sequential_decision_making/q_value_networks.py)
  * [value_networks.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/neural_networks/common/value_networks.py)
  * [utils.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/neural_networks/common/utils.py)
* Agent
  * [pearl_agent.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/pearl_agent.py)
* Learn
  * [policy_learner.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/policy_learners/policy_learner.py)
  * [offline_learning_and_evaluation.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/utils/functional_utils/train_and_eval/offline_learning_and_evaluation.py)
  * [online_learning.py](https://github.com/facebookresearch/Pearl/blob/main/pearl/utils/functional_utils/train_and_eval/online_learning.py)

## :books: [RLlib](https://docs.ray.io/en/latest/rllib/index.html) | [GitHub](https://github.com/ray-project/ray/tree/master/rllib)

Industry-Grade Reinforcement Learning.

RLlib is an open-source library for reinforcement learning (RL), offering support for production-level, highly distributed RL workloads while maintaining unified and simple APIs for a large variety of industry applications. Whether you would like to train your agents in a multi-agent setup, purely from offline (historic) datasets, or using externally connected simulators, RLlib offers a simple solution for each of your decision making needs.

## :books: [Stable-Baselines3](https://stable-baselines3.readthedocs.io/en/master/) | [GitHub](https://github.com/DLR-RM/stable-baselines3)

Stable Baselines3 (SB3) is a set of reliable implementations of reinforcement learning algorithms in PyTorch.

[[2021] Stable-Baselines3, Reliable Reinforcement Learning Implementations (JMLR)](https://jmlr.org/papers/volume22/20-1364/20-1364.pdf)

---

### Reference
- Acme GitHub, https://github.com/google-deepmind/acme, 2024-02-20-Tue.
- Gymnasium, https://gymnasium.farama.org/, 2024-02-20-Tue.
- Gymnasium GitHub, https://github.com/Farama-Foundation/Gymnasium, 2024-02-20-Tue.
- Keras-RL, https://keras-rl.readthedocs.io/en/latest/, 2024-03-04-Mon.
- Keras-RL GitHub, https://github.com/keras-rl/keras-rl, 2024-03-04-Mon.
- Gym Documentation, https://www.gymlibrary.dev/index.html, 2024-03-04-Mon.
- Gym GitHub, https://github.com/openai/gym, 2024-03-04-Mon.
- Pearl, https://pearlagent.github.io/, 2024-03-06-Wed.
- Pearl GitHub, https://github.com/facebookresearch/Pearl, 2024-03-06-Wed.
- RLlib, https://docs.ray.io/en/latest/rllib/index.html, 2024-03-06-Wed.
- RLlib GitHub, https://github.com/ray-project/ray/tree/master/rllib, 2024-03-06-Wed.
- Stable-Baselines3, https://stable-baselines3.readthedocs.io/en/master/, 2024-03-06-Wed.
- Stable-Baselines3 GitHub, https://github.com/DLR-RM/stable-baselines3, 2024-03-06-Wed.
- Using DQN and Double DQN in Pearl with different neural network instantiations, https://nbviewer.org/github/facebookresearch/Pearl/blob/main/tutorials/sequential_decision_making/DQN_and_DoubleDQN_example.ipynb, 2024-03-25-Mon.
