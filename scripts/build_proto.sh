root=$(git rev-parse --show-toplevel)

docker build -t protogen ${root}/scripts/build_proto_env
docker run -v ${root}:/import protogen
