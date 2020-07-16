# [TensorFlow](https://www.tensorflow.org/) [GitHub](https://github.com/tensorflow/tensorflow)
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchs push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organiztion to conduct machine learning and deep nural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranted backward compatible API for other languages. [Ref]

## [Bazel](https://www.bazel.build/) [Wiki (KOR)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) [GitHub](https://github.com/bazelbuild/bazel)
Basel is an open source tool that enables software build and test automation. Google used and built Blaze, a build tool internally, and released and released part of the Blaze tool with Bazel, named Blaze's anagram. Bazel was first released in March 2015 and was beta tested until September 2015.

Similar to build tools like Make, Apache Ant, or Apache Maven, Bazel uses a set of rules to build application software from source code. Rules and macros are written in the Skylark language, a subset of Python. There are basic rules for writing software written in Java, C, C++, Python, Objective-C and Bourne shell script programming languages. Bazel can create application software packages suitable for distribution for Android and iOS operating systems.

When designing Bazel, we focused on build speed, accuracy and reproducibility. This tool uses parallelism to accelerate parts of the build process. Includes Bazel Query language that can be used to analyze build dependencies in complex build graphs.[Ref]

### [Starlark Language](https://docs.bazel.build/versions/2.0.0/skylark/language.html) [GitHub](https://github.com/bazelbuild/starlark)
Starlark (formerly known as Skylark) is a language intended for use as a configuration language. It was designed for the Bazel build system, but may be useful for other projects as well. This repository is where Starlark features are proposed, discussed, and specified. It contains information about the language, including the specification. There are multiple implementations of Starlark.

Starlark is a dialect of Python. Like Python, it is a dynamically typed language with high-level data types, first-class functions with lexical scope, and garbage collection. Independent Starlark threads execute in parallel, so Starlark workloads scale well on parallel machines. Starlark is a small and simple language with a familiar and highly readable syntax. You can use it as an expressive notation for structured data, defining functions to eliminate repetition, or you can use it to add scripting capabilities to an existing application.

A Starlark interpreter is typically embedded within a larger application, and the application may define additional domain-specific functions and data types beyond those provided by the core language. For example, Starlark was originally developed for the Bazel build tool. Bazel uses Starlark as the notation both for its BUILD files (like Makefiles, these declare the executables, libraries, and tests in a directory) and for its macro language, through which Bazel is extended with custom logic to support new languages and compilers.[Ref]


#### Reference
- TensorFlow GitHub, https://github.com/tensorflow/tensorflow, 2020-07-16-Thu.
- Bazel, https://www.bazel.build/, 2020-07-16-Thu.
- Bazel wiki, https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- Bazel GitHub, https://github.com/bazelbuild/bazel, 2020-07-16-Thu.
- Starlark GitHub, https://github.com/bazelbuild/starlark, 2020-07-16-Thu.
