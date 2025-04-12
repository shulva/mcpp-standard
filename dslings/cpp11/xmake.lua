set_languages("cxx11")

-- target: cpp11-00-auto-and-decltype

target("cpp11-00-auto-and-decltype")
    set_kind("binary")
    add_files("00-auto-and-decltype.cpp")
target("cpp11-00-auto-and-decltype-x")
    set_kind("binary")
    add_files("00-auto-and-decltype.x.cpp")
target("cpp11-00-auto-and-decltype-y")
    set_kind("binary")
    add_files("00-auto-and-decltype.y.cpp")
target("cpp11-00-auto-and-decltype-z")
    set_kind("binary")
    add_files("00-auto-and-decltype.z.cpp")

-- target: cpp11-01-default-and-delete

target("cpp11-01-default-and-delete")
    set_kind("binary")
    add_files("01-default-and-delete.cpp")