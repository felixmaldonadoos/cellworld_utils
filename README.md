# MvP
Mouse Versus Predator

[Brief Description of the Project]

## Setup Guide
These are the steps you need to follow in order to run the Experiment in Unreal Engine

### Generating Project Files
1. Begin by cloning the [Experiments](https://github.com/germanespinosa/Experiment) Repo
2. Open up the containing folder and right-click on Experiment.uproject
3. You should see an option to "Generate Visual Studio Project Files"
   1. ![Generate Project Files](images/genproj.png)
4. Once this completes, open up **Experiment.sln** in Visual Studio 

### Configuration Settings
Let's make sure we have the correct Configuration Settings, which will let us correctly 
build and compile the code so that we can edit the game!
1. At the top of the Visual Studio IDE, open up the Configuration Manager by click on the drop-down menu
next to the "Local Windows Debugger" play button
   1. ![Configuration Manager](images/configmanager.png)
2. Match your settings to the following:
   1. ![Configuration Settings in the Configuration Manager](images/configsettings.png)
   2. Also, set **Experiment** as the Startup Project, you can do this by right-clicking on Experiment 
   in the solution explorer and navigating down to "Set as Startup Project"
   3. ![Startup Project](images/startupproj.png)
3. You should then be able to start Unreal Engine's Game Editor


### Port-Forwarding
1. Start by opening up `/mnt/c/Research/vr_service` in Windows Powershell 
2. Run the script `.\wsl-port-forwarding.ps1`
3. Now the ports should be forwarded

### Starting the Server
Before we can go ahead and actually play the game, we are going to need to start up the **vr server**,
which is a script that exists locally on the development computer. In fact a lot of what you need
exists locally under: `/mnt/c/Research/...`

1. Start by opening up `/mnt/c/Research/vr_service` in CLion
2. You may need to **Reload CMake Projects** or Rebuild it
3. Under **File -> Settings**
4. Under **Build, Execution, Deployment -> Toolchains**
5. ![Toolchain Settings](images/clionbed.png)
6. ***It is Imperative that the WSL here is WSL2*** 
   1. To check your version, open up Windows Powershell and run `wsl -l -v`
   2. It should output: **Ubuntu-22.04 Version 2**
7. In the top right, you should now be able to run the script `vr_server`. 
8. ![VR Service Script](images/vrsrvscript.png)
9. At this point the vr_server 

### Adding in the Occlusions
In order to see occlusions in the VR World, you need to run an Experiment. This involves running a Python
script that describes specific locations of the occlusions. 
1. After starting the vr_server you can go to the same menu and this time run **start_experiment**
2. This will add in occlusions into the environment when you play

### Setting up a Static IP Address
In order to set up a Static IP Address, start by going to the Windows settings
1. Open up _Network & Internet_
2. Scroll down to _Ethernet or WiFi_, and open up the connected network. 
3. Go down to _IP Setting_, click _Edit_ then _Manual_ to create a Static IP
   1. Set the IP Address - This is something you come up with
   2. Subnet prefix length should be 24 (bits)
   3. Gateway is the same address as the default gateway (129.105.69.1 or 129.105.49.1)?

## Setting up OpenVPN
Connections can be done in one of three ways. First, we can use an ethernet cable to directly connect between two computers to communicate.
This, of course, is not feasible since communication is going to be done on two different parts of campus, and will be done using a moving subject.
The next is communication through our own routers, which requires the use of an open port. That involves getting IT involved. The final solution is a VPN, 
which can be running through anything - for example Northwestern's VPN. In this case I used OpenVPN from AWS, which is not a good idea but at least I know how to use it now.
Here's how to use it...
1. Start the Instance on the AWS Website.
   1. Make sure to click on the Elastic IP Address on each PC you want to connect it to
2. On a Linux Machine install via [these](https://openvpn.net/openvpn-client-for-linux/) instructions. 
   1. If you're using Windows, there's an easy to use GUI that it comes with
3. Download the `user_profile` after connecting to the IP Address listed.
4. Import the Configuration file
   1. `openvpn3 config-import --config <profile.ovpn>`
   2. Confirm you did it correctly with `openvpn3 configs-list`
   3. Start a session using `openvpn3 session-start --config <profile.ovpn>`
      1. You will need to enter in your username and password
   4. View current sessions using `openvpn3 sessions-list`
   5. End the session using `openvpn3 session-manage --config <profile.ovpn> --disconnect`

## Step-Up Module
There does not exist a proprietary cable that connects the HP Reverb G2 VR backpack to the HP Reverb G2 Headset, so I made my own! This DC to DC converter takes 12V from the backpack and steps it up to 19.5V and goes into the headset. This allows the backpack and headset to be untethered from a power supply. 

### Step-Up Module Bill of Materials
Here is the Bill of Materials as well as pictures depicting how the step-up module is assembled. Not depicted are the spacers and screws necessary, as well as the DC-DC step-up converter itself. 

Lastly is the fully assembled Step-Up Module

[Step-Up Module BoM](https://docs.google.com/spreadsheets/d/1b9FdkY2aQWLmUtxk2oAGR2HAnpVTHtHQpYreBFGOhEA/edit?usp=sharing)

#### Assembly of the Step-Up Module
![Assembly of the Step-Up Module](images/assembly_1.jpg)

#### Assembly with Numbered Parts
![Assembly with numbered parts](images/assembly_2.jpg)

#### Fully Assembled Step-Up Module
![Fully Assembled Module](images/full_assembly.jpg)

LAPTOP: 10.105.232.16
PC: 

Arena WAN: 129.105.249.94
Arena: Given IP: 192.168.137.73
Fixed IP: 192.168.137.151

129.105.182.109

Client Test - 