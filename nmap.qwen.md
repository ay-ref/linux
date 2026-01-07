# Complete Nmap Cheatsheet

## Basic Scanning Commands

### Basic Scan
```bash
nmap <target>                      # Basic scan with default options
nmap -v <target>                   # Verbose output
nmap -vv <target>                  # Very verbose output
```

### Target Specification
```bash
nmap 192.168.1.1                  # Single IP address
nmap 192.168.1.0/24               # CIDR notation network
nmap 192.168.1.1-100              # Range of IP addresses
nmap example.com                  # Domain name
nmap -iL targets.txt              # List of targets from file
```

## Scan Types

### Host Discovery
```bash
nmap -sL <target>                 # List scan (no scanning)
nmap -sn <target>                 # Ping scan (no port scan)
nmap -Pn <target>                 # Treat all hosts as online (skip ping)
nmap -PS <target>                 # TCP SYN ping
nmap -PA <target>                 # TCP ACK ping
nmap -PU <target>                 # UDP ping
nmap -PR <target>                 # ARP ping (local network only)
```

### Port Scanning Techniques
```bash
nmap -sS <target>                 # TCP SYN scan (stealth scan)
nmap -sT <target>                 # TCP connect scan
nmap -sU <target>                 # UDP scan
nmap -sF <target>                 # FIN scan
nmap -sN <target>                 # NULL scan (no flags)
nmap -sX <target>                 # XMAS scan (FIN,PSH,URG flags)
nmap -sA <target>                 # ACK scan (firewall testing)
nmap -sW <target>                 # Window scan
nmap -sI <zombie_host> <target>   # Idle scan (zombie host)
```

## Port Specification
```bash
nmap -p 80 <target>              # Scan specific port
nmap -p 80,443 <target>          # Scan multiple ports
nmap -p 1-1000 <target>          # Scan port range
nmap -p U:53,T:21-25,80,443 <target>  # Mixed UDP/TCP ports
nmap -p- <target>                # Scan all 65535 ports
nmap -F <target>                 # Fast scan (top 100 ports)
nmap --top-ports 1000 <target>   # Scan top N ports
```

## Service/Version Detection
```bash
nmap -sV <target>                # Service/version detection
nmap -sV --version-intensity 5 <target>  # Set intensity (0-9)
nmap -sV --version-light <target>       # Light intensity
nmap -sV --version-all <target>         # All intensity levels
```

## OS Detection
```bash
nmap -O <target>                 # OS detection
nmap -O --osscan-limit <target>  # Limit OS detection to promising targets
nmap -O --osscan-guess <target>  # Guess OS more aggressively
```

## Timing and Performance
```bash
nmap -T0 <target>                # Paranoid (slowest, most stealthy)
nmap -T1 <target>                # Sneaky
nmap -T2 <target>                # Polite
nmap -T3 <target>                # Normal (default)
nmap -T4 <target>                # Aggressive
nmap -T5 <target>                # Insane (fastest, most visible)
```

## Firewall/IDS Evasion
```bash
nmap -f <target>                 # Fragment packets
nmap -mtu 24 <target>            # Specify fragment size
nmap -D RND:10 <target>          # Decoy scans (10 random decoys)
nmap -S <spoof_ip> <target>      # Spoof source IP
nmap --source-port 53 <target>   # Use source port 53 (DNS)
nmap --data-length 100 <target>  # Append random data
nmap --scan-delay 1s <target>    # Delay between probes
```

## Script Scanning (NSE)
```bash
nmap -sC <target>                # Run default scripts
nmap --script <script_name> <target>  # Run specific script
nmap --script "http*" <target>   # Run scripts matching pattern
nmap --script vuln <target>      # Run vulnerability detection scripts
nmap --script safe <target>      # Run safe scripts only
nmap --script-args=user=admin,pass=secret <target>  # Script arguments
```

## Output Options
```bash
nmap -oN normal.txt <target>     # Normal output format
nmap -oG grep.txt <target>       # Grepable output format 
nmap -oX xml.xml <target>        # XML output format 
nmap -oA basename <target>       # All formats (basename.nmap, basename.gnmap, basename.xml)
nmap --append-output <target>    # Append to existing files
```

## Advanced Options

### Host Discovery Optimization
```bash
nmap -PE <target>                # ICMP echo request
nmap -PP <target>                # ICMP timestamp request
nmap -PM <target>                # ICMP netmask request
```

### Port State Filtering
```bash
nmap --open <target>             # Show only open ports
nmap --closed <target>           # Show only closed ports
nmap --filtered <target>         # Show only filtered ports
```

### Timing Templates
```bash
nmap --min-hostgroup 100 <target>    # Minimum parallel hosts
nmap --max-hostgroup 100 <target>    # Maximum parallel hosts
nmap --min-parallelism 10 <target>   # Minimum parallel probes
nmap --max-parallelism 10 <target>   # Maximum parallel probes
nmap --min-rtt-timeout 100ms <target> # Minimum RTT timeout
nmap --max-rtt-timeout 1s <target>   # Maximum RTT timeout
nmap --initial-rtt-timeout 500ms <target> # Initial RTT timeout
```

## Practical Examples

### Basic Network Scan
```bash
nmap -sS -sV -p- -T4 -v 192.168.1.0/24
```

### Web Server Scan
```bash
nmap -sV -sC -p 80,443,8080 -v example.com
```

### Comprehensive Security Scan
```bash
nmap -sS -sU -sV -O -sC --script vuln -p- -T4 -v <target>
```

### Stealth Scan
```bash
nmap -sS -f -D RND:5 --source-port 53 -T2 -v <target>
```

## Common NSE Scripts
```bash
# Vulnerability scanning
nmap --script vuln <target>

# Web scanning
nmap --script http-enum,http-title,http-methods <target>

# SMB scanning
nmap --script smb-os-discovery,smb-enum-shares,smb-enum-users <target>

# SSH scanning
nmap --script ssh-brute,ssh-hostkey <target>

# Database scanning
nmap --script mysql-info,mysql-brute <target>
```

This comprehensive cheatsheet covers essential Nmap commands for both beginners and advanced users, providing over 50 practical commands for network scanning, enumeration, and security assessment.  
