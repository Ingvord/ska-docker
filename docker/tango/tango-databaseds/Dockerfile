ARG DOCKER_REGISTRY_USER
ARG DOCKER_REGISTRY_HOST
FROM ${DOCKER_REGISTRY_HOST}/${DOCKER_REGISTRY_USER}/tango-libtango:latest

ENTRYPOINT ["/usr/local/bin/DataBaseds"]

CMD ["2", "-ORBendPoint", "giop:tcp::10000"]

