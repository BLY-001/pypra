with open('devices.txt')as f:
    content = f.read().splitlines()
    devices = []
    for lines in content[1:]:
        c = lines.split(':')
        devices.append(c)
    print(devices)

    # now that everything has been arranged to iterate over the ip address
    for device in devices:
        print(f'pinging {device[1]}...')
        # pass