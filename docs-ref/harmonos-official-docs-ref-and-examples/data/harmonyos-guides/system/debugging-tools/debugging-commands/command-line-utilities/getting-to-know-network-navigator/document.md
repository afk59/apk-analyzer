# Getting to Know Network Navigator

Network Navigator, also known as netcopilot, is a tool designed to assist you in network simulation. It allows you to directly call related APIs via hdc command-line interface (CLI) to simulate preset network scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/9igEtaRbT0mQ2JJYEWr0vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=018397CF44CEF55C4887DE85652DFEB871E03ACAF0D7DBCB1DCE5F2CF07EDF18)

Before using Network Navigator, you need to obtain the hdc tool.

#### How to Use

## Command Syntax

hdc shell netcopilot <Parameter> <Sub-parameter>

The following table lists the command parameters and sub-parameters.

## Command Parameters

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Parameters</p></td><td valign="top"><p>Sub-parameter</p></td><td valign="top"><p>Description</p></td><td valign="top"><p>Remarks</p></td></tr><tr><td valign="top"><p>-h</p></td><td valign="top"><p>NA</p></td><td valign="top"><p>Displays help information.</p></td><td valign="top">&nbsp;&nbsp;</td></tr><tr><td valign="top"><p>-e</p></td><td valign="top"><p><strong>0</strong>: off; <strong>1</strong>: on</p></td><td valign="top"><p>Enables or disables Network Navigator.</p></td><td valign="top"><p>When this switch is disabled, other options are unavailable.</p></td></tr><tr><td valign="top"><p>-p</p></td><td valign="top"><p>NA</p></td><td valign="top"><p>Prints the list of network simulation scenarios.</p></td><td valign="top"><p>By default, the list of preset network simulation scenarios is printed.</p><p>In &amp; out of elevator</p><p>Leave home WLAN range</p><p>Enter home WLAN range</p><p>Busy cafeteria</p><p>Parking garage</p><p>Riding the subway</p><p>Riding high-speed train (switching between SIM cards)</p><p>Highway driving</p></td></tr><tr><td valign="top"><p>-s</p></td><td valign="top"><p>Scenario ID</p></td><td valign="top"><p>Starts a network simulation.</p></td><td valign="top"><p>You can switch between different network simulation scenarios.</p><p>Network simulations must meet the corresponding network adapter requirements. For scenarios such as using the elevator, disconnecting WLAN when leaving home, or connecting WLAN when arriving home, both WLAN and cellular networks must be connected. For all other scenarios, either WLAN or cellular networks need to be connected.</p></td></tr><tr><td valign="top"><p>-c</p></td><td valign="top"><p>Scenario ID</p></td><td valign="top"><p>Cancels a network simulation.</p></td><td valign="top">&nbsp;&nbsp;</td></tr></tbody></table>

#### Usage Examples

## Displaying Help Information

\> hdc shell netcopilot -h
netcopilot usage:
  -h : show help message
  -e <enable>: 0 for disable, 1 for enable
  -p : print all scenario info
  -s <scenario id>: simulate specified network scenario
  -c : cancel simulating scenario
  -P <scenario id>: print specified scenario details
  -a <custom scenario details>: add custom network scenario
  -d <scenario id>: delete custom network scenario

## Enabling or Disabling Network Navigator

\> hdc shell netcopilot -e 0
Disable netcopilot success

> hdc shell netcopilot -e 1
Enable netcopilot success

## Viewing the List of Network Simulation Scenarios

\> hdc shell netcopilot -p
  +------------+------------------------------+
  | ScenarioID | ScenarioName                 |
  +------------+------------------------------+
  1            | In & out of elevator
  2            | Leave home WLAN range
  3            | Enter home WLAN range
  4            | Busy cafeteria
  5            | Parking garage
  6            | Riding the subway
  7            | Riding high-speed train (switching between SIM cards)
  8            | Highway driving
  +------------+------------------------------+

## Starting a Network Simulation

\> hdc shell netcopilot -s 4
Success to simulate scenario 4

## Canceling a Network Simulation

\> hdc shell netcopilot -c 4
Clear active net scenario success
