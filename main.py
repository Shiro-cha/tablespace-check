from filehandler import FileHandler
from sshhandler import SSHCommandExecutor 
from subprocesshandler import SubprocessCommandExecutor
from outputhandler import OutputHandler

command_executor = SubprocessCommandExecutor()
file_handler = FileHandler(command_executor)
ssh_executor = SSHCommandExecutor(command_executor)

# Main logic
sql_file = "query_tablespace.sql"
remote_dir = "/tmp/"
remote_path = remote_dir + sql_file

# Check if file exists remotely and send if necessary
if not file_handler.check_file_exists("10.72.42.70", remote_path):
    file_handler.send_file("10.72.42.70", sql_file, remote_dir)
else:
    print("File already exists.")

print("Running on {}".format("10.72.42.70"))

# Run SSH command

result = ssh_executor.execute_ssh_command("10.72.42.70", "export ORACLE_HOME=/opt/oracle/product/11gR2/db;export ORACLE_SID=suseora && /opt/oracle/product/11gR2/db/bin/sqlplus  / as sysdba @{}".format(remote_path))
output_handler = OutputHandler(result)
print(output_handler.parse())
