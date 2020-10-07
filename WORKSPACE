# rules_python
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    commit = "3baa2660569a76898d0f520c73b299ea39b6374d",
    remote = "https://github.com/bazelbuild/rules_python.git",
    shallow_since = "1599564582 +1000",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip3_import", "pip_repositories")

pip_repositories()

pip3_import(
    name = "requirements",
    requirements = "//:requirements.txt",
)

load("@requirements//:requirements.bzl", "pip_install")

pip_install()

# Docker
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Download the rules_docker repository at release v0.14.4
git_repository(
    name = "io_bazel_rules_docker",
    commit = "faaa10a72fa9abde070e2a20d6046e9f9b849e9a",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    shallow_since = "1592582964 -0400",
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load("@io_bazel_rules_docker//repositories:pip_repositories.bzl", "pip_deps")

pip_deps()

load(
    "@io_bazel_rules_docker//python3:image.bzl",
    py3_image_repositories = "repositories",
)

py3_image_repositories()

load("@io_bazel_rules_docker//container:container.bzl", "container_pull")

container_pull(
    name = "py385",
    digest = "sha256:675ca1005d35edfb6f324e7211110cad6d1247c7b945c738b7b549f46a608a79",
    registry = "index.docker.io",
    repository = "library/python",
    tag = "3.8.5-buster",
)
