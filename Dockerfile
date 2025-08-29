ARG PYTHON_VERSION=3.13-alpine
ARG ANSIBLE_VERSION=11.9.0

FROM python:${PYTHON_VERSION}
ARG ANSIBLE_VERSION
RUN apk add --no-cache bash curl sshpass openssh-client ; \
    pip install ansible==${ANSIBLE_VERSION} passlib ansible-lint ansible-review yamllint; \
    pip cache purge && rm -rf /var/cache/apk/* ; \
    #&& \
    cd /usr/local/lib/python3.13/site-packages/ansible_collections/ && \
    rm -rf fortinet cisco dellemc netapp f5networks azure arista junipernetworks \
           vyos ovirt purestorage vmware inspur netapp_eseries amazon openstack \
           ngine_io awx theforeman check_point ibm wti sensu t_systems_mms \
           mellanox hetzner chocolatey cloudscale_ch frr infinidat netbox \
           servicenow vultr cloud cyberark gluster hpe infoblox lowlydba \
           openvswitch splunk google && \
    cd community/ && \
    rm -rf aws vmware azure zabbix windows mongodb fortios postgresql \
           digitalocean okd grafana mysql microsoft telekom_mms

RUN echo "Host *\n    StrictHostKeyChecking no\n    UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config
#RUN mkdir -p /opt/proxmox && chmod 755 /opt/proxmox
WORKDIR /opt/proxmox
CMD ["bash", "-c", "chmod -R 755 /opt/proxmox && /bin/bash"] 

#ansible-lint yamllint pyOpenSSL pyyaml jmespath passlib