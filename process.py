import subprocess

def ssh_command(server, command):
    ssh_command = "ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -o StrictHostKeyChecking=no oracle@{} {}".format(server, command)
    
    
    output = subprocess.check_output(ssh_command, shell=True, stderr=subprocess.STDOUT)
    return output.decode("utf-8")
  

sql_query = """select 
                    df.tablespace_name "Tablespace",
                    df.bytes/(1024*1024) "Total Size(MB)",
                    sum(fs.bytes)/(1024*1024) "Free Size(MB)",
                    round(sum(fs.bytes)*100/df.bytes) "% Free",
                    round((df.bytes-sum(fs.bytes))*100/df.bytes) "% Used" 
                from 
                    dba_free_space fs, 
                    (select 
                        tablespace_name, 
                        sum(bytes) bytes 
                     from 
                        dba_data_files 
                     group by 
                        tablespace_name) df 
                where 
                    fs.tablespace_name = df.tablespace_name 
                group by 
                    df.tablespace_name, df.bytes;"""

output = ssh_command("10.72.42.70", "if [ -f /home/oracle/monitoring/process.sql ]; then rm -f /home/oracle/monitoring/process.sql; fi; echo '{}' > /home/oracle/monitoring/process.sql".format(sql_query))
if output is not None:
    print(output)
