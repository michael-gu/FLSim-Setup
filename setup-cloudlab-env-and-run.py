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
mysql_command = '''sudo mysql -u root -ptest -e "CREATE DATABASE IF NOT EXISTS cifar10_benchmarks; USE cifar10_benchmarks; CREATE USER IF NOT EXISTS 'michgu'@'localhost' IDENTIFIED BY 'Dolphin#1';
GRANT ALL PRIVILEGES ON *.* TO 'michgu'@'localhost' WITH GRANT OPTION;"'''

try:
    # change directory to root /
    for _ in range(3):
        try:
            os.chdir('..')
        except Exception as e:
            print("cd to root failed, exiting.")
            sys.exit(1)
    if os.path.exists("/mydata/FLSim"):
        if os.system("sudo rm -rf /mydata/FLSim") != 0:
            print("Failed to remove /mydata/FLSim, exiting.")
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
    try:
        os.chdir('mydata/FLSim')
        print("current path: " + os.getcwd())
    except Exception as e:
        print("cd to flsim failed, exiting.")
        sys.exit(1)
    if os.system(install_mysql_connector) != 0:
        print("installation of mysql-connector failed, exiting.")
        sys.exit(1)
    if os.system(install_project_packages) != 0:
        print("installation of project packages failed, exiting.")
        sys.exit(1)
    try:
        os.chdir('examples')
    except Exception as e:
        print("cd to examples failed, exiting.")
        sys.exit(1)
        
    print("Setup completed.")
    print("To run the benchmark, please run the following command:")
    print("cd ../../../mydata/FLSim/examples")
    
    print("Changing directories and running the benchmark test...")
    try:
        os.chdir('../../../mydata/FLSim/examples')
    except Exception as e:
        print("cd to examples failed, exiting.")
        sys.exit(1)
    print("Benchmarking beginning now...")
    # benchmark
    if os.system("nohup sudo python3 record_stats.py false 10") != 0:
        print("benchmarking without feature failed, exiting.")
        sys.exit(1)
    if os.system("nohup sudo python3 record_stats.py true 10") != 0:
        print("benchmarking with feature failed, exiting.")
        sys.exit(1)

except KeyboardInterrupt:
        print("Interrupted by user, exiting.")
        sys.exit(1)
