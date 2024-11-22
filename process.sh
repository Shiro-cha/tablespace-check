#!/bin/bash
#!/usr/bin
port=22
login="oracle"
server="10.72.42.70"
pawd="Oracle_1"

LogDirectory='/home/oracle/monitoring'
DataDirectory='/opt/oracle'

DBUSER='sys'
DBUSERPASSWORD='as sysdba'
DB=$1
DATY=`date  "+%Y%m%d"`

function make_command() {

    echo "sqlplus  $DBUSER/$DBUSERPASSWORD@$DB @$LogDirectory/process.sql"
}


function run_ssh() {
    local server="$1"
    local command="$2"
    if [ -z "$server" ]; then
        echo "Error: server is null" >&2
        return 1
    fi

/usr/bin/expect << EOF
    spawn ssh $login@$server
    expect "password:"
    send "$pawd\r"
    expect "$"
    send "$command\r"
    expect "$"
    send "exit\r"
    expect eof
EOF

    echo "$out"
}


command=$(cat "query.remote")

run_ssh "$server" "$command"

