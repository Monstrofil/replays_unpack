.travis.yml# Getting exposed index for properties and methods

To get exposed id, both clients, WoT and WoWS are doing the same stuff, so this package is suitable for both.

Here is the algorithm:
- parse scripts/alias.xml file in order to be able to transform aliases into primitive types (INT16, BLOB, etc)
- for each .def file, do the following:
 - if 'Parent' or 'Implement' section exists, parse that .def file first
 - save exposed methods into array
- finally sort exposed methods by payload size, index of method in sorted array is what you need
For properties do the same.

## What properties are exposed
Regarding bigworld docs, exposed properties have the following flags:
- ALL_CLIENTS
- BASE_AND_CLIENT
- OTHER_CLIENTS
- OWN_CLIENT
- CELL_PUBLIC_AND_OWN
All other properties are available only for server-side scripts.

## What methods I should parse
Exposed indexes are different for each section of .def file. Regarding replays you need only ClientMethods section.


p.s. Many thanks to Dragon armor and his post https://koreanrandom.com/forum/topic/45855-/?do=findComment&comment=436717