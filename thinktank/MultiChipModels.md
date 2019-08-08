## Multi Chip Models For Yolol

Multiple Yolol chips can be set up to interact in different ways for two primary purposes: speed (processing several lines of code at once) and space (allowing more than 20 lines of code in a single program).

### Functions

A function can be moved to another chip and then invoked to do some work, while the function is running on the other chip the calling chip is blocked (waiting for the result).

This technique purely saves space and does not increase speed.

Example implementation:

```
// Chip 1
:p1 = "parameter" :p2 = "parameter" :p3 = 3 :call = 1 // Set parameters and call function
if :call == 1 then goto 2 end                         // Wait for execution to finish
result = :r1                                          // Fetch result
```

```
// Chip 2
if :call == 0 then goto 1 end // Wait for function to be called
:result = :p1 + :p2 + :p3     // Execute function body; this can be as many lines as necessary
:call = 0 goto 1              // Indicate that the function is complete
```

### Channels

A channel is a way to communicate between two running chips. Sending to a channel which already contains a value blocks until the channel is empty. Reading from a channel with no value blocks until the channel has an available value.

This technique can save space and provide modest speedups.

### Unsynchronised Threads

Each chip can be considered a separate thread, running at its own speed.

This is the simplest model to support for a language design perspective, but is likely the most complex to implement because it exposes the details of the yolol memory model. e.g. what is the result of reading and writing multiple external variables in a single line? a language compiled into this form would have to expose these details to the programmer.

### Pipelining

Each chip can be considered a single line of code, this does not reduce latency but can vastly increase throughput.

This example code reads a sensor, processes it and repeats that loop:

```
v = :read_sensor
range_lo = v < 10 range_hi = v > 20
if range_lo or range_hi then v2 = 0 else v2 = v end
:output = v2 / 100 goto 1
```

This reads the sensor value and updates the output once every 800ms (4 lines of code, 200ms per line). This can instead be pipelined as this:

```
:v = :read_sensor goto 1
```

```
v = :v :range_lo = v < 10 range_hi = v > 20 :v2 = v goto 1
```

```
if :range_lo or :range_hi then :v3 = 0 else :v3 = :v2 end goto 1
```

```
:output = :v3 goto 1
```

This new pipelined implementation reads the sensor every 200ms and updates the output variable every 200ms, although the total latency is still the same (4 lines over 4 chips, 200ms per line) the throughput is 4x greater.
