# UDP Test Suit
-----

This tool is created for communication between the HOST test suite and the device, setting up the environment for automatic test for HFNC device.

## Table of Contents 
----
- [Requirement and Setup](#requirement-and-setup)
- [Launch](#launch)
- [Sample Output](#sample-output)


## Requirement and Setup ##
-----
- **[Python 3.8](https://www.python.org/)** 
- **[clang_parser](https://bitbucket.org/reso2h/clang_parser/src/master/)**    
- Using **Virtual Environment(venv)** is recommended

#### Test Suite Topologic Diagram  
![Test Suite Topologic Diagram](assets/imgs/test_suite_topologic_diagram.png)
  
##### Modify the **protocol.py** file under the *udp_test_suite/config* if necessary  

#### Host  
Host side of test suite needs a PC with ethernet connection with below   setting:
  
- IPv4 address: 192.168.10.11  
- Network Mask: 255.255.255.0  
- Gateway: 0,0.0.0  

#### Device Setting  
The ethernet of HFNC device shall be configured as below:  
  
- IPv4 address: 192.168.10.13  
- Network Mask: 255.255.255.0  
- Gateway: 0,0.0.0  

#### Communication Channel  
The communication is established based on UDP connection:  
  
- Host Port: 10000  
- Device Port: 10000  

#### Communication Mode
Communication between Host and Device is synchronized based on Request/Response mode:  
  
1. Host sends UDP request to Device  
2. Device sends UDP response back to Host  



## Launch ##
-----
To run this project, clone from the repository or use the following command with git.    
UDP Test Suite: `$ git clone git@bitbucket.org:reso2h/udp_test_suite.git` 
clang_parser: `$ git clone git@bitbucket.org:reso2h/clang_parser.git`   
     
Then run the following command in terminal:  
`$ python3 udp_command_test.py --case_file file_path`    
    or     
`$ python3 udp_command_test.py -c file_path`   

### Example
`python3 udp_command_test.py --case_file testcases/test_cases.py`     
    or    
`python3 udp_command_test.py -c testcases/test_cases.py` 


## Sample Output ##
![Sample Output](assets/imgs/sample_out1.png)
