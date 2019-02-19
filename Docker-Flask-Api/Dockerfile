FROM ubuntu:16.04

# --------------------------Add User Couture--------------------------

RUN apt-get update -y

#standard apt packages
RUN apt-get install -y apt-transport-https apt-utils software-properties-common

#--------------install required dependencies--------------
RUN apt-get install -y build-essential libssl-dev libffi-dev  libsasl2-dev libldap2-dev libxi-dev


#----------install python3 and development tools----------
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update -y && apt-get install -y python3.6
RUN apt-get install python3.6-dev python3-pip python-dev -y
RUN python3.6 -m pip install --upgrade setuptools pip wheel

#------install python packages from requirements.txt------

#--------------------install superset--------------------

#-----switch user inside container after installation-----
#give permission to user for the superset_dir for copying couture-dashboard files

#---------------Application specific changes---------------

#------------------Expose required Ports------------------

#-----------------Run Superset Application-----------------
#docker run --name CONTAINER-NAME-tid -p 8088:8088 -v supersetdb:/home/couture/.superset image:tag

