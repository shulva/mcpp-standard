set_languages("cxx11")

-- target: cpp11-00-auto-and-decltype

target("cpp11-00-auto-and-decltype")
    set_kind("binary")
    add_files("00-auto-and-decltype-0.cpp")
target("cpp11-00-auto-and-decltype-1")
    set_kind("binary")
    add_files("00-auto-and-decltype-1.cpp")
target("cpp11-00-auto-and-decltype-2")
    set_kind("binary")
    add_files("00-auto-and-decltype-2.cpp")
target("cpp11-00-auto-and-decltype-3")
    set_kind("binary")
    add_files("00-auto-and-decltype-3.cpp")
target("cpp11-00-auto-and-decltype-4")
    set_kind("binary")
    add_files("00-auto-and-decltype-4.cpp")

-- target: cpp11-01-default-and-delete

target("cpp11-01-default-and-delete-0")
    set_kind("binary")
    add_files("01-default-and-delete-0.cpp")

target("cpp11-01-default-and-delete-1")
    set_kind("binary")
    add_files("01-default-and-delete-1.cpp")

target("cpp11-01-default-and-delete-2")
    set_kind("binary")
    add_files("01-default-and-delete-2.cpp")

-- target: cpp11-02-final-and-override

target("cpp11-02-final-and-override-0")
    add_files("02-final-and-override-0.cpp")

target("cpp11-02-final-and-override-1")
    add_files("02-final-and-override-1.cpp")

target("cpp11-02-final-and-override-2")
    add_files("02-final-and-override-2.cpp")

-- target: cpp11-03-trailing-return-type

target("cpp11-03-trailing-return-type")
    add_files("03-trailing-return-type.cpp")

-- target: cpp11-04-rvalue-references

target("cpp11-04-rvalue-references")
    set_optimize("none")
    add_cxflags("-fno-elide-constructors")
    add_cxxflags("-fno-elide-constructors")
    add_files("04-rvalue-references.cpp")