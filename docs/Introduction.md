# Basic format

## Header
Every replay starts off with an 8 byte header, consisting of the following values:

- magic number - An unsigned 32 bit integer (4 bytes)
- block count - An unsigned 32 bit integer (4 bytes)
The block count is an indication of how many data blocks (excluding the real replay data) are stored inside the replay.

## Blocks
Every data block starts with an unsigned 32 bit integer that holds the length of the data for the given block. The first block consists of a JSON encoded structure.

## Reading
- Open the replay file
- Seek to offset 4 in the replay file (skipping the magic number)
- Read 4 bytes, and interpret these as an unsigned 32 bit integer, let this be "block count"
- For every block take the following action:
    - Read 4 bytes, and interpret these as an unsigned 32 bit integer, let this be "data length"
    - Read "data length" bytes
- Once all blocks have been read, the remainder of the data in the file is the compressed and encrypted replay data

_Via <http://wiki.vbaddict.net/pages/File_Replays>_