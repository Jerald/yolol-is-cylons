# Daisy: Dynamic Addressing In Space for Yonder

## Abstract

Given the extremely bare-bones design for transmitters and receivers in Starbase, there is no simple way to specify an address where you want a message to arrive at. We propose Daisy as the solution to this problem. Daisy is a protocol designed for spatial addressing and routing for use in the Yonder network. The novel approach used in Daisy is based around a variable length address specifying a direction vector, representing the destination relative to the location of the current node. These addresses segment space into 25km^3 sectors, based on the max transmitter range of 30km plus some buffer. To route a packet you only need to use the last character of the address, allowing for performant parsing even when the destination is very far away. Daisy is designed to exist in the entire stack of Yonder protocols, so we provide an overview of how it fits into the picture. In addition, we show experimental emulated usage of the protocol in action, as proof of its functionality. Lastly, we discuss various improvements that may be made in the future, or incorporated into another layer of the Yonder stack.

## 1. Introduction

## 2. Relation To Other Protocols

## 3. Addressing

## 4. Routing

## 5. Experiments

## 6. Future Work

## 7. Conclusion
