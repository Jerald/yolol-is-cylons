# YOLOL Concepts : Simple Lists
*Document Status : Theoretical - none of the methods have been tested.*

Lists are data structures which organize sets of values in a list of countable values. The following lists are the simplest to setup and use.

> **Multiscript safety**: The following implementations are **not** designed to be safely used by multiple concurrent scripts. If two scripts attempt the access those lists at the same time, unintended result may occur. Multiscript-safe lists will be presented in a follow up document at a later time.

## Indexed Lists
Indexed Lists are a type of list which allow for direct access to its content using an index value.

### Single-chip list
A single-chip list is a list stored on a single YOLOL chip, but is limited to a size of 21 items. It requires three external variables, the first to receive the index, the second to transmit the value of the item in the list, and the third to indicate the action.

> [Single-chip indexed list code](./scripts/lists_single-chip-indexed-list.yolol)
> 
> <sub>In this code, the `:chipwait` field of the chip is renamed `:listwait`. In addition, this code uses the external variables `:i`, `:v` and `:act`, which must be defined.</sub>
>  
>  **Using a single-chip list**
>  <sub>In  the following script, the code uses `:chipwait=2` to wait for 2 chip ticks, ensuring that execution of the action is completed.</sub>
>  
>  | | Chip |
>  |-|-|
>  |1|*// fetch the first two elements (indexes 0 and 1) of the list*|
>  |2|:i=0 :act="get" :listwait=0 :chipwait=2|
>  |3|a=:v :i=1 :act="get" :listwait=0 :chipwait=2|
>  |4|b=:v|
>  |5| |
>  |6|*// set the value of the third element (index 2) of the list to the sum of the first two.*|
>  |7|:i=2 :v=a+b :act="set" :listwait=0 :chipwait=2|

### Multi-chip list
A multi-chip list is a extension of the single-chip list, with no theoretical limit of size. The following implementation limited to a size of 12 items per chip, with any number of additional chips possible. Like the Single-chip list, it only requires three external variables to work.

> [Multi-chip indexed list code](./scripts/lists_single-chip-indexed-list.yolol)
> 
> <sub>This code is the code for the first chip of the system. For every additional chip, change the value of the `chipnumber` variable on line 1 of the script</sub>
> <sub>All chips of the list must have their `:chipwait` field renamed to `:listwait`. In addition, this code uses the external variables `:i`, `:v` and `:act`, which must be defined.</sub>
>
> **Using a multi-chip list**
> A multi-chip list is used in exactly the same way as a single-chip list.

### Memchip list
Both the single-chip and multi-chip lists shown before use yolol variables to store the list values. However, in some circumstances, you may want the content of the list to be stored on a memory chip. The following implementation uses one Yolol chip for every memory chip used, each chip storing 10 items.
> **Memory chip indexed list code:** [1st chip](./scripts/lists_single-chip-indexed-list.yolol), [2nd chip](./scripts/lists_single-chip-indexed-list.yolol) [3rd chip](./scripts/lists_single-chip-indexed-list.yolol)
> 
> <sub>Those files present the scripts of the first 3 yolol chips in a memory chip list. Any additional yolol chips added can follow the same logic, but require you to edit the chipnumber with the number of the chip, as well as the name external variables storing the list content.</sub>
> <sub>Each yolol chip needs a memory chip with the fields named from mcv0 to mcv9 for the first chip, mcv10 or mcv19 for the second, and so on.</sub>
> 
> **Using a Memchip list**
> A memory chip list is used in exactly the same way as a single-chip list.

## Stacks
Stacks are lists which allow scripts to manipulate its data in a LIFO (last in, first out) way. They allow a script to push and pop data from the tail of the list only. In YOLOL, they can be simulated using a indexed list.

