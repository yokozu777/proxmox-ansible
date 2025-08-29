
# Proxmox Ansible Playbook

This playbook is designed to automate the configuration, optimization, and management of a Proxmox system. It includes a wide range of features to help administrators quickly adapt Proxmox to specific requirements, improve performance, and ensure ease of use.

---

## v1.1.0

### Improvements
- Nginx performance and date/timezone configuration optimizations.

### Compatibility
- Added support for **Proxmox VE 9**.

### New Roles
- **Configure Mail**
- **Configure Certificates**
- **Configure ACME** (Let’s Encrypt or custom CA)

## Quickstart


### Clone the repository:
```bash
git clone git@github.com:yokozu777/proxmox-ansible.git
cd proxmox-ansible
```

### Configure variables for your hosts:
Copy and customize the example variables file:
```bash
cp hosts_vars/example.yml hosts_vars/<your_host_name>.yml
```

Edit `<your_host_name>.yml` to match your desired configuration.


### Required Variables for Connection

To ensure a successful connection, make sure to fill in the following variables in your host vars file:

### Users Configuration
```yaml
initial_user: root # The initial user for the system.
initial_password: P@ssw0rd* # The initial user's password.
```

### Using SSH Keys for Authentication

If you prefer to use SSH keys for authentication, follow these steps:

**Create a `pub_keys` folder:**
   - In the same directory as your host vars file, create a folder named `pub_keys`.

**Add your `.pub` keys:**
   - Place your public SSH keys (`.pub` files) in the `pub_keys` folder.

**User Association:**
   - These keys will automatically be added to the user specified in the `system_user` variable.

### Example:
```yaml
system_user: localuser # The user to which the public keys will be added.
```

### Add your hosts to the inventory:
Update `inventory.yml` with your host(s) and link to the variables file:
```yaml
all:
  hosts:
    proxmox-host:
      ansible_host: <your_proxmox_ip>
      vars_files:
        - hosts_vars/<your_host_name>.yml
```

## Quick Start with Docker

If you do not have Ansible installed, but Docker is available, you can use the provided `Dockerfile` for a quick setup.

### Steps to Use Docker:

1. **Build the Docker Image:**
   ```bash
   docker build -t proxmox:latest .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -it --name proxmox -v $PWD/:/opt proxmox:latest
   ```

This will create and start a Docker container with Ansible pre-installed, allowing you to run the playbook directly from the container.

### Run the playbook:
```bash
ansible-playbook proxmox.yml
```

---

## Description

This repository contains an advanced **Ansible playbook** for automating the configuration, optimization, and management of **Proxmox VE**. 

### Compatibility:
The playbook is compatible with **Proxmox VE versions 7 and 8** and has been tested on both versions using **GRUB** and **UEFI** boot configurations.

---

## Key Features

### General System Settings
- Create backups of the `/etc` directory for Proxmox.
- Automatically update the system and configure update schedules.
- Optionally reboot the system after all tasks are completed.

### Repository Management
- Add or remove Debian Backports and Proxmox Test repositories.
- Configure automatic system updates at a specific time.

### Kernel Management
- Install a specific kernel version.
- Pin a specific kernel version (kernel pinning).
- Unpin a previously pinned kernel version.

### Service and Package Management
- Disable AppArmor.
- Install Fail2Ban for enhanced security.
- Install Nginx.
- Display hardware temperatures in the Proxmox web interface.
- Install additional software (e.g., `jq`, `nano`) and remove unnecessary packages.

### Virtualization Support
- Enable nested virtualization.
- Manage Hyper-Threading (enable or disable).

### ISO Image Management
- Automatically download ISO images for Windows VirtIO drivers or custom images.
- Save ISO images to a specified directory.

### SSH Configuration
- Change the SSH port.
- Configure password authentication and root access.

### User Management
- Create and configure users.
- Change the root password if needed.
- Manage public SSH keys for authentication.

### Network Configuration
- Disable IPv6.
- Fully configure network interfaces.
- Set DNS servers.

### Temporary File Systems (tmpfs)
- Create a RAM disk for logs.
- Optimize logging for Nginx and PVEProxy.

### Locale and Timezone Settings
- Add and configure system locales.
- Set the system timezone and NTP servers.

### CPU Performance Configuration
- Configure P-State settings for AMD and Intel CPUs.
- Change CPU operation modes (e.g., `performance`, `powersave`, `schedutil`).

### Proxmox Service Management
- Disable unnecessary Proxmox services (e.g., `lxc`, `spiceproxy`, `corosync`).

### ZFS Configuration
- Manage ZFS ARC cache size.

### PCIe Passthrough Optimization
- Blacklist kernel modules (e.g., `radeon`, `nouveau`, `nvidia`).
- Specify devices for VFIO passthrough.

### Kernel SamePage Merging (KSM) Settings
- Flexible KSM configuration, including scan intervals, thresholds, and page sizes.

---

## Benefits

- **Time-Saving**: Automates routine tasks, speeding up the preparation of Proxmox for production use.
- **Enhanced Security**: Features like Fail2Ban installation, disabling unnecessary services, and SSH access management improve system security.
- **Flexibility**: A wide range of options allows you to tailor the system to specific needs.
- **Convenience**: Automated handling of ISO images, locales, and timezones simplifies administration.
- **Performance Optimization**: Enabling nested virtualization, configuring P-State settings, and using RAM disks for logs improve overall system performance.

This playbook is ideal for administrators looking to streamline the deployment and management of Proxmox, minimize errors, and enhance the performance of their virtualization platform.
