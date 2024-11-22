class FileHandler(object):
    def __init__(self, command_executor):
        self.command_executor = command_executor

    def send_file(self, server, file, remote_path):
        scp_command = "scp -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -o StrictHostKeyChecking=no {} root@{}:{}".format(file, server, remote_path)
        result = self.command_executor.execute(scp_command)
        if result:
            print("File sent successfully.")
        else:
            print("Error sending file.")

    def check_file_exists(self, server, file):
        ssh_command = "ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -o StrictHostKeyChecking=no root@{} '[ -f {} ] && echo \"yes\"'".format(server, file)
        result = self.command_executor.execute(ssh_command)
        return "yes" in result
