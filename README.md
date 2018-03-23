# conan-jwasm

[Conan.io](https://conan.io) package for [JWasm Masm-compatible assembler](https://sourceforge.net/projects/jwasm/)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-jwasm?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-jwasm)|[![Build Status](https://travis-ci.org/db4/conan-jwasm.svg?branch=master)](https://travis-ci.org/db4/conan-jwasm)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload jwasm/2.12@dbely/stable --all

## Reuse the packages

### Basic setup

    $ conan install jwasm/2.12@dbely/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    jwasm/2.12@dbely/stable

    [generators]
    txt
    cmake


