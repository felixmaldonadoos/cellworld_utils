# MvP (Title WIP)
Mouse Versus Predator

[Brief Description of the Project]

[Define Task That we Are Doing]

<!-- ![Task Diagram](images/task_logic_sq.png) -->


## Robotics Control
<div style="text-align: center;" markdown="1">
<img src="images/robot_ctrl_2x.gif" alt="2x Speed of Robot Moving"/>
</div>
[Here's the Robot, Designed by Gabrielle Wink and Dr. Angel Germán Espinosa Coarasa]

![Robot Breakdown](images/robot_sq.png)

Image Credits: Lai, et al. (2024). *A robot-rodent interaction arena with adjustable spatial complexity for ethologically relevant behavioral studies.* Cell Reports

[How Does the Robot Move?]

![Networking Diagram](images/robot_ctrl_diagram.PNG)

[Explain How Giving a Set Destination Propogates into Giving Wheel Commands to a Skid Steer Drive Robot]

## Virtual-Reality

[Okay so the readers know what the task is, how are we doing it in VR?]

[Making Arena Larger]

[Wilson Field Footage]

[How to Convert Coordinates in VR to Coordinates in the Habitat]

[Inputs to the Game]

[TODO: Adding in Occlusions]

[Anything else Relevant]
## Networking
![Networking Diagram](images/networking_diagram.jpg)
[A break down of TCP Messaging, how it works and what I wrote using this Library (Credit Dr. Angel Germán Espinosa Coarasa)]

[Is essentially a custom package that lets us easily communicate between "nodes" in a client-server like relationship]

[Short Break Down of TCPTest and how that was used]

[TCP Messages allows up to send messages, requests and responses, broadcast messages to subscribed clients, etc.]

[Anything Else Relevant]

[Necessary IP Information]
[IP Address of the Habitat] Arena WAN: 129.105.249.94
[IP Address of the Habitat Computer]
Arena: Given IP: 192.168.137.73
Fixed IP: 192.168.137.151
 
[In order to allow Port Forwarding Script to Work]
Set-ExecutionPolicy -ExecutionPolicy Unrestricted

## Step-Up Module
![Step-Up Module Diagram](images/step_up_diagram.PNG)

**Overview:** The Step-Up Module is a *DC-to-DC converter that steps up 12V from the Virtual Reality (VR) backpack to 19.5V required by the VR Headset*. 
Because there isn't a proprietary cable that connects the HP Reverb G2 VR backpack to the HP Reverb G2 Headset, I made my own!

**Why?** Our Experiment requires a mobile agent moving in a large environment, which required us to extricate ourselves from a tethered power connection. This is because the Virtual Reality gear - the Headset and Backpack - requires a connection to an outlet..

**How it Works:** As mentioned previously, this DC-to-DC converter takes 12V from the VR backpack steps it up to 19.5V, and goes into the headset. This allows the backpack and headset to be completely untethered to a wall outlet.   

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