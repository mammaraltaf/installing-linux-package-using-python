import subprocess

package_name = "htop"
try:
    command = subprocess.run(["sudo", "apt-get", "install",
                              "-y", package_name], check=True)

    with open("output.txt", 'w') as outfile:
        outfile.write("Task Completed!")

except subprocess.CalledProcessError:
    print("Unable to install Package!")
