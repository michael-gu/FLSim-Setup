import os
import sys

cd_backwards = "cd .."
git_clone_flsim = "sudo git clone https://github.com/michael-gu/FLSim-Single-Node-BM.git /mydata/FLSim"
apt_update = "sudo apt update"
# require confirmation
apt_install_python3_pip = "sudo apt install -y python3-pip"
cd_flsim = "cd /mydata/FLSim"
cd_mydata = "cd /mydata"
install_mysql_connector = "sudo pip install --upgrade mysql-connector-python"
install_project_packages = "sudo pip install -e ."
install_mysql_server = "sudo apt install -y mysql-server"
alias_1 = "alias mysqladmin=/usr/local/mysql/bin/mysqladmin"
alias_2 = "alias mysql=/usr/local/mysql/bin/mysql"
mysql_command = '''sudo mysql -u root -ptest -e "CREATE DATABASE cifar10_benchmarks; USE cifar10_benchmarks; CREATE USER 'michgu'@'localhost' IDENTIFIED BY 'Dolphin#1';
GRANT ALL PRIVILEGES ON * .* TO 'michgu'@'localhost' WITH GRANT OPTION;"'''

try:
    # change directory to root /
    for _ in range(3):
        if os.system(cd_backwards) != 0:
            print("cd to root failed, exiting.")
            sys.exit(1)
    if os.system(git_clone_flsim) != 0:
        print("git clone failed, exiting.")
        sys.exit(1)
    if os.system(apt_update) != 0:
        print("apt update failed, exiting.")
        sys.exit(1)
    if os.system(apt_install_python3_pip) != 0:
        print("installation of pip package failed, exiting.")
        sys.exit(1)
    if os.system(install_mysql_server) != 0:
        print("mysql server initialization failed, exiting.")
        sys.exit(1)
    if os.system(alias_1) != 0:
        print("alias1 add failed, exiting.")
        sys.exit(1)
    if os.system(alias_2) != 0:
        print("alias2 failed, exiting.")
        sys.exit(1)
    if os.system(mysql_command) != 0:
        print("mysql server user creation or database creation failed, exiting.")
        sys.exit(1)
        
    # change directory to /mydata/FLSim
    if os.system(cd_flsim) != 0:
        print("cd to FLSim failed, exiting.")
        sys.exit(1)
    if os.system(install_mysql_connector) != 0:
        print("installation of mysql-connector failed, exiting.")
        sys.exit(1)
    if os.system(install_project_packages) != 0:
        print("installation of project packages failed, exiting.")
        sys.exit(1)
    if os.system('cd examples') != 0:
        print("installation of project packages failed, exiting.")
        sys.exit(1)

except KeyboardInterrupt:
        print("Interrupted by user, exiting.")
        sys.exit(1)
