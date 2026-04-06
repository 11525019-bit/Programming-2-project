```Mermaid
stateDiagram-v2
    Start --> WakeUp

    WakeUp --> PhoneRings
    PhoneRings --> WalkOutside
    WalkOutside -->  MeetLuna

    MeetLuna --> WalkAndTalk
    WalkAndTalk --> ConvenienceStore
    ConvenienceStore --> BuyDrinks
    BuyDrinks --> WindowTalk

    WindowTalk --> ExistentialThoughts
    ExistentialThoughts --> ParkScene
    ParkScene --> DeepConversation

    DeepConversation --> Total_point_check
    Total_point_check --> Bad_ending
    Total_point_check --> Locked_ending
    Total_point_check --> Death_ending
    Total_point_check --> Chess_ending
    

    Bad_ending --> End
    Locked_ending --> End
    Death_ending --> End
    Chess_ending --> End
```
