```mermaid
graph LR
A --> B
A --> D
B --> C
D --> E
E --> C
```

```mermaid
sequenceDiagram
participant A
participant B
participant C

A ->> B: Hello
B ->> C: Hello
C -->> A: Bye
```
