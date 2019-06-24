# YOLOL Concepts : Simple Lists
*Document Status : Theoritical - none of the methods have been tested.*

Lists are data structures which organize sets of values in a list of countable values. The following lists are the simplest to setup and use.

> **Multiscript safety**: The following implementations are **not** designed to be safely used by multiple concurrent scripts. If two scripts attempt the access those lists at the same time, unintended result may occur. For Multiscript-safe lists, consult the [Advanced Lists](./concepts_advanced_lists.md) document.

## Indexed Lists
Indexed Lists are a type of list which allow for direct access to its content using an index value.

### Single-chip list
A single-chip list uses only a single YOLOL chip, but is limited to a size of 21 items. It requires three external variables, the first to receive the index, the second to transmit the value of the item in the list, and the third to indicate the action.

> [Single-chip indexed list code](./scripts/lists_single-chip-indexed-list.txt)
> <sub>In this code, the `:chipwait` field of the chip is renamed `:listwait`. In addition, this code uses the external variables `:i`, `:v` and `:act`, which must be defined.</sub>
>  
>  **Usage Sample of a single-chip list**
>  <sub>In  the following script, the code uses `:chipwait=2` to wait for 2 chip ticks, ensuring that the result has been returned.</sub>
>  
>  | | Chip |
>  |-|-|
>  |1|*// fetch the first two elements (indexes 0 and 1) of the list*|
>  |2|:i=0 :act="get" :listwait=0 :chipwait=2|
>  |3|a=:v :i=1 :act="get" :listwait=0 :chipwait=2|
>  |4|b=:v|
>  |5|*// set the value of the third element (index 2) of the list to the sum of the first two.*|
>  |6|:i=2 :v=a+b :act="set" :listwait=0 :chipwait=2|


## Stacks
Stacks are lists which allow scripts to manipulate its data in a LIFO (last in, first out) way. They allow a script to push and pop data from the tail of the list only.


## Queues
Queues are lists which allow scripts to manipulte its data in a FIFO (first in, first out) way. They allow a script to add data to the tail, but remove them from the head.



## Deques - Double-ended Queues
Double-ended queues, or deques are lists which allows scripts to add and remove data from either the head to the tail of the list.
