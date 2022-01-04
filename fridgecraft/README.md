# Smart Fridge

link: [https://katalyst.codurance.com/smart-fridge](https://katalyst.codurance.com/smart-fridge)

```websequence
title FridgeCraft Kata
actor Person

Person->Fridge: signalFridgeDoorOpened()

Fridge->ItemScanner: scanAddedItem()
Fridge->Repository: addItem()

Person->Fridge: signalFridgeDoorClosed()
Fridge->Clock: simulateDayOver()

Person->Fridge: showDisplay()

Person->Fridge: signalFridgeDoorOpened()
Fridge->ItemScanner: scanRemovedItem()

Person->Fridge: signalFridgeDoorClosed()
Fridge->Clock: simulateDayOver()

Person->Fridge: showDisplay()
```
