# YOLOL Concepts : Execution locks

*Document Status : Theoritical - none of the methods have been tested.*
A Execution locks are various methods to delay the execution of a YOLOL script until triggered by a outside source. 

# Basic Types of locks

## Looplock
A looplock delay the execution of a script by using a looping line that check if the triggering condition is met every chip tick.
This method has the advantage to allow of for complex triggering conditions, but works through the use of External Fields and variables, and as a result may require the use of additional memory chips.
Looplocks are most effective when monitoring a device's External Fields, or when the triggering condition require data from multiple sources.
Due to the fact that a looplock constantly execute its condition line, it may have an increased load on the game servers than a Waitlock or a Sleeplock <sup>unverified</sup>.

#TODO : Include Looplock example.

## Sleeplock
A sleeplock make use of the YOLOL chip Field `ChipWait` to suspend execution until an outside source reactivates it. 
This method requires has the advantage of being self-contained, as it doesn't require any External variable to set up; and of being really short to use. However, it cannot handle complex triggering conditions, reactivating only when its own `ChipWait` is altered.
Sleeplock are most effective for scripts designed to be directly activated by other scripts.

#TODO : Include Sleeplock technical explanation and example.

## Waitlock
A waitlock is a variant of a Sleeplock, which include a built-in timeout. This allow it to reactivate itself on its own after a set time has past.
This method as the share the same advantages and issues than the sleeplock, with the exception of being time-limited.
Waitlocks are most effective for timer and implementing fallback systems in case a subscript is non-responding.

#TODO : Include Waitlock example

# Composite Locks
Composite Locks are lock composed of a combination of locks. They can be more complex to set up, but allow can give unique advantages, or mitigate the limitation of other locks.

## Conditional Sleeplock
#TODO : Include description (Sleeplock + Conditional Lock)

#TODO : Include example

## Timed Looplock
#TODO : Include description (Waitlock + Conditional Lock)

#TODO : Include example

## Fixed Steps lock
#TODO : Include description (Multiple Conditional Locks)

#TODO : Include example

# Chip Chaining
#TODO : describe & List types of chaining (+ button-chain trick)
