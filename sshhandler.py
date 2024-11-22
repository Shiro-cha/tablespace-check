class SSHCommandExecutor(object):
    def __init__(self, command_executor):
        self.command_executor = command_executor

    def execute_ssh_command(self, server, command):
        ssh_cmd = (
            "ssh -o HostKeyAlgorithms=+ssh-rsa "
            "-o PubkeyAcceptedAlgorithms=+ssh-rsa "
            "-o StrictHostKeyChecking=no oracle@{} '{}'".format(server, command)
        )
        return self.command_executor.execute(ssh_cmd)
