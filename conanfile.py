import os
from conans import tools, ConanFile, CMake

class JWasmConan(ConanFile):
    name = "jwasm"
    version = "2.12"
    description = "JWasm Masm-compatible assembler"
    url = "http://github.com/db4/conan-jwasm"
    license = "Sybase Open Watcom Public License"
    settings = "os", "compiler", "os_build", "arch", "arch_build"
    # if os is not defined, conan passes CMAKE_SYSTEM_NAME="Generic"
    # no cmake during x86_64 -> x86 cross building and cmake
    # fails to configure Visual Studio project correctly
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    def source(self):
        tools.get("https://sourceforge.net/projects/jwasm/files/JWasm%20Source%20Code/JWasm212s_140105.zip")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = "Release"
        cmake.configure()
        cmake.build(args=["--config", "Release"])

    def package(self):
        self.copy("License.txt")
        self.copy("*", dst="bin", src="bin")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        os = self.info.settings.os
        arch = self.info.settings.arch
        del self.info.settings.os
        del self.info.settings.compiler
        del self.info.settings.arch
        self.info.settings.os_build = os
        self.info.settings.arch_build = arch

