ARG BASE_IMAGE=alpine:latest
FROM ${BASE_IMAGE}

RUN \
    apk \
        update \
    && \
    apk \
        add \
            wine \
    && \
        ln -s \
            /usr/bin/wine64 \
            /usr/bin/wine

ARG WINE_GROUP_ID=1000
ARG WINE_GROUP_NAME=whiners
ARG WINE_USER_ID=1000
ARG WINE_USER_NAME=main

RUN \
    addgroup \
        -g ${WINE_GROUP_ID} \
        ${WINE_GROUP_NAME} \
    && \
    adduser -D \
        -G \
            ${WINE_GROUP_NAME} \
        -u \
            ${WINE_USER_ID} \
        -h \
            /home/${WINE_USER_NAME} \
        ${WINE_USER_NAME} \
    && \
    mkdir -p \
        /home/${WINE_USER_NAME}/wine/source \
    && \
    mkdir -p \
        /home/${WINE_USER_NAME}/wine/target \
    && \
    mkdir -p \
        /home/${WINE_USER_NAME}/wine/prefix \
    && \
    chown

RUN \
    chmod -R \
        ${WINE_USER_NAME}:${WINE_GROUP_NAME} \
        /home/${WINE_USER_NAME}/wine

USER ${WINE_USER_NAME}
WORKDIR /home/${WINE_USER_NAME}/wine

ENTRYPOINT [ /home/${WINE_USER_NAME}/loader.py ]
