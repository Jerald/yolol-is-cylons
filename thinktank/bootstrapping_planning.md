# Bootstrapping Planning

Yolol as a language is quite limiting. Adding in the restrictions on how it works that are present in Starbase itself, complicated computation is a massive undertaking. To that end, we need to setup a plan for how to [bootstrap](https://en.wikipedia.org/wiki/Bootstrapping) ourselves to the point of being able to make more complicated systems.

Below is a set of steps we should acomplish to be able to get ourselves the tools to create complicated systems. They are a rough outline, and need to be refined as time goes on.

## Step 1: function call protocol

Yolol has no way to trigger code on another chip, in the same style as a function call might be. Having the ability to organize code to exist in other locations is very useful normally, but within the world of Starbase, where yolol chips have only 20 lines, it's absolutely essential.

The goal for this step would be to have a simple design for how one chip (the "caller") can trigger some sort of code execution on another chip (the "callee") while passing input to it. Having this complete paves the way for many new features down the line.

A current theoretical for this has been proposed by Aralicia#0278 and Matrixmage#4830 where we use the [ChipWait functionality](https://wiki.starbasegame.com/index.php/YOLOL_Chip) to block the caller's execution until the callee has finished the work. The caller would pass parameters to the callee by setting specific fields which the callee would know how to interpret as the input. This is actually quite similar to the real-world x86 function call protocol called [cdecl](https://en.wikipedia.org/wiki/X86_calling_conventions).