> [Stack code](./scripts/lists_stack.yolol) <sup>(require an indexed list)</sup>
> 
> <sub>In this code, the `:chipwait` field of the chip is renamed `:stackwait`. In addition, you must set the value of the `maxsize` variable in the first line of the script to the maximum size of the list.</sub>
>  
>  **Using a stack**
   
>  <sub>In  the following script, the code uses `:chipwait=3` to wait for 3 chip ticks, ensuring that execution of the action is completed.</sub>
>  
>  | | Chip |
>  |-|-|
>  |1|*// push : add a value on top of the stack. if the stack is full, skip.*|
>  |2|:v=42 :act="push" :stackwait=0 :chipwait=3|
>  |3| |
>  |4|*// peek : get the top value without removing it from the stack*|
>  |5|:act="peek" :stackwait=0 :chipwait=3|
>  |6|value = :v|
>  |7| |
>  |8|*// pop : get and remove the value on top the stack.*|
>  |9|:act="pop" :stackwait=0 :chipwait=3|
>  |10|value = :v|

## Queues
Queues are lists which allow scripts to manipulate its data in a FIFO (first in, first out) way. They allow a script to add data to the tail, but remove them from the head. Like stacks, in YOLOL, they can be simulated using an indexed list.

> [Queue code](./scripts/lists_queue.yolol) <sup>(require an indexed list)</sup>
> 
> <sub>In this code, the `:chipwait` field of the chip is renamed `:queuewait`. In addition, you must set the value of the `maxsize` variable in the first line of the script to the maximum size of the list.</sub>
>  
>  **Using a queue**
>  
>  <sub>In  the following script, the code uses `:chipwait=3` to wait for 3 chip ticks, ensuring that execution of the action is completed.</sub>
>  
>  | | Chip |
>  |-|-|
>  |1|*// push : add a value at the end of the queue. if the queue is full, skip.*|
>  |2|:v=42 :act="push" :queuewait=0 :chipwait=3|
>  |3| |
>  |4|*// peek : get the first value of the queue without removing*|
>  |5|:act="peek" :queuewait=0 :chipwait=3|
>  |6|value = :v|
>  |7| |
>  |8|*// pop : get and remove the first value of the queue.*|
>  |9|:act="pop" :queuewait=0 :chipwait=3|
>  |10|value = :v|

## Deques - Double-ended Queues
Double-ended queues, or deques are lists which allows scripts to add and remove data from either the head to the tail of the list.

> [Deque code](./scripts/lists_deque.yolol) <sup>(require an indexed list)</sup>
> 
> <sub>In this code, the `:chipwait` field of the chip is renamed `:dequewait`. In addition, you must set the value of the `maxsize` variable in the first line of the script to the maximum size of the list.</sub>
>  
>  **Using a deque**
>  
>  <sub>In  the following script, the code uses `:chipwait=3` to wait for 3 chip ticks, ensuring that execution of the action is completed.</sub>
>  
>  | | Chip |
>  |-|-|
>  |1|*// unshift : add a value at the beginning of the queue. if the queue is full, skip.*|
>  |2|:v=20 :act="unshift" :dequewait=0 :chipwait=3|
>  |3| |
>  |4|*// push : add a value at the end of the queue. if the queue is full, skip.*|
>  |5|:v=42 :act="push" :dequewait=0 :chipwait=3|
>  |6| |
>  |7|*// shift : get and remove the first value of the queue.*|
>  |8|:act="shift" :dequewait=0 :chipwait=3|
>  |9|value = :v|
>  |10| |
>  |11|*// pop : get and remove the last value of the queue.*|
>  |12|:act="pop" :dequewait=0 :chipwait=3|
>  |13|value = :v|
>  |14| |
>  |15|*// front : get the first value of the deque without removing.*|
>  |16|:act="front" :dequewait=0 :chipwait=3|
>  |17|value = :v|
>  |18| |
>  |19|*// back : get the last value of the deque without removing.*|
>  |20|:act="back" :dequewait=0 :chipwait=3|
>  |21|value = :v|
