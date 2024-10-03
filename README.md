# mikrotik-alist-converter 🛠️
Convert IP/CIDR to address-list command RouterOS v7.x

## 📋 How to use?
1. **Clone** the repository to your local folder:
   ```bash
   git clone https://github.com/REZANANS-yep/mikrotik-alist-converter.git
   ```
2. **Create** a file named `input.txt` if it not exist. (Optional)
3. **Add** IP/CIDR-based IPv4/IPv6 addresses to `input.txt`.

### 📄 Format of `input.txt`:
```
1.1.1.1/24
1.1.1.0/32
1.1.1.3/19
...

## 🔧 Requirements (note: Script tested only at python 3.11 and ROS 7.16 i cant guarantee stable work on older versions)
- Python 3.11 or higher
- RouterOS version of 7.x
