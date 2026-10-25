from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Reina_Hani"
version = "0.1"


@init
def initialize(project):
    project.set_property("name", "calculator_Reina_Hani")
    project.set_property("version", "0.1")
    project.set_property("default_task", "publish")
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Reina_Hani")
    project.set_property("unittest_module_glob", "test_*")
