load("@rules_python//python:defs.bzl", "py_binary")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@requirements//:requirements.bzl", "requirement")

py_binary(
    name = "cli",
    srcs = [":main.py"],
    main = "main.py",
    deps = [
        requirement("click"),
    ],
)

py3_image(
    name = "cli-image",
    srcs = ["main.py"],
    base = "//:py385",
    main = "main.py",
    deps = [
        requirement("click"),
    ],
)
