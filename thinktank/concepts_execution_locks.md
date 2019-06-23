# YOLOL Concepts : Execution locks

*Document Status : Theoritical - none of the methods have been tested.*
A Execution locks are various methods to delay the execution of a YOLOL script until triggered by a outside source. 

# Basic Types of locks

## Looplock
A looplock delay the execution of a script by using a looping line that check if the triggering condition is met every chip tick.
This method has the advantage to allow of for complex triggering conditions, but works through the use of External Fields and variables, and as a result may require the use of additional memory chips.
Looplocks are most effective when monitoring a device's External Fields, or when the triggering condition require data from multiple sources.
Due to the fact that a looplock constantly execute its condition line, it may have an increased load on the game servers than a Waitlock or a Sleeplock <sup>unverified</sup>.
> **Example**
>
> | | Chip |
> |-|-|
> |1|if :condition then goto 2 end goto 1|
> |2|*// this line is executed only once the condition is realized*  |

> **Example - Inversed**
>
> <sup>Depending on the condition, this method can be shorter than a normal Looplock</sup>
>
> | | Chip |
> |-|-|
> |1|if :condition then goto 1 end|
> |2|*// this line is executed only once the condition is not realized.*  | 

## Sleeplock
A sleeplock make use of the YOLOL chip Field `ChipWait` to suspend execution until an outside source reactivates it. 
This method requires has the advantage of being self-contained, as it doesn't require any External variable to set up; and of being really short to use. However, it cannot handle complex triggering conditions, reactivating only when its own `ChipWait` is altered.
Sleeplock are most effective for scripts designed to be directly activated by other scripts.


> **Example**
>
> | | Chip |
> |-|-|
> |1|:ChipWait = -1|
> |2|*// this line will not be executed until an external source sets :ChipWait to 0*  |

## Waitlock
A waitlock is a variant of a Sleeplock, which include a built-in timeout. This allow it to reactivate itself on its own after a set time has past.
This method as the share the same advantages and issues than the sleeplock, with the exception of being time-limited.
Waitlocks are most effective for timers and implementing fallback systems in case a subscript is non-responding.

> **Example**
>
> | | Chip |
> |-|-|
> |1|:ChipWait = 300|
> |2|*// this line will not be executed until an external source sets :ChipWait to 0 or 300 chip tick (1 minute) passes.*  |

# Composite Locks
Composite Locks are lock composed of a combination of locks. They can be more complex to set up, but allow can give unique advantages, or mitigate the limitation of other locks.

## Conditional Sleeplock
Conditional Sleeplock are a combination of a Looplock and a Sleeplock, which allow for the lock to verify if an arbitrary condition is met as soon as it is awaken.
It has the advantage of not running constantly, but the drawback of requiring another device to wake it up.

> **Example**
>
> | | Chip |
> |-|-|
> |1| if :condition then goto 2 else :ChipWait = -1 goto 1|
> |2|*// this line will not be executed until the condition is realised AND an external source sets :ChipWait to 0*  |

> **Example - Inversed**
>
> <sup>Depending on the condition, this method can be shorter than a normal Sleeplock</sup>
>
> | | Chip |
> |-|-|
> |1|if :condition then :ChipWait = -1 goto 1 end|
> |2|*// this line is executed only once the condition is not realized AND an external source sets :ChipWait to 0*  | 

## Timed Looplock
Timed Looplock work in the same way as looplock, but check the condition every time a given interval of time passes, instead of every chip tick.
This lock is useful if you need to act in sync with other device, based on a condition that could become true at any time.

> **Example**
>
> | | Chip |
> |-|-|
> |1|if :condition then goto 2 end :ChipWait = 300 goto 1|
> |2|*// Every 300 chip tick (1 minute), the script will verify the condition. If it is true, this line will be executed*  |

> **Example - Inversed**
>
> <sup>Depending on the condition, this method can be shorter than a normal Sleeplock</sup>
>
> | | Chip |
> |-|-|
> |1|if :condition then :ChipWait = 300 goto 1 end|
> |2|*// Every 300 chip tick (1 minute), the script will verify the condition. If it is not true, this line will be executed*  | 

# Multilocks
A Multilock is a sequence of locks, which require activation in sequence for the script to activate. This can be used to ensure that the correct sequence of inputs are realised before activating a device, or to react if a series of circumstances occurs.

It is possible to build multilocks to including, for example, the need for all the lock to open in a certain timeframe, or to be done step by step and to reset itself if one step is missed.

> **Example - Basic Multilock**
>
> | | Chip |
> |-|-|
> |1|if :cond1 then goto 2 end goto 1|
> |2|if :cond2 then goto 3 end goto 2|
> |3|if :cond3 then goto 4 end goto 3|
> |4|*// This line will be executed if :cond1, :cond2 and :cond3 are realized. Once :cond1 and :cond2 is realized and its lock is passed, it doesn't need to stay realized.*  |

> **Example - Step by Step Multilock**
>
> | | Chip |
> |-|-|
> |1|if :cond1 then Chipwait = -1 goto 2 end Chipwait = -1 goto 1|
> |2|if :cond2 then Chipwait = -1 goto 3 end Chipwait = -1 goto 1|
> |3|if :cond3 then Chipwait = -1 goto 4 end Chipwait = -1 goto 1|
> |4|*// This line will be executed if for each condition, it is realized and an external source sets :Chipwait to 0. If any step fails, the lock resets.*  |

> **Example - Timed Multilock**
>
> | | Chip |
> |-|-|
> |1|if :cond1 then timer = 300 goto 2 end goto 1|
> |2|if :cond2 then goto 3 end if --timer > 0 then goto 2 end goto 1|
> |3|if :cond3 then goto 4 end if --timer > 0 then goto 3 end goto 1|
> |4|*// This line will be executed if :cond1, :cond2 and :cond3 are realized in a time of 300 chip ticks (1 minute).*  |

