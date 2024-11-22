import subprocess

class CommandExecutor(object):
    def execute(self, command):
        raise NotImplementedError("Subclasses should implement this method.")
class SubprocessCommandExecutor(CommandExecutor):
    def execute(self, command):
        """
        Execute the given command using the subprocess module.

        :param command: The command to execute
        :type command: str
        :return: The output of the command
        :rtype: str
        :raises subprocess.CalledProcessError: If the command fails
        """
        if not command:
            raise ValueError("command cannot be null or empty")

        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stderr:
                print("Error executing command: {}".format(stderr.decode('utf-8')))
            return stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            if e.output:
                print("Error executing command: {}".format(e.output.decode('utf-8')))
            raise