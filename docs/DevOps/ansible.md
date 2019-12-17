# Ansible

## Intro

- Ansible is an open source tool that enables autoamtion, configuration and orchestration of infrastructure. Helps in:
    - Automation of app deployment
    - Manage multi server systems
    - Reduce complexity
- When using Ansible, we build out the entire system in code and store the code in source control. Rollbacks will be available when needed and the code can be shared with other team members. 
- Produces reliable and repeatable systems and reduces human error in spinning up the infrastructure multiple times. 
- Written in `Python` and the scripting language used is YAML. 
- Commands are sent to nodes (in parallel) via `SSH` and executed sequentially on each respective node.
- Ansible can be used in:
    - *Mass deployments*
    - As a configuration management tool to ensure identical environments when *scaling* to meet demands (during high spikes of traffic)
    - *Migrating environments* from integration, testing and production in a reliable and dependable way. 
    - *Failure prevention* - As a tool for reviewing change logs and rolling back applications if failures do occur.

![Ansible is better](img/ansible-better.png)


## Setup inventory machines

- Create sandbox servers that will need to be configured and managed.
- Inventory, child and node servers naming can be used interchangeably.
- These are the servers we will configure using Ansible.
- Can create 3 VMs using [this](src/setup-env.yml) template.


## Install Ansible

Ansible can be installed via pip.
```bash
    $ sudo pip3 install ansible
    $ ansible --version
        ansible 2.9.2
        config file = None
        configured module search path = ['~/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
        ansible python module location = /usr/local/lib/python3.7/site-packages/ansible
        executable location = /usr/local/bin/ansible
        python version = 3.7.5 (default, Nov  1 2019, 02:16:23) [Clang 11.0.0 (clang-1100.0.33.8)]
```

To check that the control machine (Laptop) has access to the node VMs, we can SSH into those systems and confirm access to the machines. 

```bash
    $ ssh -i ~/.ssh/ansible-2020.pem ec2-user@54.152.194.112
    $ ssh -i ~/.ssh/ansible-2020.pem ec2-user@3.211.181.182
    $ ssh -i ~/.ssh/ansible-2020.pem ec2-user@54.89.101.67
```


## Setup inventory file

- Ansible must be given information on the inventory servers before we can execute commands on the node machines.
- The file can either be static or dynamic.
    - **Static inventory file:** [Create](src/hosts-dev) an `inventory file` containing the node/inventory server information. This file lists the hostnames and groups. 
        ```bash
        # hosts-dev

        [webservers]
        54.152.194.112
        3.211.181.182

        [loadbalancers]
        lb ansible_host=54.89.101.67

        [local] 
        control ansible_connection=local
        # above 2 lines code is the way Ansible communicates back to the control host. Also, this tells Ansible not to SSH into it as it is the localhost
        ```
    - **[Dynamic inventory file:](https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html)** If you use Amazon Web Services EC2, maintaining an inventory file might not be the best approach, because hosts may come and go over time, be managed by external applications, or you might even be using AWS autoscaling. For this reason, you can use the [EC2 external inventory](https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py) script. You can use this script in one of two ways: 
        - The easiest is to use Ansible’s `-i` command line option and specify the path to the script after marking it executable:
            ```bash
                $ ansible -i ec2.py -u ubuntu us-east-1d -m ping
            ```
        - The second option is to copy the script to `/etc/ansible/hosts` and `chmod +x` it. You must also copy the ec2.ini file to `/etc/ansible/ec2.ini`. Then you can run ansible as you would normally.
- The inventory file can include inventory specific parameters like non-standard SSH port numbers or aliases using `<name> ansible_host=<IP address>`.
- Default Ansible inventory is located in `/etc/ansible/hosts`
- Reference a different inventory by using `-i <path>` in CLI.
    ```bash
    $ ansible --list-hosts all -i hosts-dev 
    hosts (4):
        54.152.194.112
        3.211.181.182
        lb
        control
    ```


## Ansible Configuration

We might need to configure our local Ansible environment with global [specific properties](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings) associated with our setup.
- This can be done by creating a configuration file (ansible.cfg) to control the local Ansible environmental settings. 
- Configuration file will search in the following order:
    - `ANSIBLE_CONFIG` (environment variable if set)
    - `ansible.cfg` (in the current directory)
    - `~/.ansible.cfg` (in the home directory)
    - `/etc/ansible/ansible.cfg` (in the default ansible directory)
- The ansible.cfg file contains important information like the location of the inventory file, default SSH key to use, default remote users to use with SSH and more.

[Patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html) can be used to targeted hosts and groups. Here are some examples:
```bash
$ ansible --list-hosts all
    hosts (4):
        app1
        app2
        lb
        control
$ ansible --list-hosts app*
    hosts (2):
        app1
        app2
$ ansible --list-hosts "*"
    hosts (4):
        app1
        app2
        lb
        control
$ ansible --list-hosts webservers:loadbalancers
    hosts (3):
        app1
        app2
        lb
$ ansible --list-hosts \!control
    hosts (3):
        app1
        app2
        lb
$ ansible --list-hosts webservers:\!app1
    hosts (1):
        app2
$ ansible --list-hosts webservers[0]
    hosts (1):
        app1
```


## Ansible Tasks

- Tasks are a way to run adhoc commands against our inventory in a one-line single executable. 
- Tasks are the basic building blocks of Ansible's execution and configuration. 
- Running `AdHoc commands` are great for troubleshooting and quick testing against the inventory.
- [Ansible modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)
- [Ansible command](https://docs.ansible.com/ansible/latest/cli/ansible.html)
- Commands consist of command, options and host-pattern. As the remote user and other configuration settings are not specified, it will result in ping failure. 
    ```bash 
        $ ansible options <host-pattern> 
        $ ansible -m ping all
        # ansible <module-flag> <module-name> <inventory>

            app1 | UNREACHABLE! => {
            "changed": false,
            "msg": "Failed to connect to the host via ssh: pradeepgorthi@54.152.194.112: Permission denied (publickey).",
            "unreachable": true
        }
        app2 | UNREACHABLE! => {
            "changed": false,
            "msg": "Failed to connect to the host via ssh: pradeepgorthi@3.211.181.182: Permission denied (publickey).",
            "unreachable": true
        }
        lb | UNREACHABLE! => {
            "changed": false,
            "msg": "Failed to connect to the host via ssh: pradeepgorthi@54.89.101.67: Permission denied (publickey).",
            "unreachable": true
        }

        control | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python"
            },
            "changed": false,
            "ping": "pong"
        }
    ```
- The results returned will give the important information about the execution on the end hosts.
- After adding the `remote_user`, `private_key_file` and `host_key_checking` information in ansible.cfg file, the pings are successful as it now knows which user and ssh keypair to use when logging in.
    ```bash
    $ ansible -m ping all 

        control | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python"
            },
            "changed": false,
            "ping": "pong"
        }

        lb | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python"
            },
            "changed": false,
            "ping": "pong"
        }
        
        app1 | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python"
            },
            "changed": false,
            "ping": "pong"
        }
        
        app2 | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python"
            },
            "changed": false,
            "ping": "pong"
    }
    ```

- We can run shell commands using the following:
    ```bash
    $ ansible -m shell -a "uname" webservers:loadbalancers

        app1 | CHANGED | rc=0 >>
        Linux

        app2 | CHANGED | rc=0 >>
        Linux

        lb | CHANGED | rc=0 >>
        Linux
        # rc translates to Return code which is 0 -> successful.
        # As a command ran on the remote node, status is shown as CHANGED.
    ```

## Playbooks 

- Playbooks are a way to combine ordered processess and manage configuration needed to build out a remote system. 
- Makes configuration management easy and gives us the ability to deploy a multi-machine setup.
- Playbooks can declare configurations and orchestrate steps and can ensure our remote system is configured as expected when run. 
- The written tasks in playbook can be run synchronously or asynchronously.
- Gives us the ability to infra as code and manage in source control. 


To contruct a system using playbooks:
- Package Management - packages the system needs.
    - package manager
    - patching
    - Example playbook:
    ```yaml
    ---
      - hosts: loadbalancers
        tasks:
        - name: Install apache
          yum: name=httpd state=latest
    ```
- Configuration - configure the system with necessary application files/configuration files needed.
    - copy files or folders from control machine to nodes
    - edit configuration files
    - Example playbook:
    ```yaml
    ---
      - hosts: loadbalancers
        tasks:
        - name: Copy config file
          copy: src=./config.cfg dest=/etc/config.cfg
        
      - hosts: webservers
        tasks:
        - name: Sync folders
          synchronize: src=./app dest=/var/www/html/app
    ```
- Service Handlers - we can create service handlers to start, stop or restart out system when changes are made. 
    - command
    - service
    - handlers
    - Example playbook:
    ```yaml
    ---
      - hosts: loadbalancers
        tasks:
        - name: Configure port number
          lineinfile: path=/etc/config.cfg regexp='^port' line='port=80'
          notify: Restart apache
    # apache will be restarted only if the line is changed to port=80
        handlers:
        - name: Restart apache
          service: name=httpd status=restarted
    
    ```

To do `yum update`:
```yaml
# yum-update.yml

---
  - hosts: webservers:loadbalancers
    become: true # to become sudo
    tasks:
      - name: Updating yum packages
        yum: name=* state=latest
```

To install `apache` and `php`:
```yaml
# install-services.yml

---
# install-services.yml

---
  - hosts: loadbalancers
    become: true
    tasks:
      - name: Installing apache
        yum: name=httpd state=present # It will check the system to see if apache is already installed, if it is nothing will be done and if it is not, apache will be installed.
      - name: Ensure apache starts
        service: name=httpd state=started enabled=yes

  - hosts: webservers
    become: true
    tasks:
      - name: Installing services
        yum: 
          name:
            - httpd
            - php
          state: present
      - name: Ensure apache starts
        service: 
          name: httpd 
          state: started # start httpd service
          enabled: yes # to configure it to start on every boot
```

```bash
$ ansible-playbook playbooks/install-services.yml 

PLAY [loadbalancers] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [lb]

TASK [Installing apache] *******************************************************************************************************************************************************
ok: [lb]

TASK [Ensure apache starts] ****************************************************************************************************************************************************
changed: [lb]

PLAY [webservers] **************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [app1]
ok: [app2]

TASK [Installing services] *****************************************************************************************************************************************************
ok: [app1]
ok: [app2]

TASK [Ensure apache starts] ****************************************************************************************************************************************************
changed: [app1]
changed: [app2]

PLAY RECAP *********************************************************************************************************************************************************************
app1                       : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
app2                       : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
lb                         : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

To upload files to node servers:

```yaml
# setup-app.yml

---
  - hosts: webservers
    become: true
    tasks:
      - name: Upload index file
        copy: 
          src: ../index.php
          dest: /var/www/html
          mode: 0755

      - name: Configure php.ini file
        lineinfile: # Change a line in a config file matching the regex to the line value.
          path: /etc/php.ini
          regexp: ^short_open_tag
          line: 'short_open_tag=Off'
        notify: restart-apache
      
      # restart apache
    handlers:  # Declaring restart apache task as a handler and adding notify in configure task.
      - name: restart-apache
        service: 
          name: httpd 
          state: restarted
```

Load balance playbook using the template file:
```yaml
# setup-lb.yml

---
  - hosts: loadbalancers
    become: true
    tasks: 
      - name: Creating template
        template: 
          src: ../config/lb-config.j2
          dest: /etc/httpd/conf.d/lb.conf
          owner: bin
          group: wheel
          mode: 064
        notify: restart apache
    
    handlers:  # Declaring restart apache task as a handler and adding notify in configure task.
      - name: restart apache
        service: name=httpd state=restarted
```
Template file to be used by Ansible to dynamically configure the Loadbalancer:
```jinja
# Loadbalancer config that can be read by Ansible is written in Jinja2

ProxyRequests off
<Proxy balancer://webcluster >
  {% for hosts in groups['webservers'] %}
    BalancerMember http://{{hostvars[hosts]['ansible_host']}}
  {% endfor %}
    ProxySet lbmethod=byrequests
</Proxy>
```

Running all playbooks in a single file from start to finish for a cleaner approach.

```yaml
# all-playbooks.yml

---
  - import_playbook:  yum-update.yml
  - import_playbook:  install-services.yml
  - import_playbook:  setup-app.yml
  - import_playbook:  setup-lb.yml
```

To check status of httpd service:

```yaml
# check-status.yml

---
  - hosts: webservers:loadbalancers
    become: true
    tasks:
      - name: Check apache status
        command: service httpd status
```

Ansible provides variables and metadata about the host that we interact with when running playbooks. 
- During the TASK[Gathering facts] step, variables get populated. 
- Gathers useful facts about the host and can be used in playbooks. 
- Use the `status` module to see all of the facts gathered during TASK[Gathering facts] step.
- Uses jinja2 templating to evaluate these expressions. 

- Example Adhoc command:
    ```bash
        $ ansible -m setup app1 
    # Gives all the variables associated with it and we can use them in playbooks
    ```

??? "$ ansible -m setup app1"
    ```json
        app1 | SUCCESS => {
            "ansible_facts": {
                "ansible_all_ipv4_addresses": [
                    "172.31.94.190"
                ],
                "ansible_all_ipv6_addresses": [
                    "fe80::10f3:50ff:fea3:9151"
                ],
                "ansible_apparmor": {
                    "status": "disabled"
                },
                "ansible_architecture": "x86_64",
                "ansible_bios_date": "08/24/2006",
                "ansible_bios_version": "4.2.amazon",
                "ansible_cmdline": {
                    "console": "ttyS0",
                    "nvme_core.io_timeout": "4294967295",
                    "root": "LABEL=/",
                    "selinux": "0"
                },
                "ansible_date_time": {
                    "date": "2019-12-17",
                    "day": "17",
                    "epoch": "1576552252",
                    "hour": "03",
                    "iso8601": "2019-12-17T03:10:52Z",
                    "iso8601_basic": "20191217T031052467561",
                    "iso8601_basic_short": "20191217T031052",
                    "iso8601_micro": "2019-12-17T03:10:52.467633Z",
                    "minute": "10",
                    "month": "12",
                    "second": "52",
                    "time": "03:10:52",
                    "tz": "UTC",
                    "tz_offset": "+0000",
                    "weekday": "Tuesday",
                    "weekday_number": "2",
                    "weeknumber": "50",
                    "year": "2019"
                },
                "ansible_default_ipv4": {
                    "address": "172.31.94.190",
                    "alias": "eth0",
                    "broadcast": "172.31.95.255",
                    "gateway": "172.31.80.1",
                    "interface": "eth0",
                    "macaddress": "12:f3:50:a3:91:51",
                    "mtu": 9001,
                    "netmask": "255.255.240.0",
                    "network": "172.31.80.0",
                    "type": "ether"
                },
                "ansible_default_ipv6": {},
                "ansible_device_links": {
                    "ids": {},
                    "labels": {
                        "xvda1": [
                            "\\x2f"
                        ]
                    },
                    "masters": {},
                    "uuids": {
                        "xvda1": [
                            "1ade993f-5854-45a8-ae15-3d49e5fcbe67"
                        ]
                    }
                },
                "ansible_devices": {
                    "xvda": {
                        "holders": [],
                        "host": "",
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {
                            "xvda1": {
                                "holders": [],
                                "links": {
                                    "ids": [],
                                    "labels": [
                                        "\\x2f"
                                    ],
                                    "masters": [],
                                    "uuids": [
                                        "1ade993f-5854-45a8-ae15-3d49e5fcbe67"
                                    ]
                                },
                                "sectors": "16773087",
                                "sectorsize": 512,
                                "size": "8.00 GB",
                                "start": "4096",
                                "uuid": "1ade993f-5854-45a8-ae15-3d49e5fcbe67"
                            }
                        },
                        "removable": "0",
                        "rotational": "0",
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": "noop",
                        "sectors": "16777216",
                        "sectorsize": "512",
                        "size": "8.00 GB",
                        "support_discard": "0",
                        "vendor": null,
                        "virtual": 1
                    }
                },
                "ansible_distribution": "Amazon",
                "ansible_distribution_file_parsed": true,
                "ansible_distribution_file_path": "/etc/system-release",
                "ansible_distribution_file_variety": "Amazon",
                "ansible_distribution_major_version": "2018",
                "ansible_distribution_release": "NA",
                "ansible_distribution_version": "NA",
                "ansible_dns": {
                    "nameservers": [
                        "172.31.0.2"
                    ],
                    "options": {
                        "attempts": "5",
                        "timeout": "2"
                    },
                    "search": [
                        "ec2.internal"
                    ]
                },
                "ansible_domain": "ec2.internal",
                "ansible_effective_group_id": 500,
                "ansible_effective_user_id": 500,
                "ansible_env": {
                    "AWS_AUTO_SCALING_HOME": "/opt/aws/apitools/as",
                    "AWS_CLOUDWATCH_HOME": "/opt/aws/apitools/mon",
                    "AWS_ELB_HOME": "/opt/aws/apitools/elb",
                    "AWS_PATH": "/opt/aws",
                    "EC2_AMITOOL_HOME": "/opt/aws/amitools/ec2",
                    "EC2_HOME": "/opt/aws/apitools/ec2",
                    "HOME": "/home/ec2-user",
                    "JAVA_HOME": "/usr/lib/jvm/jre",
                    "LANG": "en_US.UTF-8",
                    "LESSOPEN": "||/usr/bin/lesspipe.sh %s",
                    "LESS_TERMCAP_mb": "\u001b[01;31m",
                    "LESS_TERMCAP_md": "\u001b[01;38;5;208m",
                    "LESS_TERMCAP_me": "\u001b[0m",
                    "LESS_TERMCAP_se": "\u001b[0m",
                    "LESS_TERMCAP_ue": "\u001b[0m",
                    "LESS_TERMCAP_us": "\u001b[04;38;5;111m",
                    "LOGNAME": "ec2-user",
                    "MAIL": "/var/mail/ec2-user",
                    "PATH": "/usr/local/bin:/bin:/usr/bin:/opt/aws/bin",
                    "PWD": "/home/ec2-user",
                    "SHELL": "/bin/bash",
                    "SHLVL": "2",
                    "SSH_CLIENT": "24.187.17.118 60904 22",
                    "SSH_CONNECTION": "24.187.17.118 60904 172.31.94.190 22",
                    "SSH_TTY": "/dev/pts/0",
                    "TERM": "xterm-256color",
                    "USER": "ec2-user",
                    "_": "/usr/bin/python"
                },
                "ansible_eth0": {
                    "active": true,
                    "device": "eth0",
                    "features": {
                        "esp_hw_offload": "off [fixed]",
                        "esp_tx_csum_hw_offload": "off [fixed]",
                        "fcoe_mtu": "off [fixed]",
                        "generic_receive_offload": "on",
                        "generic_segmentation_offload": "on",
                        "highdma": "off [fixed]",
                        "hw_tc_offload": "off [fixed]",
                        "l2_fwd_offload": "off [fixed]",
                        "large_receive_offload": "off [fixed]",
                        "loopback": "off [fixed]",
                        "netns_local": "off [fixed]",
                        "ntuple_filters": "off [fixed]",
                        "receive_hashing": "off [fixed]",
                        "rx_all": "off [fixed]",
                        "rx_checksumming": "on [fixed]",
                        "rx_fcs": "off [fixed]",
                        "rx_udp_tunnel_port_offload": "off [fixed]",
                        "rx_vlan_filter": "off [fixed]",
                        "rx_vlan_offload": "off [fixed]",
                        "rx_vlan_stag_filter": "off [fixed]",
                        "rx_vlan_stag_hw_parse": "off [fixed]",
                        "scatter_gather": "on",
                        "tcp_segmentation_offload": "on",
                        "tx_checksum_fcoe_crc": "off [fixed]",
                        "tx_checksum_ip_generic": "off [fixed]",
                        "tx_checksum_ipv4": "on [fixed]",
                        "tx_checksum_ipv6": "off [requested on]",
                        "tx_checksum_sctp": "off [fixed]",
                        "tx_checksumming": "on",
                        "tx_esp_segmentation": "off [fixed]",
                        "tx_fcoe_segmentation": "off [fixed]",
                        "tx_gre_csum_segmentation": "off [fixed]",
                        "tx_gre_segmentation": "off [fixed]",
                        "tx_gso_partial": "off [fixed]",
                        "tx_gso_robust": "on [fixed]",
                        "tx_ipxip4_segmentation": "off [fixed]",
                        "tx_ipxip6_segmentation": "off [fixed]",
                        "tx_lockless": "off [fixed]",
                        "tx_nocache_copy": "off",
                        "tx_scatter_gather": "on",
                        "tx_scatter_gather_fraglist": "off [fixed]",
                        "tx_sctp_segmentation": "off [fixed]",
                        "tx_tcp6_segmentation": "off [requested on]",
                        "tx_tcp_ecn_segmentation": "off [fixed]",
                        "tx_tcp_mangleid_segmentation": "off",
                        "tx_tcp_segmentation": "on",
                        "tx_udp_tnl_csum_segmentation": "off [fixed]",
                        "tx_udp_tnl_segmentation": "off [fixed]",
                        "tx_vlan_offload": "off [fixed]",
                        "tx_vlan_stag_hw_insert": "off [fixed]",
                        "udp_fragmentation_offload": "off",
                        "vlan_challenged": "off [fixed]"
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": "172.31.94.190",
                        "broadcast": "172.31.95.255",
                        "netmask": "255.255.240.0",
                        "network": "172.31.80.0"
                    },
                    "ipv6": [
                        {
                            "address": "fe80::10f3:50ff:fea3:9151",
                            "prefix": "64",
                            "scope": "link"
                        }
                    ],
                    "macaddress": "12:f3:50:a3:91:51",
                    "module": "xen_netfront",
                    "mtu": 9001,
                    "pciid": "vif-0",
                    "promisc": false,
                    "timestamping": [
                        "rx_software",
                        "software"
                    ],
                    "type": "ether"
                },
                "ansible_fibre_channel_wwn": [],
                "ansible_fips": false,
                "ansible_form_factor": "Other",
                "ansible_fqdn": "ip-172-31-94-190.ec2.internal",
                "ansible_hostname": "ip-172-31-94-190",
                "ansible_hostnqn": "",
                "ansible_interfaces": [
                    "lo",
                    "eth0"
                ],
                "ansible_is_chroot": false,
                "ansible_iscsi_iqn": "",
                "ansible_kernel": "4.14.62-65.117.amzn1.x86_64",
                "ansible_kernel_version": "#1 SMP Fri Aug 10 20:03:52 UTC 2018",
                "ansible_lo": {
                    "active": true,
                    "device": "lo",
                    "features": {
                        "esp_hw_offload": "off [fixed]",
                        "esp_tx_csum_hw_offload": "off [fixed]",
                        "fcoe_mtu": "off [fixed]",
                        "generic_receive_offload": "on",
                        "generic_segmentation_offload": "on",
                        "highdma": "on [fixed]",
                        "hw_tc_offload": "off [fixed]",
                        "l2_fwd_offload": "off [fixed]",
                        "large_receive_offload": "off [fixed]",
                        "loopback": "on [fixed]",
                        "netns_local": "on [fixed]",
                        "ntuple_filters": "off [fixed]",
                        "receive_hashing": "off [fixed]",
                        "rx_all": "off [fixed]",
                        "rx_checksumming": "on [fixed]",
                        "rx_fcs": "off [fixed]",
                        "rx_udp_tunnel_port_offload": "off [fixed]",
                        "rx_vlan_filter": "off [fixed]",
                        "rx_vlan_offload": "off [fixed]",
                        "rx_vlan_stag_filter": "off [fixed]",
                        "rx_vlan_stag_hw_parse": "off [fixed]",
                        "scatter_gather": "on",
                        "tcp_segmentation_offload": "on",
                        "tx_checksum_fcoe_crc": "off [fixed]",
                        "tx_checksum_ip_generic": "on [fixed]",
                        "tx_checksum_ipv4": "off [fixed]",
                        "tx_checksum_ipv6": "off [fixed]",
                        "tx_checksum_sctp": "on [fixed]",
                        "tx_checksumming": "on",
                        "tx_esp_segmentation": "off [fixed]",
                        "tx_fcoe_segmentation": "off [fixed]",
                        "tx_gre_csum_segmentation": "off [fixed]",
                        "tx_gre_segmentation": "off [fixed]",
                        "tx_gso_partial": "off [fixed]",
                        "tx_gso_robust": "off [fixed]",
                        "tx_ipxip4_segmentation": "off [fixed]",
                        "tx_ipxip6_segmentation": "off [fixed]",
                        "tx_lockless": "on [fixed]",
                        "tx_nocache_copy": "off [fixed]",
                        "tx_scatter_gather": "on [fixed]",
                        "tx_scatter_gather_fraglist": "on [fixed]",
                        "tx_sctp_segmentation": "on",
                        "tx_tcp6_segmentation": "on",
                        "tx_tcp_ecn_segmentation": "on",
                        "tx_tcp_mangleid_segmentation": "on",
                        "tx_tcp_segmentation": "on",
                        "tx_udp_tnl_csum_segmentation": "off [fixed]",
                        "tx_udp_tnl_segmentation": "off [fixed]",
                        "tx_vlan_offload": "off [fixed]",
                        "tx_vlan_stag_hw_insert": "off [fixed]",
                        "udp_fragmentation_offload": "off",
                        "vlan_challenged": "on [fixed]"
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": "127.0.0.1",
                        "broadcast": "host",
                        "netmask": "255.0.0.0",
                        "network": "127.0.0.0"
                    },
                    "ipv6": [
                        {
                            "address": "::1",
                            "prefix": "128",
                            "scope": "host"
                        }
                    ],
                    "mtu": 65536,
                    "promisc": false,
                    "timestamping": [
                        "tx_software",
                        "rx_software",
                        "software"
                    ],
                    "type": "loopback"
                },
                "ansible_local": {},
                "ansible_lsb": {},
                "ansible_machine": "x86_64",
                "ansible_machine_id": "fef67c45adfb1d65225893255df2b04b",
                "ansible_memfree_mb": 224,
                "ansible_memory_mb": {
                    "nocache": {
                        "free": 868,
                        "used": 117
                    },
                    "real": {
                        "free": 224,
                        "total": 985,
                        "used": 761
                    },
                    "swap": {
                        "cached": 0,
                        "free": 0,
                        "total": 0,
                        "used": 0
                    }
                },
                "ansible_memtotal_mb": 985,
                "ansible_mounts": [
                    {
                        "block_available": 1632826,
                        "block_size": 4096,
                        "block_total": 2030953,
                        "block_used": 398127,
                        "device": "/dev/xvda1",
                        "fstype": "ext4",
                        "inode_available": 483722,
                        "inode_total": 524288,
                        "inode_used": 40566,
                        "mount": "/",
                        "options": "rw,noatime,data=ordered",
                        "size_available": 6688055296,
                        "size_total": 8318783488,
                        "uuid": "1ade993f-5854-45a8-ae15-3d49e5fcbe67"
                    }
                ],
                "ansible_nodename": "ip-172-31-94-190",
                "ansible_os_family": "RedHat",
                "ansible_pkg_mgr": "yum",
                "ansible_proc_cmdline": {
                    "console": [
                        "tty1",
                        "ttyS0"
                    ],
                    "nvme_core.io_timeout": "4294967295",
                    "root": "LABEL=/",
                    "selinux": "0"
                },
                "ansible_processor": [
                    "0",
                    "GenuineIntel",
                    "Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz"
                ],
                "ansible_processor_cores": 1,
                "ansible_processor_count": 1,
                "ansible_processor_threads_per_core": 1,
                "ansible_processor_vcpus": 1,
                "ansible_product_name": "HVM domU",
                "ansible_product_serial": "NA",
                "ansible_product_uuid": "NA",
                "ansible_product_version": "4.2.amazon",
                "ansible_python": {
                    "executable": "/usr/bin/python",
                    "has_sslcontext": true,
                    "type": "CPython",
                    "version": {
                        "major": 2,
                        "micro": 16,
                        "minor": 7,
                        "releaselevel": "final",
                        "serial": 0
                    },
                    "version_info": [
                        2,
                        7,
                        16,
                        "final",
                        0
                    ]
                },
                "ansible_python_version": "2.7.16",
                "ansible_real_group_id": 500,
                "ansible_real_user_id": 500,
                "ansible_selinux": {
                    "status": "Missing selinux Python library"
                },
                "ansible_selinux_python_present": false,
                "ansible_service_mgr": "upstart",
                "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBAKmcc4NBxWTiOqX/jdg01Ywl1xYmHKFES13l3gPDstl1jOkFkCjJTZhY1hnCywOXC/yYWd1dlBAf3U1rnrGsEWG98/gGHamBsR6ykuPe2pxI9znh46V1xYpRpY1RfjZZ/8D7aEPHXIBDpCsUxHlF41gvX2EhVpIIioJeOwF5uz8zAAAAFQCRBwQz9E5URC/umtsp+si9VNsGjwAAAIBpxNzHbhGIab4+YpLc1Mt1EucWH202OcaYPHN8Rzyxx0BMp4Pqh0yvlAo8tfwOzDUxVYCPimSzXKRHwobeXy/hmv9DMekUT+DYFFSpDYTQn23rurihuHxTM3StGourHhq3iTk00B+X1qKF69V9O1HwPKR8VYbQnSNgnJ81NdJN6AAAAIAc+TnOyu3TXLHw0IXJEPmUqi2sOBgHNEWbtqEybhFIJKmXGrfYF6CPJLlwdtd0rIR3iPz0du1CKvBXAKY50+y29v8gDHTQdYbnDLeYxqpMf+xFEjfuSU3rmbRA/ealoG3P+dpR5DhhOuIN1beRMZFarArqtMBmTRiCqAioRIEz5A==",
                "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBI95vsHxkXdL4JjueQ/F8E7tfr5dUhH8kdvnnXiu0QvEKo8wJVV6cBGnBKuvckEesAoOc+55QWwn8RviHp/LfyU=",
                "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIBCcSbXTmYudwPkmhmShysni/n0CRfdcPvY9l6NN095B",
                "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDn03D+cJVjB7XOMu62K7xTTwoYNeMWa2lSmgoFJSlxvCYw9eCqlt1XPFAAoHmlYvBhPmCXATu2v6f1XWQRaD4VYR1uopDh6Ku9WhBOyYk5FGkJWgyM5Vm+TTrd6Btx5d/+w8tWUIT1BQ4V0pQYSeYRwZilfs+AA8mYRFrlf6+Bqvzn1hGGlRnC5PD4JTbjCT6ys22Il1RSIwWYHtx+zHfCJTrcP8qUcYB9mftJspWrwyOSw1zTCQBs8yQazlxLlzy3XsGK8zgJEtA5vQvosibPGYckfp/TM7SIYzY/pLz2IhQiaeHwdmInlvvSssUlJ6taTBiLga7LDQDmDH7G9sLn",
                "ansible_swapfree_mb": 0,
                "ansible_swaptotal_mb": 0,
                "ansible_system": "Linux",
                "ansible_system_capabilities": [
                    ""
                ],
                "ansible_system_capabilities_enforced": "True",
                "ansible_system_vendor": "Xen",
                "ansible_uptime_seconds": 11917,
                "ansible_user_dir": "/home/ec2-user",
                "ansible_user_gecos": "EC2 Default User",
                "ansible_user_gid": 500,
                "ansible_user_id": "ec2-user",
                "ansible_user_shell": "/bin/bash",
                "ansible_user_uid": 500,
                "ansible_userspace_architecture": "x86_64",
                "ansible_userspace_bits": "64",
                "ansible_virtualization_role": "guest",
                "ansible_virtualization_type": "xen",
                "discovered_interpreter_python": "/usr/bin/python",
                "gather_subset": [
                    "all"
                ],
                "module_setup": true
            },
            "changed": false
        }
    ```

- Example playbook:
    ```yaml
    - name: Add webserver info
      copy: 
        dest: /var/www/html/info.php
        content: "{{ ansible_hostname }}"
    ```

- We can create local variables within the playbooks. 
    - Create playbook variables using `vars` to create key/value pairs and dictionary/map of variables. 
    - Can reference variables directly in playbooks. 
    - Can create variable files and import them into the playbooks.
    - Example playbook:
        ```yaml
        vars:
            html_path: "/var/www/html"
            new_var: "repeated information"
        
        tasks:
          - name: Add webserver information
            copy:
              dest: "{{ html_path }}/info.php"
              content: "{{ new_var }}"
        ``` 

- Ansible also gives us the ability to `register` variables from tasks that run to get information about its execution. 
    - Create variables from info returned from tasks ran using `register`.
    - Call registered variables for later use. 
    - Use `debug` module anytime to see variables and debug our playbooks.
    - Example playbook:
        ```yaml
        vars:
            html_path: "/var/www/html"
        
        tasks:
          - name: See directory contents
            command: ls -la {{ html_path }}
            register: dir_contents  # Output/information of execution of the above command is stored in this variable
          
          - name: Debug dir contents
            debug:
              msg: "{{ dir_contents }}"
        ``` 

- [Variables](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html) can also be stored and used from command line, variables in external files or in inventory files. 

## Roles

- Ansible provides [roles framework](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html) that makes each part of variables, tasks, templates and modules fully independent. 
- Helps group tasks together in a way that is self containing.
- Clean and predefined directory structure.
- Break up the configurations into files. 
- Re-use code by others who need similar configurations. 
- Easy to modify and reduces syntax errors. 
- Ansible [helps in creating](https://galaxy.ansible.com/) the directory structure using `ansible-galaxy init <dir_path>`

??? "ansible-galaxy init |dir_path|"
    ```
    $ ansible-galaxy init roles/webservers
        roles/
        └── webservers
            ├── README.md
            ├── defaults
            │   └── main.yml
            ├── files
            ├── handlers
            │   └── main.yml
            ├── meta
            │   └── main.yml
            ├── tasks
            │   └── main.yml
            ├── templates
            ├── tests
            │   ├── inventory
            │   └── test.yml
            └── vars
                └── main.yml
        
        .
        ├── ansible.cfg
        ├── hosts-dev
        ├── index.php
        ├── roles
        │   └── webservers
        │       ├── README.md
        │       ├── defaults
        │       │   └── main.yml
        │       ├── files
        │       │   └── index.php
        │       ├── handlers
        │       │   └── main.yml
        │       ├── meta
        │       │   └── main.yml
        │       ├── tasks
        │       │   └── main.yml
        │       ├── templates
        │       ├── tests
        │       │   ├── inventory
        │       │   └── test.yml
        │       └── vars
        │           └── main.yml
        └── setup-app.yml

        # ansible.cfg

        [defaults]
        inventory = ./hosts-dev
        remote_user = ec2-user
        private_key_file = ~/.ssh/ansible-2020.pem
        host_key_checking = False


        # hosts-dev

        [webservers]
        app1 ansible_host=54.152.194.112
        app2 ansible_host=3.211.181.182

        [loadbalancers]
        lb ansible_host=54.89.101.67

        [local] 
        control ansible_connection=local
        # above 2 lines code is the way Ansible communicates back to the control host and so this is important
        

        # index.php

        <?php
            echo "<h1>Hello, World! This is my Ansible page.</h1>";
        ?>


        # setup-app.yml

        ---
        - hosts: webservers
            become: true
            roles:
            - webservers
    ```

## Check Mode (Dry run)

- Reports changes that Ansible would have to make on the end hosts rather than applying the changes. 
- Commands are run without affecting the remote system and reports changes.
- Great for one node at a time and used for basic configuration management use cases.
    ```bash
    $ ansible-playbook setup-app.yml --check
    ```

## Error Handling in playbooks

- Change the default behavior of Ansible when certain events happen that may or may not need to report as a failure or changed status.
- Sometimes non-zero exit code is fine.
- Sometimes commands might not need to report a changed status. 
- Explicitly force Ansible to ignore errors or changes that occur. 

!!! Note ""
    *Shell Module and Command Module always return a changed status when run and even when no changes are made to the node server*

```yaml
# check-status.yml
---
  - hosts: webservers:loadbalancers
    become: true
    tasks:
      - name: Check apache status
        command: service httpd status
        changed_when: false # Ignores if changes occur
      
      - name: this will not fail
        command: /bin/false # always returns non-zero exit code (fail status)
        ignore_errors: yes # Ignore errors
```

## Tags

- Assigning tags to specific tasks in playbooks allows you to only call certain tasks in a very long playbook. 
- It only runs specific parts of a playbook rather than all of the plays.
- Add tags to any tasks and re-use if needed. 
- Specify the tags you want to run (or not to) on the command line. 
- After adding `tags: <tag_name>` to any of the tasks, it can be called (or not) using:
    ```bash
    $ ansible-playbook setup-app.yml --tags <tag_name>
    $ ansible-playbook setup-app.yml --skip-tags <tag_name>
    ```

## Ansible Vault

- Ansible vault is a way to keep sensitive information in encrypted files and not plain text in playbooks. 
- Keeps passwords, keys and other sensitive variables in encrypted vault files. 
- Vault files can be shared through source control. 
- Password protected and default cipher is AES. 
- Encrypted data file can be created using:
    ```bash
    $ ansible-vault create secret-variables.yml # create encrypted file
    $ ansible-vault edit secret-variables.yml # edit encrypted file
    $ ansible-playbook setup-app.yml --ask-vault-pass # prompt for password to use the encrypted secret variables file
    ```

