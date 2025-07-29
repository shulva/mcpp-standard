add_includedirs(".")

if is_host("windows") then
    set_encodings("source:utf-8", "target:utf-8")
end

target("00-0-hello-mcpp")
    set_languages("cxx11")
    add_files("hello-mcpp.cpp")

includes("cpp11")
