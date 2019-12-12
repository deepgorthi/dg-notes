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

