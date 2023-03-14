import subprocess

data = subprocess.check_output(['iwlist', 'scan']).decode('utf-8').split('\n')
ssid_list = []
for line in data:
    if 'ESSID:' in line:
        ssid = line.strip().split(':')[1][1:-1]
        if ssid not in ssid_list:  # check if SSID is not already added
            ssid_list.append(ssid)
for ssid in ssid_list:
    try:
        results = subprocess.check_output(['iwconfig', ssid]).decode('utf-8').split('\n')
        results = [b.split(' ')[-1] for b in results if 'Quality=' in b]
        print("{:<30}| {:<}".format(ssid, results[0]))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(ssid, "Error: SSID not available or invalid"))
