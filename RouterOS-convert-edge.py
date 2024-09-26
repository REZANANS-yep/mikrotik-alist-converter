import ipaddress

def is_ipv6(ip):
    """Check if the given IP is IPv6."""
    try:
        return ipaddress.ip_network(ip).version == 6
    except ValueError:
        return False

def get_mikrotik_command(ip_CIDR, list_name):
    """Return MikroTik list add command based on IP/CIDR and list name."""
    return f"add address={ip_CIDR} list={list_name}"

def main():
    list_name = input("Enter the name of the MikroTik list: ")

    overwrite = input("Do you want to overwrite the existing content of output.txt? (yes/no): ").strip().lower()
    if overwrite not in ['yes', 'no']:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    # input.txt
    with open('input.txt', 'r') as f:
        ips = [line.strip() for line in f]

    # Check if there are any IPv6 addresses
    if any(is_ipv6(ip) for ip in ips):
        include_ipv6 = input("The list contains IPv6 addresses. Do you want to include them? (yes/no): ").strip().lower()
        if include_ipv6 not in ['yes', 'no']:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            return
    else:
        include_ipv6 = 'yes'

    if include_ipv6 == 'no':
        ips = [ip for ip in ips if not is_ipv6(ip)]

    commands = [get_mikrotik_command(ip, list_name) for ip in ips]

    # Determine the write mode based on user input
    write_mode = 'w' if overwrite == 'yes' else 'a'

    # output.txt
    with open('output.txt', write_mode) as f:
        for command in commands:
            f.write(command + '\n')

    print(f"Converted IP/CIDR to MikroTik commands {'and overwrote' if overwrite == 'yes' else 'and appended to'} 'output.txt'.")

if __name__ == '__main__':
    main()
