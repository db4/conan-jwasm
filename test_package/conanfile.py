from conans import ConanFile, CMake, tools, RunEnvironment
import os

class JWasmTestConan(ConanFile):
    def test(self):
        if not tools.cross_building(self.settings):
            self.run("jwasm -coff %s" % os.path.join(self.source_folder, "test32.asm"))
