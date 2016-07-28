from connection import Machine
from credentials import get_credentials

targets = ['45.32.13.245']
#targets = ['localhost']
input_file = 'cmd'

def main():
    global targets
    username, password = get_credentials('laozi')
    remote_host = Machine(username, password)
    for target in targets:
        remote_host.connect(target)
        stdin, stdout = remote_host.create_channel(target, input_file)
        slb.send_cmd(stdin, stdout, input_file)
        remote_dir = input('Which directory should I list?')
        remote_host.list_content(remote_dir)
        remote_file = input('Which file should I retrieve?')
        for f in remote_file:
            remote_host.retrieve(remote_dir, remote_file)

if __name__ == '__main__':
    main()

