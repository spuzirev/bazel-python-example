load("@io_bazel_rules_docker//container:container.bzl", "container_image")

container_image(
    name = "py385",
    base = "@py385//image",
    symlinks = {
        "/usr/bin/python3": "/usr/local/bin/python",
    },
    visibility = ["//visibility:public"],
)
