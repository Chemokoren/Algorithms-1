"""
script removes lines starting with numbers
e.g.
----------input -------
1
00:00:00,150 --> 00:00:04,920
In this section we will write Python program to implement QS using Linked List.

2
00:00:04,990 --> 00:00:08,710
It cleared up by then pi and give it the name as queue link.

----------output -------

In this section we will write Python program to implement QS using Linked List.
It cleared up by then pi and give it the name as queue link.
"""


input_file  ="linkedDeque.srt"
output_file ="linkedDeque.srt1"

output = open(output_file, "w")

with open(input_file) as input:
    for line in input:
        if not line[0].isdigit():
            output.write(line)
            print(line)
#rm -rf input_file
output.close()
