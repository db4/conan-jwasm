from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if platform.system() == "Windows":
        builder.add({"os_build": "Windows", "arch_build": "x86"})
        builder.add({"os_build": "Windows", "arch_build": "x86_64"})
    else:
        builder.add()
    builder.run()
