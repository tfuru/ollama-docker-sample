ARG FEDORA_VERSION=40
FROM fedora:$FEDORA_VERSION
USER 0

RUN dnf update -y \
    && dnf clean all \
    && dnf install -y curl

# install patched mesa driver for GPU remoting and some tools
RUN dnf -y install dnf-plugins-core \
 && dnf -y install dnf-plugin-versionlock \
 && dnf -y install mesa-vulkan-drivers vulkan-loader-devel vulkan-headers vulkan-tools\
 && dnf -y copr enable slp/mesa-krunkit fedora-40-aarch64 \
 && dnf -y downgrade mesa-vulkan-drivers.aarch64 — repo=copr:copr.fedorainfracloud.org:slp:mesa-krunkit \
 && dnf versionlock mesa-vulkan-drivers \
 && dnf update -y \
 && dnf clean all \
 && rm -rf /var/cache/dnf

RUN curl -fsSL https://ollama.com/install.sh | sh

ENV XDG_RUNTIME_DIR=/tmp
ENV OLLAMA_DEBUG=true
ENV OLLAMA_HOST=0.0.0.0:11434
ENV OLLAMA_GPU_LAYERS=-1

EXPOSE 11434
CMD ["ollama","serve"]