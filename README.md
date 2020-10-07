# bazel-python-example

This repo contains just an example of simple hello-world app written in python built and packaged into docker image by bazel.

## Run
* `bazel run //cli:cli` will run the app with your local python
* `bazel run //cli:cli-image` will build a docker image, load it into your docker daemon and run it inside.

## Special notes
This example does not use distroless python since it has only Python 3.7. Instead of that standard python image from dockerhub is used. If you prefer to use distroless python you can remove `base = "//:py385` line from cli/BUILD.

## Links
* https://docs.bazel.build/versions/master/be/python.html
* https://github.com/bazelbuild/rules_docker
* https://thethoughtfulkoala.com/posts/2020/05/16/bazel-hermetic-python.html
