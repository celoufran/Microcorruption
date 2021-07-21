# Microcorruption: New Orleans
![Date](https://img.shields.io/badge/Date-July%2020th%202021-brightgreen)  
![Reverse Engineering Category](https://img.shields.io/badge/Category-Reverse_Engineering-lightgrey.svg)\
![Score](https://img.shields.io/badge/Score-15-blue.svg)

## Description
```
Lockitall                                            LOCKIT PRO r a.02
______________________________________________________________________

              User Manual: Lockitall LockIT Pro, rev a.02              
______________________________________________________________________


OVERVIEW

    - We have revised the software in revision 02.
    - This lock is not attached to any hardware security module.


DETAILS

    The LockIT Pro a.02  is the first of a new series  of locks. It is
    controlled by a  MSP430 microcontroller, and is  the most advanced
    MCU-controlled lock available on the  market. The MSP430 is a very
    low-power device which allows the LockIT  Pro to run in almost any
    environment.

    The  LockIT  Pro   contains  a  Bluetooth  chip   allowing  it  to
    communiciate with the  LockIT Pro App, allowing the  LockIT Pro to
    be inaccessable from the exterior of the building.

    There is  no default password  on the LockIT  Pro---upon receiving
    the LockIT Pro, a new password must be set by connecting it to the
    LockIT Pro  App and  entering a password  when prompted,  and then
    restarting the LockIT Pro using the red button on the back.
    
    This is Hardware  Version A.  It contains  the Bluetooth connector
    built in, and one available port  to which the LockIT Pro Deadbolt
    should be connected.

    This is  Software Revision 02.  We have received reports  that the
    prior  version of  the  lock was  bypassable  without knowing  the
    password. We have fixed this and removed the password from memory.

    


(c) 2013 LOCKITALL                                            Page 1/1
```

## Attached files
- [Sydney.txt](Sydney.txt) (Deassembly code)

## Summary
We have to reverse the code to determine the password used to unlock the door.

## Flag
```
xxx
```

## Detailed solution
