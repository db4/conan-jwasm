import os
from conans import tools, ConanFile, CMake

class JWasmConan(ConanFile):
    name = "jwasm"
    version = "2.12"
    description = "JWasm Masm-compatible assembler"
    url = "http://github.com/db4/conan-jwasm"
    license = "Sybase Open Watcom Public License"
    settings = "os_build", "compiler", "arch", "arch_build"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    def source(self):
        tools.get("https://sourceforge.net/projects/jwasm/files/JWasm%20Source%20Code/JWasm212s_140105.zip")

    def build(self):
        self.settings.arch = self.settings.arch_build
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
        self.info.include_build_settings()
        del self.info.settings.compiler
        del self.info.settings.arch

